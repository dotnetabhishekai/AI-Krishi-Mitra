"""
Views for farmers app
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import logging

from .models import FarmerProfile, Conversation, Message, Interaction
from .forms import FarmerProfileForm, MessageForm, FarmerRegistrationForm
from .translations import get_all_translations
from aws_services.bedrock import BedrockService
from aws_services.transcribe import TranscribeService
from aws_services.polly import PollyService
from aws_services.s3 import S3Service
from aws_services.weather import WeatherService

logger = logging.getLogger(__name__)

# Initialize AWS services
bedrock_service = BedrockService()
transcribe_service = TranscribeService()
polly_service = PollyService()
s3_service = S3Service()
weather_service = WeatherService()


def _safe_voice_response(text, language):
    """Generate TTS URL best-effort and return None on failure."""
    try:
        return polly_service.synthesize(text, language)
    except Exception as exc:
        logger.error(f"Error generating voice response: {str(exc)}")
        return None


def _reset_guest_chat(session):
    """Reset guest onboarding/session context for chat."""
    session['guest_chat_state'] = 'awaiting_location'
    session['guest_chat_profile'] = {}
    session.modified = True


def _handle_guest_message(message_content, session):
    """Guide anonymous users through basic onboarding questions before chat."""
    state = session.get('guest_chat_state')
    profile = session.get('guest_chat_profile', {})

    if message_content.lower() in {'restart', 'start over', 'reset'}:
        _reset_guest_chat(session)
        return (
            "Sure, let's start again. Which area do you live in? "
            "Please share village/town, district, and state."
        )

    if not state:
        _reset_guest_chat(session)
        return (
            "Welcome to AI Krishi Mitra. Before we start, please tell me your area "
            "(village/town, district, and state)."
        )

    if state == 'awaiting_location':
        profile['location'] = message_content
        session['guest_chat_profile'] = profile
        session['guest_chat_state'] = 'awaiting_problem'
        session.modified = True
        return (
            "Thank you. Please describe the main farming problem you are facing now "
            "(crop, pest, disease, weather, soil, or market issue)."
        )

    if state == 'awaiting_problem':
        profile['problem'] = message_content
        session['guest_chat_profile'] = profile
        session['guest_chat_state'] = 'ready'
        session.modified = True

        prompt = (
            "You are an agriculture assistant. A guest farmer has shared details. "
            f"Location: {profile.get('location', 'Unknown')}. "
            f"Problem: {profile.get('problem', 'Not provided')}. "
            "Give practical and safe first-step advice in simple language, then ask one useful follow-up question."
        )
        return bedrock_service.generate_response(prompt, "Guest onboarding complete")

    prompt = (
        "You are helping a guest farmer. Use this context and answer clearly with practical steps. "
        f"Location: {profile.get('location', 'Unknown')}. "
        f"Main problem: {profile.get('problem', 'Not provided')}. "
        f"Current message: {message_content}"
    )
    return bedrock_service.generate_response(prompt, "Guest chat context")


def home(request):
    """Home page"""
    return render(request, 'farmers/home.html')


def logout_view(request):
    """Logout user and redirect to home"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


def register(request):
    """Farmer registration with language-first approach"""
    if request.method == 'POST':
        form = FarmerRegistrationForm(request.POST)
        if form.is_valid():
            # Create user account
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data.get('full_name', '').split()[0] if form.cleaned_data.get('full_name') else '',
                last_name=' '.join(form.cleaned_data.get('full_name', '').split()[1:]) if form.cleaned_data.get('full_name') and len(form.cleaned_data.get('full_name', '').split()) > 1 else ''
            )
            
            # Create farmer profile
            profile = form.save(commit=False)
            profile.user = user
            profile.approval_status = 'pending'
            
            # Parse crops from comma-separated text
            crops_text = form.cleaned_data.get('crops_text', '')
            if crops_text:
                crops_list = [crop.strip() for crop in crops_text.split(',') if crop.strip()]
                profile.crops = crops_list
            
            profile.save()
            
            messages.success(request, 'Registration successful! Your account is pending admin approval.')
            return redirect('registration_pending')
    else:
        form = FarmerRegistrationForm()
    
    return render(request, 'farmers/register.html', {'form': form})


def registration_pending(request):
    """Show pending registration message"""
    return render(request, 'farmers/registration_pending.html')


