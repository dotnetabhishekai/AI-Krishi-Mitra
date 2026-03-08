"""
Forms for farmers app
"""
from django import forms
from django.contrib.auth.models import User
from .models import FarmerProfile, Message


class FarmerRegistrationForm(forms.ModelForm):
    """Simplified farmer registration form"""
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )
    full_name = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name (Optional)'})
    )
    
    class Meta:
        model = FarmerProfile
        fields = ['language', 'phone_number', 'location', 'state', 'district', 'farm_size']
        widgets = {
            'language': forms.Select(attrs={'class': 'form-select', 'id': 'language-select'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+91XXXXXXXXXX'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City/Village'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'District'}),
            'farm_size': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Farm size in hectares'}),
        }
    
    crops_text = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter crops separated by commas (e.g., rice, wheat, cotton)',
            'id': 'crops-input'
        }),
        help_text='Enter crop names separated by commas'
    )
    
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        return username
    
    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if FarmerProfile.objects.filter(phone_number=phone).exists():
            raise forms.ValidationError("Phone number already registered")
        return phone


class FarmerProfileForm(forms.ModelForm):
    """Form for farmer profile"""
    
    class Meta:
        model = FarmerProfile
        fields = ['phone_number', 'location', 'state', 'district', 'crops', 'farm_size', 'language']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+91XXXXXXXXXX'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City/Village'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'crops': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., ["rice", "wheat"]'}),
            'farm_size': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Hectares'}),
            'language': forms.Select(attrs={'class': 'form-select'}),
        }


class MessageForm(forms.ModelForm):
    """Form for sending messages"""
    
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Type your message...'
            }),
        }