@require_http_methods(["POST"])
def transcribe_voice_input(request):
    """Transcribe voice input for registration form"""
    try:
        audio_file = request.FILES.get('audio')
        language = request.POST.get('language', 'en')
        field_name = request.POST.get('field_name', '')
        
        if not audio_file:
            return JsonResponse({'error': 'No audio file provided'}, status=400)
        
        # Upload to S3 (or save locally in mock mode)
        try:
            s3_url = s3_service.upload_audio(audio_file, 'registration')
        except:
            # Mock mode - save locally
            s3_url = 'local://audio/registration.ogg'
        
        # Transcribe audio
        transcript = transcribe_service.transcribe(s3_url, language)
        
        if not transcript:
            return JsonResponse({'error': 'Failed to transcribe audio'}, status=500)
        
        return JsonResponse({
            'success': True,
            'transcript': transcript,
            'field_name': field_name
        })
        
    except Exception as e:
        logger.error(f"Error transcribing voice: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)


@login_required
def dashboard(request):
    """Farmer dashboard"""
    # If user is admin/staff without farmer profile, redirect to admin panel
    if request.user.is_staff and not hasattr(request.user, 'farmer_profile'):
        return redirect('/admin/')
    
    try:
        farmer_profile = request.user.farmer_profile
        
        # Check approval status
        if farmer_profile.approval_status == 'pending':
            return redirect('registration_pending')
        elif farmer_profile.approval_status == 'rejected':
            return render(request, 'farmers/registration_rejected.html', {
                'reason': farmer_profile.rejection_reason
            })
            
    except FarmerProfile.DoesNotExist:
        return redirect('profile_setup')
    
    # Get recent conversations
    recent_conversations = Conversation.objects.filter(
        farmer=farmer_profile
    )[:5]
    
    # Get recent interactions
    recent_interactions = Interaction.objects.filter(
        farmer=farmer_profile
    )[:10]
    
    # Get weather data
    weather = None
    if farmer_profile.location and farmer_profile.location != 'Unknown':
        weather = weather_service.get_weather(farmer_profile.location)
    
    # Get translations for user's language
    translations = get_all_translations(farmer_profile.language)
    
    context = {
        'farmer': farmer_profile,
        'conversations': recent_conversations,
        'interactions': recent_interactions,
        'weather': weather,
        'trans': translations,
    }
    
    return render(request, 'farmers/dashboard.html', context)


def chat(request, conversation_id=None):
    """Chat interface"""
    if request.user.is_authenticated:
        try:
            farmer_profile = request.user.farmer_profile
        except FarmerProfile.DoesNotExist:
            return redirect('profile_setup')

        # Get or create conversation
        if conversation_id:
            conversation = get_object_or_404(
                Conversation,
                id=conversation_id,
                farmer=farmer_profile
            )
        else:
            conversation = Conversation.objects.create(
                farmer=farmer_profile,
                title="New Conversation"
            )
            return redirect('chat_with_id', conversation_id=conversation.id)

        context = {
            'conversation': conversation,
            'conversation_id': conversation.id,
            'messages': conversation.messages.all(),
            'all_conversations': Conversation.objects.filter(farmer=farmer_profile, is_active=True),
            'farmer': farmer_profile,
            'guest_mode': False,
        }
        return render(request, 'farmers/chat.html', context)

    if conversation_id:
        return redirect('chat')

    if 'guest_chat_state' not in request.session:
        _reset_guest_chat(request.session)

    context = {
        'conversation': None,
        'conversation_id': 0,
        'messages': [],
        'all_conversations': [],
        'farmer': None,
        'guest_mode': True,
    }
    return render(request, 'farmers/chat.html', context)


@require_http_methods(["POST"])
def send_message(request):
    """Send a text message"""
    try:
        data = json.loads(request.body)
        conversation_id = data.get('conversation_id')
        message_content = data.get('message', '').strip()
        input_mode = (data.get('input_mode') or 'text').strip().lower()
        language = (data.get('language') or 'en').strip().lower()
        is_voice_input = input_mode == 'voice'
        
        if not message_content:
            return JsonResponse({'error': 'Message cannot be empty'}, status=400)
        
        is_authenticated_farmer = request.user.is_authenticated and hasattr(request.user, 'farmer_profile')

        if is_authenticated_farmer:
            farmer_profile = request.user.farmer_profile
            conversation = get_object_or_404(
                Conversation,
                id=conversation_id,
                farmer=farmer_profile
            )
        else:
            farmer_profile = None
            conversation = None
        
        # Save farmer's message
        if conversation:
            farmer_message = Message.objects.create(
                conversation=conversation,
                sender_type='farmer',
                message_type='voice' if is_voice_input else 'text',
                content=message_content
            )
        else:
            farmer_message = None
        
        # Generate AI response
        if farmer_profile:
            context = build_farmer_context(farmer_profile)
            ai_response = bedrock_service.generate_response(message_content, context)
        else:
            ai_response = _handle_guest_message(message_content, request.session)

        # Always return voice if user used voice input.
        audio_url = _safe_voice_response(ai_response, language) if is_voice_input else None
        
        # Save AI response
        if conversation:
            ai_message = Message.objects.create(
                conversation=conversation,
                sender_type='ai',
                message_type='voice' if is_voice_input else 'text',
                content=ai_response,
                metadata={'audio_url': audio_url} if audio_url else {}
            )
        else:
            ai_message = None
        
        # Log interaction
        if farmer_profile:
            Interaction.objects.create(
                farmer=farmer_profile,
                interaction_type='voice_query' if is_voice_input else 'text_query',
                query=message_content,
                response=ai_response
            )
        
        # Update conversation
        if conversation and farmer_message:
            conversation.updated_at = farmer_message.created_at
            conversation.save()
        
        return JsonResponse({
            'success': True,
            'farmer_message': {
                'id': farmer_message.id if farmer_message else None,
                'content': farmer_message.content if farmer_message else message_content,
                'created_at': farmer_message.created_at.isoformat() if farmer_message else None,
            },
            'ai_message': {
                'id': ai_message.id if ai_message else None,
                'content': ai_message.content if ai_message else ai_response,
                'created_at': ai_message.created_at.isoformat() if ai_message else None,
            }
            ,
            'audio_url': audio_url,
            'input_mode': input_mode,
        })
        
    except Exception as e:
        logger.error(f"Error sending message: {str(e)}")
        # If original input was voice, return a spoken fallback response instead of hard error.
        try:
            data = json.loads(request.body)
        except Exception:
            data = {}

        input_mode = (data.get('input_mode') or 'text').strip().lower()
        language = (data.get('language') or 'en').strip().lower()

        if input_mode == 'voice':
            fallback_text = "Sorry, I could not process your request right now. Please try again."
            fallback_audio_url = _safe_voice_response(fallback_text, language)
            return JsonResponse({
                'success': True,
                'ai_message': {
                    'content': fallback_text,
                    'created_at': None,
                },
                'audio_url': fallback_audio_url,
                'input_mode': 'voice',
                'is_fallback': True,
            })

        return JsonResponse({'error': str(e)}, status=500)


@login_required
@require_http_methods(["POST"])
def upload_voice(request):
    """Upload and process voice message"""
    try:
        conversation_id = request.POST.get('conversation_id')
        audio_file = request.FILES.get('audio')
        
        if not audio_file:
            fallback_text = 'No audio file was provided. Please record and try again.'
            return JsonResponse({
                'success': False,
                'error': fallback_text,
                'audio_url': _safe_voice_response(fallback_text, request.POST.get('language', 'en')),
            }, status=400)
        
        farmer_profile = request.user.farmer_profile
        conversation = get_object_or_404(
            Conversation,
            id=conversation_id,
            farmer=farmer_profile
        )
        
        # Upload to S3
        s3_url = s3_service.upload_audio(audio_file, farmer_profile.phone_number)
        
        # Transcribe audio
        transcript = transcribe_service.transcribe(s3_url, farmer_profile.language)
        
        if not transcript:
            fallback_text = 'Sorry, I could not transcribe your voice. Please try speaking again.'
            return JsonResponse({
                'success': False,
                'error': fallback_text,
                'audio_url': _safe_voice_response(fallback_text, farmer_profile.language),
            }, status=500)
        
        # Save farmer's message
        farmer_message = Message.objects.create(
            conversation=conversation,
            sender_type='farmer',
            message_type='voice',
            content=transcript,
            audio_file=audio_file
        )
        
        # Generate AI response
        context = build_farmer_context(farmer_profile)
        ai_response = bedrock_service.generate_response(transcript, context)
        
        # Generate audio response
        audio_url = _safe_voice_response(ai_response, farmer_profile.language)
        
        # Save AI response
        ai_message = Message.objects.create(
            conversation=conversation,
            sender_type='ai',
            message_type='voice',
            content=ai_response,
            metadata={'audio_url': audio_url}
        )
        
        # Log interaction
        Interaction.objects.create(
            farmer=farmer_profile,
            interaction_type='voice_query',
            query=transcript,
            response=ai_response
        )
        
        return JsonResponse({
            'success': True,
            'transcript': transcript,
            'response': ai_response,
            'audio_url': audio_url
        })
        
    except Exception as e:
        logger.error(f"Error processing voice: {str(e)}")
        fallback_text = 'Sorry, voice processing failed. Please try again in a moment.'
        fallback_audio_url = _safe_voice_response(fallback_text, request.POST.get('language', 'en'))
        return JsonResponse({
            'success': False,
            'error': fallback_text,
            'audio_url': fallback_audio_url,
        }, status=500)


@login_required
@require_http_methods(["POST"])
def upload_image(request):
    """Upload and analyze crop/pest image"""
    try:
        conversation_id = request.POST.get('conversation_id')
        image_file = request.FILES.get('image')
        description = request.POST.get('description', '')
        
        if not image_file:
            return JsonResponse({'error': 'No image file provided'}, status=400)
        
        farmer_profile = request.user.farmer_profile
        conversation = get_object_or_404(
            Conversation,
            id=conversation_id,
            farmer=farmer_profile
        )
        
        # Upload to S3
        s3_url = s3_service.upload_image(image_file, farmer_profile.phone_number)
        
        # Save farmer's message
        farmer_message = Message.objects.create(
            conversation=conversation,
            sender_type='farmer',
            message_type='image',
            content=description or "Image uploaded for analysis",
            image_file=image_file
        )
        
        # Generate AI response (image analysis would use Rekognition in production)
        prompt = f"Farmer uploaded an image. Description: {description}. Provide agricultural advice."
        context = build_farmer_context(farmer_profile)
        ai_response = bedrock_service.generate_response(prompt, context)
        
        # Save AI response
        ai_message = Message.objects.create(
            conversation=conversation,
            sender_type='ai',
            message_type='text',
            content=ai_response
        )
        
        # Log interaction
        Interaction.objects.create(
            farmer=farmer_profile,
            interaction_type='image_query',
            query=f"Image: {description}",
            response=ai_response
        )
        
        return JsonResponse({
            'success': True,
            'image_url': s3_url,
            'response': ai_response
        })
        
    except Exception as e:
        logger.error(f"Error processing image: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)


@login_required
def profile_setup(request):
    """Setup or edit farmer profile"""
    try:
        farmer_profile = request.user.farmer_profile
    except FarmerProfile.DoesNotExist:
        farmer_profile = None
    
    if request.method == 'POST':
        form = FarmerProfileForm(request.POST, instance=farmer_profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('dashboard')
    else:
        form = FarmerProfileForm(instance=farmer_profile)
    
    return render(request, 'farmers/profile_setup.html', {'form': form})


def knowledge_base(request):
    """Browse agricultural knowledge base"""
    # Load knowledge from S3 or local cache
    try:
        knowledge = s3_service.get_knowledge_base()
    except:
        knowledge = {'crops': {}, 'pests': {}, 'diseases': {}}
    
    context = {
        'crops': knowledge.get('crops', {}),
        'pests': knowledge.get('pests', {}),
        'diseases': knowledge.get('diseases', {}),
    }
    
    return render(request, 'farmers/knowledge.html', context)


def weather_view(request):
    """Weather information page"""
    try:
        if request.user.is_authenticated:
            farmer_profile = request.user.farmer_profile
            location = farmer_profile.location
        else:
            location = 'India'
    except (FarmerProfile.DoesNotExist, AttributeError):
        location = 'India'
    
    weather = weather_service.get_weather(location)
    forecast = weather_service.get_forecast(location, days=7)
    alerts = weather_service.get_alerts(location)
    
    context = {
        'weather': weather,
        'forecast': forecast,
        'alerts': alerts,
        'location': location,
    }
    
    return render(request, 'farmers/weather.html', context)


def build_farmer_context(farmer_profile):
    """Build context string for AI"""
    context_parts = [
        f"Farmer location: {farmer_profile.location}",
        f"Main crops: {', '.join(farmer_profile.crops) if farmer_profile.crops else 'Not specified'}",
        f"Language: {farmer_profile.get_language_display()}",
        f"Farm size: {farmer_profile.farm_size} hectares" if farmer_profile.farm_size else "Farm size: Not specified"
    ]
    
    return "\n".join(context_parts)
