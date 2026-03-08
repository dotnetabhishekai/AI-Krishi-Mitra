# 🌾 AI Krishi Mitra - Agricultural AI Assistant

> An intelligent web-based agricultural advisory system powered by AWS AI services, designed to help Indian farmers with crop management, pest control, weather insights, and farming best practices.

[![Django](https://img.shields.io/badge/Django-5.0-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![AWS](https://img.shields.io/badge/AWS-Bedrock%20%7C%20S3%20%7C%20Polly-orange.svg)](https://aws.amazon.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo Accounts](#demo-accounts)
- [Quick Start](#quick-start)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Usage Guide](#usage-guide)
- [API Documentation](#api-documentation)
- [AWS Integration](#aws-integration)
- [Multi-Language Support](#multi-language-support)
- [Deployment](#deployment)
- [Cost Estimation](#cost-estimation)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

AI Krishi Mitra is a Django-based web application that provides farmers with an intelligent agricultural advisory system. The platform leverages AWS AI services (Bedrock, Transcribe, Polly) to deliver personalized farming advice through text, voice, and image interactions.

### Key Highlights

- 🤖 **AI-Powered Advice**: Uses AWS Bedrock (Claude 3) for intelligent agricultural recommendations
- 🗣️ **Voice Support**: Speech-to-text and text-to-speech in 8 Indian languages
- 📸 **Image Analysis**: Upload crop/pest photos for AI-powered diagnosis
- 🌦️ **Weather Integration**: Real-time weather data and agricultural advisories
- 👥 **User Management**: Complete registration, approval workflow, and profile management
- 📊 **Admin Dashboard**: Comprehensive admin panel for managing farmers and content
- 🌐 **Multi-Language**: Support for Hindi, English, Telugu, Tamil, Marathi, Punjabi, Kannada, Bengali, Gujarati

---

## ✨ Features

### For Farmers

✅ **Intelligent Chat Interface**
- Real-time messaging with AI agricultural advisor
- Context-aware responses based on location, crops, and farm size
- Conversation history and multiple chat sessions

✅ **Voice Interaction**
- Record voice queries in your preferred language
- AI responses converted to speech
- Hands-free operation for field use

✅ **Image Upload & Analysis**
- Upload photos of crops, pests, or diseases
- Get AI-powered diagnosis and treatment recommendations
- Visual problem identification

✅ **Personalized Dashboard**
- View recent conversations and interactions
- Weather widget with location-based forecasts
- Quick access to knowledge base and resources

✅ **Knowledge Base**
- Browse information on crops, pests, and diseases
- Search functionality for quick answers
- Best practices and farming tips

✅ **Weather Information**
- Current weather conditions
- 7-day forecast
- Agricultural advisories and alerts

### For Administrators

✅ **User Management**
- Approve/reject farmer registrations
- View and manage farmer profiles
- Reset user passwords

✅ **Content Management**
- Manage knowledge base content
- Monitor conversations and interactions
- View analytics and usage statistics

✅ **System Administration**
- Django admin panel with full control
- Database management
- Configuration settings

---

## 👤 Demo Accounts

The application comes with pre-configured test accounts:

### Admin Account
- **Username**: `admin`
- **Access**: Full admin panel access at `/admin/`

### Test Farmer Account
- **Username**: `testfarmer`
- **Password**: `test123`
- **Status**: Approved
- **Language**: Hindi
- **Access**: Dashboard, chat, and all farmer features

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- AWS Account (optional, for production features)
- Git

### Installation (5 minutes)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd poc-django
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings (AWS credentials optional for development)
   ```

4. **Initialize database**
   ```bash
   python manage.py migrate
   ```

5. **Create admin user** (optional, if not using demo accounts)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
   - Login with demo accounts above

### First Steps

1. **Login as Admin** 
   - Access admin panel at `/admin/`
   - View registered farmers
   - Approve pending registrations

2. **Login as Farmer** (`testfarmer` / `test123`)
   - View personalized dashboard in Hindi
   - Start a chat conversation
   - Ask agricultural questions
   - Upload images or use voice input

3. **Register New Farmer**
   - Click "Register" on home page
   - Select preferred language first
   - Fill in profile details (text or voice)
   - Wait for admin approval

---

## 🏗️ Architecture

### System Overview

```
┌─────────────┐
│   Browser   │
│  (Farmer)   │
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────────┐
│      Django Web Application         │
│  ┌─────────────────────────────┐   │
│  │  Views & API Endpoints      │   │
│  │  - Chat, Voice, Image       │   │
│  │  - Dashboard, Profile       │   │
│  │  - Knowledge Base, Weather  │   │
│  └─────────────┬───────────────┘   │
│                │                     │
│  ┌─────────────▼───────────────┐   │
│  │  Models & Database          │   │
│  │  - FarmerProfile            │   │
│  │  - Conversation, Message    │   │
│  │  - Interaction, Weather     │   │
│  └─────────────┬───────────────┘   │
│                │                     │
│  ┌─────────────▼───────────────┐   │
│  │  AWS Service Layer          │   │
│  │  - BedrockService           │   │
│  │  - TranscribeService        │   │
│  │  - PollyService             │   │
│  │  - S3Service                │   │
│  │  - WeatherService           │   │
│  └─────────────┬───────────────┘   │
└────────────────┼───────────────────┘
                 │
                 ▼
┌─────────────────────────────────────┐
│         AWS Cloud Services          │
│  ┌──────────────────────────────┐  │
│  │ Bedrock (Claude 3 Haiku)     │  │
│  │ - AI agricultural advice     │  │
│  └──────────────────────────────┘  │
│  ┌──────────────────────────────┐  │
│  │ Transcribe                   │  │
│  │ - Voice-to-text (8 langs)    │  │
│  └──────────────────────────────┘  │
│  ┌──────────────────────────────┐  │
│  │ Polly                        │  │
│  │ - Text-to-speech (Neural)    │  │
│  └──────────────────────────────┘  │
│  ┌──────────────────────────────┐  │
│  │ S3                           │  │
│  │ - Audio/image storage        │  │
│  └──────────────────────────────┘  │
└─────────────────────────────────────┘
```

### Request Flow

**Text Query Flow**:
```
Farmer types question → Django view → Build context → 
Bedrock (Claude) → AI response → Save to DB → Display to farmer
```

**Voice Query Flow**:
```
Farmer records audio → Upload to S3 → Transcribe to text → 
Build context → Bedrock (Claude) → AI response → 
Polly (text-to-speech) → Audio response → Display to farmer
```

**Image Query Flow**:
```
Farmer uploads image → Upload to S3 → Build context with description → 
Bedrock (Claude) → AI analysis → Save to DB → Display to farmer
```

---

## 🛠️ Technology Stack

### Backend
- **Framework**: Django 5.0
- **Language**: Python 3.11
- **Database**: SQLite (development), PostgreSQL (production)
- **AWS SDK**: boto3 1.34.34
- **Web Server**: Gunicorn 21.2.0
- **Static Files**: WhiteNoise 6.6.0

### Frontend
- **HTML5** with semantic markup
- **CSS3** with responsive design
- **JavaScript** (ES6+)
- **Bootstrap 5** for UI components
- **Web Audio API** for voice recording
- **Fetch API** for AJAX requests

### AWS Services
- **Bedrock**: AI responses (Claude 3 Haiku)
- **Transcribe**: Speech-to-text conversion
- **Polly**: Text-to-speech synthesis
- **S3**: Media file storage
- **IAM**: Access management

### Additional Libraries
- **django-crispy-forms**: Form rendering
- **crispy-bootstrap5**: Bootstrap 5 integration
- **djangorestframework**: API endpoints
- **django-cors-headers**: CORS handling
- **Pillow**: Image processing
- **python-dotenv**: Environment variables
- **requests**: HTTP client

---

## 📁 Project Structure

```
poc-django/
├── 📂 krishi_mitra/              # Django project configuration
│   ├── settings.py               # Project settings
│   ├── urls.py                   # Root URL configuration
│   ├── wsgi.py                   # WSGI application
│   └── __init__.py
│
├── 📂 farmers/                   # Main application
│   ├── 📂 migrations/            # Database migrations
│   ├── 📂 templates/             # HTML templates
│   │   └── 📂 farmers/
│   │       ├── home.html         # Landing page
│   │       ├── register.html     # Registration form
│   │       ├── login.html        # Login page
│   │       ├── dashboard.html    # Farmer dashboard
│   │       ├── chat.html         # Chat interface
│   │       ├── knowledge.html    # Knowledge base
│   │       ├── weather.html      # Weather page
│   │       ├── profile_setup.html
│   │       ├── registration_pending.html
│   │       └── registration_rejected.html
│   ├── models.py                 # Database models
│   ├── views.py                  # View functions
│   ├── urls.py                   # App URL patterns
│   ├── forms.py                  # Django forms
│   ├── admin.py                  # Admin configuration
│   ├── translations.py           # Multi-language support
│   └── __init__.py
│
├── 📂 aws_services/              # AWS integrations
│   ├── bedrock.py                # AI responses (Claude)
│   ├── transcribe.py             # Voice-to-text
│   ├── polly.py                  # Text-to-speech
│   ├── s3.py                     # File storage
│   ├── weather.py                # Weather service
│   └── __init__.py
│
├── 📂 static/                    # Static files (CSS, JS, images)
├── 📂 media/                     # User-uploaded files
├── 📂 staticfiles/               # Collected static files
│
├── 📄 manage.py                  # Django management script
├── 📄 requirements.txt           # Python dependencies
├── 📄 .env.example               # Environment template
├── 📄 db.sqlite3                 # SQLite database
│
├── 📄 README.md                  # This file
├── 📄 QUICKSTART.md              # Quick setup guide
├── 📄 POC-SUMMARY.md             # Project summary
├── 📄 REGISTRATION-GUIDE.md      # Registration workflow
├── 📄 MULTI-LANGUAGE-GUIDE.md    # Language support
├── 📄 LOGIN-GUIDE.md             # Login instructions
├── 📄 PASSWORD-RESET-GUIDE.md    # Password reset
├── 📄 BEDROCK-WORKFLOW-GUIDE.md  # AI workflow details
├── 📄 ACCESS-INFO.md             # Access credentials
└── 📄 RUNNING.md                 # Server instructions
```

### Key Files Explained

**Models** (`farmers/models.py`):
- `FarmerProfile`: User profile with location, crops, language
- `Conversation`: Chat sessions
- `Message`: Individual messages (text/voice/image)
- `Interaction`: Analytics and logging
- `WeatherData`: Cached weather information

**Views** (`farmers/views.py`):
- `home()`: Landing page
- `register()`: Farmer registration
- `dashboard()`: Personalized dashboard
- `chat()`: Chat interface
- `send_message()`: Text message API
- `upload_voice()`: Voice message API
- `upload_image()`: Image upload API
- `weather_view()`: Weather information

**AWS Services** (`aws_services/`):
- `BedrockService`: AI response generation
- `TranscribeService`: Audio transcription
- `PollyService`: Speech synthesis
- `S3Service`: File upload/download
- `WeatherService`: Weather data (mock/real)

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```bash
# Django Settings
SECRET_KEY=your-secret-key-here-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# AWS Credentials (Optional for development)
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_DEFAULT_REGION=ap-south-1

# AWS Resources
AWS_S3_BUCKET=krishi-mitra-media
AWS_DYNAMODB_TABLE=krishi-mitra-farmers

# Bedrock Configuration
BEDROCK_MODEL_ID=anthropic.claude-3-haiku-20240307-v1:0
```

### Operating Modes

**Development Mode (Mock AWS)**:
- No AWS credentials required
- Uses fallback responses for AI
- Local file storage instead of S3
- Perfect for UI/UX development

**Production Mode (Real AWS)**:
- AWS credentials required
- Real AI responses from Claude
- S3 for file storage
- Transcribe and Polly for voice

### AWS Setup (Optional)

1. **Create AWS Account**
   - Sign up at https://aws.amazon.com/

2. **Enable Bedrock Model Access**
   - Go to AWS Console → Bedrock → Model Access
   - Request access to "Claude 3 Haiku"
   - Wait for approval (usually instant)

3. **Create IAM User**
   - Go to IAM → Users → Create User
   - Attach policies:
     - `AmazonBedrockFullAccess`
     - `AmazonS3FullAccess`
     - `AmazonTranscribeFullAccess`
     - `AmazonPollyFullAccess`

4. **Generate Access Keys**
   - IAM → Users → Your User → Security Credentials
   - Create Access Key
   - Copy to `.env` file

5. **Create S3 Bucket**
   - Go to S3 → Create Bucket
   - Name: `krishi-mitra-media`
   - Region: `ap-south-1` (Mumbai)
   - Update bucket name in `.env`

For detailed AWS setup, see [BEDROCK-WORKFLOW-GUIDE.md](BEDROCK-WORKFLOW-GUIDE.md).

---

## 📖 Usage Guide

### For Farmers

#### 1. Registration

1. Visit the home page
2. Click "Register" button
3. **Select your preferred language first** (Hindi, English, Telugu, etc.)
4. Fill in your details:
   - Username and password
   - Full name
   - Phone number
   - Location (state, district)
   - Crops (comma-separated, e.g., "Wheat, Rice, Cotton")
   - Farm size in hectares
5. Use voice input for any field (click microphone icon)
6. Submit and wait for admin approval

#### 2. Login

1. Click "Login" on home page
2. Enter username and password
3. Access your personalized dashboard

#### 3. Using the Chat

1. Go to "Chat" from dashboard
2. **Text Query**: Type your question and press Enter
   - Example: "What fertilizer should I use for wheat?"
3. **Voice Query**: Click microphone icon, speak, and release
   - AI will transcribe and respond with voice
4. **Image Query**: Click camera icon, upload crop/pest photo
   - Add description and get AI analysis

#### 4. Dashboard Features

- **Weather Widget**: View current weather and 7-day forecast
- **Recent Conversations**: Quick access to chat history
- **Recent Interactions**: See your query history
- **Profile**: Update your information

#### 5. Knowledge Base

- Browse crops, pests, and diseases
- Search for specific information
- Read best practices and tips

### For Administrators

#### 1. Access Admin Panel

1. Login with admin credentials
2. Visit `/admin/` URL
3. Access full Django admin interface

#### 2. Manage Farmer Registrations

1. Go to "Farmer Profiles" in admin
2. View pending registrations
3. Click on a farmer to review details
4. Change "Approval status" to "Approved" or "Rejected"
5. Add rejection reason if rejecting
6. Save changes

#### 3. Reset Farmer Password

**Method 1: From List View**
1. Go to "Farmer Profiles"
2. Select farmers using checkboxes
3. Choose "Reset password for selected farmers" action
4. Click "Go"

**Method 2: From Detail View**
1. Open a farmer's profile
2. Click "Reset Password" button
3. Set new password in Django's password form

#### 4. View Analytics

1. Go to "Interactions" in admin
2. Filter by date, farmer, or interaction type
3. Export data for analysis

#### 5. Manage Content

1. Edit knowledge base content
2. Update weather data
3. Monitor conversations

---

## 🔌 API Documentation

### Authentication

All API endpoints require authentication via Django session cookies.

### Endpoints

#### Send Text Message

```http
POST /api/send-message/
Content-Type: application/json

{
  "conversation_id": 1,
  "message": "What is the best time to plant wheat?"
}
```

**Response**:
```json
{
  "success": true,
  "farmer_message": {
    "id": 123,
    "content": "What is the best time to plant wheat?",
    "created_at": "2024-01-15T10:30:00Z"
  },
  "ai_message": {
    "id": 124,
    "content": "The best time to plant wheat in India is...",
    "created_at": "2024-01-15T10:30:05Z"
  }
}
```

#### Upload Voice Message

```http
POST /api/upload-voice/
Content-Type: multipart/form-data

conversation_id: 1
audio: <audio-file.ogg>
```

**Response**:
```json
{
  "success": true,
  "transcript": "मेरी गेहूं की फसल में पीले पत्ते हैं",
  "response": "Yellow leaves in wheat can indicate...",
  "audio_url": "https://s3.amazonaws.com/..."
}
```

#### Upload Image

```http
POST /api/upload-image/
Content-Type: multipart/form-data

conversation_id: 1
image: <image-file.jpg>
description: "Cotton leaf problem"
```

**Response**:
```json
{
  "success": true,
  "image_url": "https://s3.amazonaws.com/...",
  "response": "Based on the image, this appears to be..."
}
```

#### Transcribe Voice Input (Registration)

```http
POST /api/transcribe-voice/
Content-Type: multipart/form-data

audio: <audio-file.ogg>
language: hi
field_name: full_name
```

**Response**:
```json
{
  "success": true,
  "transcript": "राजेश कुमार",
  "field_name": "full_name"
}
```

### Error Responses

```json
{
  "error": "Error message description"
}
```

HTTP Status Codes:
- `200`: Success
- `400`: Bad Request (missing parameters)
- `401`: Unauthorized (not logged in)
- `404`: Not Found
- `500`: Server Error

---

## ☁️ AWS Integration

### Bedrock (AI Responses)

**Service**: `aws_services/bedrock.py`

**Purpose**: Generate intelligent agricultural advice using Claude 3 Haiku

**How it works**:
1. Receives farmer's query and context (location, crops, farm size)
2. Builds prompt with system instructions and user query
3. Calls AWS Bedrock API with Claude 3 Haiku model
4. Returns AI-generated agricultural advice

**Configuration**:
```python
BEDROCK_MODEL_ID = 'anthropic.claude-3-haiku-20240307-v1:0'
```

**Cost**: ~$0.00025 per request

See [BEDROCK-WORKFLOW-GUIDE.md](BEDROCK-WORKFLOW-GUIDE.md) for detailed workflow.

### Transcribe (Voice-to-Text)

**Service**: `aws_services/transcribe.py`

**Purpose**: Convert farmer's voice recordings to text

**Supported Languages**:
- Hindi (hi-IN)
- English (en-IN)
- Telugu (te-IN)
- Tamil (ta-IN)
- Marathi (mr-IN)
- Punjabi (pa-IN)
- Kannada (kn-IN)
- Bengali (bn-IN)

**How it works**:
1. Audio file uploaded to S3
2. Transcribe job started with language code
3. Transcription retrieved and returned as text

**Cost**: ~$0.024 per minute of audio

### Polly (Text-to-Speech)

**Service**: `aws_services/polly.py`

**Purpose**: Convert AI responses to speech in farmer's language

**Voice Options**:
- Hindi: Aditi (Neural)
- English: Kajal (Neural)
- Telugu: Mock (standard voices available)
- Tamil: Mock (standard voices available)

**How it works**:
1. AI response text sent to Polly
2. Neural voice synthesizes speech
3. Audio file saved to S3
4. URL returned for playback

**Cost**: ~$0.016 per million characters

### S3 (File Storage)

**Service**: `aws_services/s3.py`

**Purpose**: Store audio recordings, images, and knowledge base content

**Bucket Structure**:
```
krishi-mitra-media/
├── audio/
│   ├── registration/
│   └── <phone-number>/
├── images/
│   └── <phone-number>/
└── knowledge/
    └── knowledge-base.json
```

**Cost**: ~$0.023 per GB per month

### Weather Service

**Service**: `aws_services/weather.py`

**Purpose**: Provide weather data and agricultural advisories

**Current Mode**: Mock data (can integrate with real weather API)

**Features**:
- Current conditions
- 7-day forecast
- Agricultural alerts
- Location-based data

---

## 🌐 Multi-Language Support

### Supported Languages

| Language | Code | Dashboard | Voice Input | Voice Output |
|----------|------|-----------|-------------|--------------|
| Hindi | hi | ✅ | ✅ | ✅ |
| English | en | ✅ | ✅ | ✅ |
| Telugu | te | ✅ | ✅ | ⚠️ Mock |
| Tamil | ta | ✅ | ✅ | ⚠️ Mock |
| Marathi | mr | ✅ | ✅ | ⚠️ Mock |
| Punjabi | pa | ✅ | ✅ | ⚠️ Mock |
| Kannada | kn | ✅ | ✅ | ⚠️ Mock |
| Bengali | bn | ✅ | ✅ | ⚠️ Mock |
| Gujarati | gu | ✅ | ⚠️ Mock | ⚠️ Mock |

### How It Works

1. **Registration**: Farmer selects preferred language first
2. **Dashboard**: All UI elements translated to selected language
3. **Voice Input**: Transcribe uses language-specific models
4. **Voice Output**: Polly synthesizes speech in selected language
5. **AI Responses**: Claude responds in context-appropriate language

### Translation System

**File**: `farmers/translations.py`

**Structure**:
```python
TRANSLATIONS = {
    'hi': {
        'welcome': 'स्वागत है',
        'dashboard': 'डैशबोर्ड',
        # ... more translations
    },
    'en': {
        'welcome': 'Welcome',
        'dashboard': 'Dashboard',
        # ... more translations
    }
}
```

**Usage in Templates**:
```html
<h1>{{ trans.welcome }}</h1>
<a href="/dashboard/">{{ trans.dashboard }}</a>
```

See [MULTI-LANGUAGE-GUIDE.md](MULTI-LANGUAGE-GUIDE.md) for details.

---

## 🚢 Deployment

### Development Server

```bash
python manage.py runserver
# Access at http://127.0.0.1:8000/
```

### Production Deployment

#### Option 1: AWS Elastic Beanstalk

1. **Install EB CLI**
   ```bash
   pip install awsebcli
   ```

2. **Initialize EB**
   ```bash
   eb init -p python-3.11 krishi-mitra
   ```

3. **Create Environment**
   ```bash
   eb create krishi-mitra-prod
   ```

4. **Deploy**
   ```bash
   eb deploy
   ```

5. **Configure Environment Variables**
   ```bash
   eb setenv SECRET_KEY=your-secret-key
   eb setenv AWS_ACCESS_KEY_ID=your-key
   eb setenv AWS_SECRET_ACCESS_KEY=your-secret
   ```

#### Option 2: AWS EC2

1. **Launch EC2 Instance**
   - AMI: Ubuntu 22.04 LTS
   - Instance Type: t3.small or larger
   - Security Group: Allow ports 80, 443, 22

2. **Connect and Setup**
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-ip
   
   # Update system
   sudo apt update && sudo apt upgrade -y
   
   # Install Python and dependencies
   sudo apt install python3-pip python3-venv nginx -y
   
   # Clone repository
   git clone <your-repo-url>
   cd poc-django
   
   # Create virtual environment
   python3 -m venv venv
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   pip install gunicorn
   ```

3. **Configure Environment**
   ```bash
   cp .env.example .env
   nano .env  # Add your credentials
   ```

4. **Collect Static Files**
   ```bash
   python manage.py collectstatic --noinput
   ```

5. **Setup Gunicorn Service**
   ```bash
   sudo nano /etc/systemd/system/gunicorn.service
   ```
   
   Add:
   ```ini
   [Unit]
   Description=Gunicorn daemon for Krishi Mitra
   After=network.target
   
   [Service]
   User=ubuntu
   Group=www-data
   WorkingDirectory=/home/ubuntu/poc-django
   ExecStart=/home/ubuntu/poc-django/venv/bin/gunicorn \
             --workers 3 \
             --bind unix:/home/ubuntu/poc-django/gunicorn.sock \
             krishi_mitra.wsgi:application
   
   [Install]
   WantedBy=multi-user.target
   ```

6. **Configure Nginx**
   ```bash
   sudo nano /etc/nginx/sites-available/krishi-mitra
   ```
   
   Add:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
   
       location = /favicon.ico { access_log off; log_not_found off; }
       
       location /static/ {
           root /home/ubuntu/poc-django;
       }
       
       location /media/ {
           root /home/ubuntu/poc-django;
       }
   
       location / {
           include proxy_params;
           proxy_pass http://unix:/home/ubuntu/poc-django/gunicorn.sock;
       }
   }
   ```

7. **Enable and Start Services**
   ```bash
   sudo ln -s /etc/nginx/sites-available/krishi-mitra /etc/nginx/sites-enabled
   sudo systemctl start gunicorn
   sudo systemctl enable gunicorn
   sudo systemctl restart nginx
   ```

#### Option 3: Docker

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.11-slim
   
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   
   COPY . .
   
   RUN python manage.py collectstatic --noinput
   
   EXPOSE 8000
   
   CMD ["gunicorn", "krishi_mitra.wsgi:application", "--bind", "0.0.0.0:8000"]
   ```

2. **Build and Run**
   ```bash
   docker build -t krishi-mitra .
   docker run -p 8000:8000 --env-file .env krishi-mitra
   ```

3. **Docker Compose** (with PostgreSQL)
   ```yaml
   version: '3.8'
   
   services:
     web:
       build: .
       ports:
         - "8000:8000"
       env_file:
         - .env
       depends_on:
         - db
     
     db:
       image: postgres:15
       environment:
         POSTGRES_DB: krishi_mitra
         POSTGRES_USER: postgres
         POSTGRES_PASSWORD: your-password
       volumes:
         - postgres_data:/var/lib/postgresql/data
   
   volumes:
     postgres_data:
   ```

### Production Checklist

- [ ] Set `DEBUG=False` in `.env`
- [ ] Use strong `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use PostgreSQL instead of SQLite
- [ ] Enable HTTPS (SSL certificate)
- [ ] Set up AWS IAM roles (instead of access keys)
- [ ] Configure CloudWatch logging
- [ ] Set up database backups
- [ ] Enable AWS CloudFront CDN
- [ ] Configure rate limiting
- [ ] Set up monitoring and alerts
- [ ] Enable CORS properly
- [ ] Configure email backend
- [ ] Set up error tracking (Sentry)

---

## 💰 Cost Estimation

### Development (Local)

| Service | Cost |
|---------|------|
| Django | Free |
| SQLite | Free |
| AWS (Mock Mode) | Free |
| **Total** | **$0/month** |

### Production (1,000 farmers, 10 queries/month each)

| Service | Usage | Cost/Month |
|---------|-------|------------|
| **Compute** |
| EC2 t3.small | 730 hours | $15 |
| **Database** |
| RDS PostgreSQL (db.t3.micro) | 730 hours | $15 |
| **Storage** |
| S3 Storage | 10 GB | $0.23 |
| S3 Requests | 50,000 | $0.02 |
| **AI Services** |
| Bedrock (Claude 3 Haiku) | 10,000 requests | $2.50 |
| Transcribe | 100 minutes | $2.40 |
| Polly (Neural) | 500,000 chars | $0.80 |
| **Networking** |
| Data Transfer | 50 GB | $4.50 |
| Load Balancer | 730 hours | $16 |
| **Total** | | **~$56/month** |

### Scaling (10,000 farmers, 10 queries/month each)

| Service | Cost/Month |
|---------|------------|
| EC2 t3.medium (2x) | $60 |
| RDS PostgreSQL (db.t3.small) | $30 |
| S3 | $2.50 |
| Bedrock | $25 |
| Transcribe | $24 |
| Polly | $8 |
| Data Transfer | $45 |
| Load Balancer | $16 |
| **Total** | **~$210/month** |

### Cost Optimization Tips

1. **Use Reserved Instances**: Save 30-40% on EC2/RDS
2. **Enable S3 Lifecycle Policies**: Move old files to Glacier
3. **Use CloudFront CDN**: Reduce data transfer costs
4. **Implement Caching**: Reduce Bedrock API calls
5. **Use Spot Instances**: For non-critical workloads
6. **Monitor Usage**: Set up billing alerts

---

## 🔧 Troubleshooting

### Common Issues

#### 1. Database Errors

**Problem**: `django.db.utils.OperationalError: no such table`

**Solution**:
```bash
python manage.py migrate
python manage.py migrate --run-syncdb
```

#### 2. Static Files Not Loading

**Problem**: CSS/JS files return 404

**Solution**:
```bash
python manage.py collectstatic --noinput
# Make sure STATIC_ROOT is configured in settings.py
```

#### 3. AWS Connection Errors

**Problem**: `botocore.exceptions.NoCredentialsError`

**Solution**:
- Check `.env` file has correct AWS credentials
- Verify IAM user has required permissions
- Test with: `aws s3 ls` (should list buckets)

#### 4. Bedrock "Model Not Found"

**Problem**: `ValidationException: The provided model identifier is invalid`

**Solution**:
- Go to AWS Console → Bedrock → Model Access
- Request access to Claude 3 Haiku
- Wait for approval (usually instant)
- Verify model ID in `.env` matches available models

#### 5. Admin Login Redirect Loop

**Problem**: Admin user can't access dashboard

**Solution**:
- This is expected behavior
- Admin users without FarmerProfile are redirected to `/admin/`
- Create a FarmerProfile for admin if needed, or use separate accounts

#### 6. Farmer Login Not Working

**Problem**: "Please enter a correct username and password"

**Solution**:
```bash
# Reset password using script
python reset_password.py

# Or create new user
python manage.py createsuperuser
```

#### 7. Voice Recording Not Working

**Problem**: Microphone button doesn't work

**Solution**:
- Check browser permissions (allow microphone access)
- Use HTTPS in production (required for getUserMedia API)
- Test in Chrome/Firefox (best support)

#### 8. Image Upload Fails

**Problem**: `413 Request Entity Too Large`

**Solution**:
- Check `DATA_UPLOAD_MAX_MEMORY_SIZE` in settings.py
- Configure nginx `client_max_body_size`
- Compress images before upload

### Debug Mode

Enable detailed error messages:

```python
# settings.py
DEBUG = True
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}
```

### Getting Help

1. **Check Documentation**:
   - [QUICKSTART.md](QUICKSTART.md)
   - [BEDROCK-WORKFLOW-GUIDE.md](BEDROCK-WORKFLOW-GUIDE.md)
   - [MULTI-LANGUAGE-GUIDE.md](MULTI-LANGUAGE-GUIDE.md)

2. **Check Logs**:
   ```bash
   # Django logs
   python manage.py runserver --verbosity 3
   
   # Gunicorn logs
   sudo journalctl -u gunicorn
   
   # Nginx logs
   sudo tail -f /var/log/nginx/error.log
   ```

3. **Test AWS Services**:
   ```bash
   # Test AWS credentials
   aws sts get-caller-identity
   
   # Test S3 access
   aws s3 ls
   
   # Test Bedrock access
   aws bedrock list-foundation-models --region ap-south-1
   ```

---

## 📱 WhatsApp API Integration

### Overview

AI Krishi Mitra can be integrated with WhatsApp Business API to provide farmers with a familiar messaging interface. This allows farmers to interact with the AI advisor directly through WhatsApp without needing to access the web interface.

### Architecture

```
WhatsApp User → WhatsApp Business API → Webhook Endpoint → Django Backend → AWS Services
                                                ↓
                                         Process Message
                                                ↓
                                    ┌───────────┴───────────┐
                                    │                       │
                              Text Query              Voice/Image
                                    │                       │
                                    ▼                       ▼
                            Bedrock (Claude)        S3 + Transcribe/Rekognition
                                    │                       │
                                    └───────────┬───────────┘
                                                ▼
                                        AI Response
                                                ▼
                                    WhatsApp Business API
                                                ▼
                                          WhatsApp User
```

### Supported WhatsApp Providers

#### 1. Meta WhatsApp Business API (Official)

**Best for**: Large scale deployments, official support

**Setup Steps**:

1. **Create Meta Business Account**
   - Go to https://business.facebook.com/
   - Create a business account
   - Verify your business

2. **Set up WhatsApp Business API**
   - Go to Meta for Developers: https://developers.facebook.com/
   - Create a new app
   - Add WhatsApp product
   - Get phone number ID and access token

3. **Configure Webhook**
   - Set webhook URL: `https://your-domain.com/api/whatsapp/webhook/`
   - Subscribe to messages, message_status events
   - Verify webhook token

**Pricing**:
- Free tier: 1,000 conversations/month
- Business-initiated: $0.0042 per conversation (India)
- User-initiated: Free for 24 hours

#### 2. Twilio WhatsApp API

**Best for**: Quick setup, developer-friendly

**Setup Steps**:

1. **Create Twilio Account**
   - Sign up at https://www.twilio.com/
   - Get account SID and auth token

2. **Enable WhatsApp Sandbox** (Development)
   - Go to Twilio Console → Messaging → Try it out → WhatsApp
   - Join sandbox by sending code to Twilio number

3. **Configure Webhook**
   - Set webhook URL: `https://your-domain.com/api/whatsapp/twilio/webhook/`
   - Method: POST

**Pricing**:
- $0.005 per message (India)
- No monthly fees

#### 3. 360Dialog WhatsApp API

**Best for**: European/Global deployments

**Setup Steps**:

1. **Create 360Dialog Account**
   - Sign up at https://www.360dialog.com/
   - Complete business verification

2. **Get API Credentials**
   - Obtain API key and phone number ID

3. **Configure Webhook**
   - Set webhook URL in 360Dialog dashboard

**Pricing**:
- €0.0042 per conversation (India)
- Monthly platform fee applies

### Implementation

#### 1. Install Dependencies

Add to `requirements.txt`:
```txt
# WhatsApp Integration
twilio==8.11.0
requests==2.31.0
python-whatsapp-bot==0.0.1
```

Install:
```bash
pip install twilio requests
```

#### 2. Create WhatsApp Service

Create `aws_services/whatsapp.py`:

```python
"""
WhatsApp Business API integration
"""
import requests
import logging
from django.conf import settings
from twilio.rest import Client

logger = logging.getLogger(__name__)


class WhatsAppService:
    """WhatsApp Business API integration"""
    
    def __init__(self, provider='meta'):
        """
        Initialize WhatsApp service
        
        Args:
            provider: 'meta', 'twilio', or '360dialog'
        """
        self.provider = provider
        
        if provider == 'meta':
            self.access_token = settings.WHATSAPP_ACCESS_TOKEN
            self.phone_number_id = settings.WHATSAPP_PHONE_NUMBER_ID
            self.api_url = f"https://graph.facebook.com/v18.0/{self.phone_number_id}/messages"
        
        elif provider == 'twilio':
            self.client = Client(
                settings.TWILIO_ACCOUNT_SID,
                settings.TWILIO_AUTH_TOKEN
            )
            self.from_number = settings.TWILIO_WHATSAPP_NUMBER
        
        elif provider == '360dialog':
            self.api_key = settings.DIALOG_360_API_KEY
            self.api_url = "https://waba.360dialog.io/v1/messages"
    
    def send_text_message(self, to_number, message):
        """Send text message via WhatsApp"""
        try:
            if self.provider == 'meta':
                return self._send_meta_text(to_number, message)
            elif self.provider == 'twilio':
                return self._send_twilio_text(to_number, message)
            elif self.provider == '360dialog':
                return self._send_360dialog_text(to_number, message)
        except Exception as e:
            logger.error(f"WhatsApp send error: {str(e)}")
            return None
    
    def _send_meta_text(self, to_number, message):
        """Send via Meta WhatsApp Business API"""
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        data = {
            "messaging_product": "whatsapp",
            "to": to_number,
            "type": "text",
            "text": {"body": message}
        }
        
        response = requests.post(self.api_url, headers=headers, json=data)
        return response.json()
    
    def _send_twilio_text(self, to_number, message):
        """Send via Twilio WhatsApp API"""
        message = self.client.messages.create(
            body=message,
            from_=f'whatsapp:{self.from_number}',
            to=f'whatsapp:{to_number}'
        )
        return message.sid
    
    def _send_360dialog_text(self, to_number, message):
        """Send via 360Dialog WhatsApp API"""
        headers = {
            "D360-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }
        
        data = {
            "to": to_number,
            "type": "text",
            "text": {"body": message}
        }
        
        response = requests.post(self.api_url, headers=headers, json=data)
        return response.json()
    
    def send_audio_message(self, to_number, audio_url):
        """Send audio message via WhatsApp"""
        try:
            if self.provider == 'meta':
                return self._send_meta_audio(to_number, audio_url)
            elif self.provider == 'twilio':
                return self._send_twilio_audio(to_number, audio_url)
        except Exception as e:
            logger.error(f"WhatsApp audio send error: {str(e)}")
            return None
    
    def _send_meta_audio(self, to_number, audio_url):
        """Send audio via Meta WhatsApp Business API"""
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        data = {
            "messaging_product": "whatsapp",
            "to": to_number,
            "type": "audio",
            "audio": {"link": audio_url}
        }
        
        response = requests.post(self.api_url, headers=headers, json=data)
        return response.json()
    
    def _send_twilio_audio(self, to_number, audio_url):
        """Send audio via Twilio WhatsApp API"""
        message = self.client.messages.create(
            media_url=[audio_url],
            from_=f'whatsapp:{self.from_number}',
            to=f'whatsapp:{to_number}'
        )
        return message.sid
    
    def send_image_message(self, to_number, image_url, caption=""):
        """Send image message via WhatsApp"""
        try:
            if self.provider == 'meta':
                return self._send_meta_image(to_number, image_url, caption)
            elif self.provider == 'twilio':
                return self._send_twilio_image(to_number, image_url, caption)
        except Exception as e:
            logger.error(f"WhatsApp image send error: {str(e)}")
            return None
    
    def _send_meta_image(self, to_number, image_url, caption):
        """Send image via Meta WhatsApp Business API"""
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        data = {
            "messaging_product": "whatsapp",
            "to": to_number,
            "type": "image",
            "image": {
                "link": image_url,
                "caption": caption
            }
        }
        
        response = requests.post(self.api_url, headers=headers, json=data)
        return response.json()
    
    def _send_twilio_image(self, to_number, image_url, caption):
        """Send image via Twilio WhatsApp API"""
        message = self.client.messages.create(
            body=caption,
            media_url=[image_url],
            from_=f'whatsapp:{self.from_number}',
            to=f'whatsapp:{to_number}'
        )
        return message.sid
    
    def send_template_message(self, to_number, template_name, language_code='en'):
        """Send template message (for business-initiated conversations)"""
        if self.provider != 'meta':
            logger.warning("Template messages only supported with Meta API")
            return None
        
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        data = {
            "messaging_product": "whatsapp",
            "to": to_number,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {"code": language_code}
            }
        }
        
        response = requests.post(self.api_url, headers=headers, json=data)
        return response.json()
```

#### 3. Create Webhook Views

Add to `farmers/views.py`:

```python
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

from aws_services.whatsapp import WhatsAppService
from aws_services.bedrock import BedrockService

whatsapp_service = WhatsAppService(provider='meta')  # or 'twilio'
bedrock_service = BedrockService()


@csrf_exempt
@require_http_methods(["GET", "POST"])
def whatsapp_webhook(request):
    """
    Webhook for Meta WhatsApp Business API
    """
    if request.method == 'GET':
        # Webhook verification
        mode = request.GET.get('hub.mode')
        token = request.GET.get('hub.verify_token')
        challenge = request.GET.get('hub.challenge')
        
        if mode == 'subscribe' and token == settings.WHATSAPP_VERIFY_TOKEN:
            return HttpResponse(challenge)
        return HttpResponse('Verification failed', status=403)
    
    elif request.method == 'POST':
        # Handle incoming messages
        try:
            data = json.loads(request.body)
            
            # Extract message details
            entry = data.get('entry', [])[0]
            changes = entry.get('changes', [])[0]
            value = changes.get('value', {})
            messages = value.get('messages', [])
            
            if not messages:
                return HttpResponse('No messages', status=200)
            
            message = messages[0]
            from_number = message.get('from')
            message_type = message.get('type')
            
            # Get or create farmer profile
            farmer_profile = get_or_create_farmer_from_whatsapp(from_number)
            
            # Process based on message type
            if message_type == 'text':
                text = message.get('text', {}).get('body', '')
                response = process_whatsapp_text(farmer_profile, text)
                whatsapp_service.send_text_message(from_number, response)
            
            elif message_type == 'audio':
                audio_id = message.get('audio', {}).get('id')
                response = process_whatsapp_audio(farmer_profile, audio_id)
                whatsapp_service.send_text_message(from_number, response)
            
            elif message_type == 'image':
                image_id = message.get('image', {}).get('id')
                caption = message.get('image', {}).get('caption', '')
                response = process_whatsapp_image(farmer_profile, image_id, caption)
                whatsapp_service.send_text_message(from_number, response)
            
            return HttpResponse('Message processed', status=200)
            
        except Exception as e:
            logger.error(f"WhatsApp webhook error: {str(e)}")
            return HttpResponse('Error', status=500)


@csrf_exempt
@require_http_methods(["POST"])
def twilio_whatsapp_webhook(request):
    """
    Webhook for Twilio WhatsApp API
    """
    try:
        from_number = request.POST.get('From', '').replace('whatsapp:', '')
        body = request.POST.get('Body', '')
        media_url = request.POST.get('MediaUrl0', '')
        
        # Get or create farmer profile
        farmer_profile = get_or_create_farmer_from_whatsapp(from_number)
        
        # Process message
        if media_url:
            # Handle media (image/audio)
            response = process_whatsapp_media(farmer_profile, media_url, body)
        else:
            # Handle text
            response = process_whatsapp_text(farmer_profile, body)
        
        # Send response via Twilio
        whatsapp_service.send_text_message(from_number, response)
        
        return HttpResponse('Message processed', status=200)
        
    except Exception as e:
        logger.error(f"Twilio webhook error: {str(e)}")
        return HttpResponse('Error', status=500)


def get_or_create_farmer_from_whatsapp(phone_number):
    """Get or create farmer profile from WhatsApp number"""
    try:
        farmer_profile = FarmerProfile.objects.get(phone_number=phone_number)
    except FarmerProfile.DoesNotExist:
        # Create new user and profile
        username = f"whatsapp_{phone_number}"
        user = User.objects.create_user(username=username)
        farmer_profile = FarmerProfile.objects.create(
            user=user,
            phone_number=phone_number,
            language='hi',  # Default to Hindi
            approval_status='approved'  # Auto-approve WhatsApp users
        )
    return farmer_profile


def process_whatsapp_text(farmer_profile, text):
    """Process text message from WhatsApp"""
    # Build context
    context = build_farmer_context(farmer_profile)
    
    # Generate AI response
    ai_response = bedrock_service.generate_response(text, context)
    
    # Log interaction
    Interaction.objects.create(
        farmer=farmer_profile,
        interaction_type='whatsapp_text',
        query=text,
        response=ai_response
    )
    
    return ai_response


def process_whatsapp_audio(farmer_profile, audio_id):
    """Process audio message from WhatsApp"""
    # Download audio from WhatsApp
    audio_url = download_whatsapp_media(audio_id)
    
    # Transcribe
    transcript = transcribe_service.transcribe(audio_url, farmer_profile.language)
    
    # Generate AI response
    context = build_farmer_context(farmer_profile)
    ai_response = bedrock_service.generate_response(transcript, context)
    
    # Log interaction
    Interaction.objects.create(
        farmer=farmer_profile,
        interaction_type='whatsapp_voice',
        query=transcript,
        response=ai_response
    )
    
    return f"आपने कहा: {transcript}\n\n{ai_response}"


def process_whatsapp_image(farmer_profile, image_id, caption):
    """Process image message from WhatsApp"""
    # Download image from WhatsApp
    image_url = download_whatsapp_media(image_id)
    
    # Generate AI response (with image context)
    prompt = f"Farmer uploaded an image. Caption: {caption}. Provide agricultural advice."
    context = build_farmer_context(farmer_profile)
    ai_response = bedrock_service.generate_response(prompt, context)
    
    # Log interaction
    Interaction.objects.create(
        farmer=farmer_profile,
        interaction_type='whatsapp_image',
        query=f"Image: {caption}",
        response=ai_response
    )
    
    return ai_response


def download_whatsapp_media(media_id):
    """Download media file from WhatsApp"""
    # Implementation depends on provider
    # For Meta: Use Graph API to get media URL
    # For Twilio: Media URL is provided directly
    pass
```

#### 4. Add URL Routes

Add to `farmers/urls.py`:

```python
urlpatterns = [
    # ... existing patterns ...
    
    # WhatsApp webhooks
    path('api/whatsapp/webhook/', views.whatsapp_webhook, name='whatsapp_webhook'),
    path('api/whatsapp/twilio/webhook/', views.twilio_whatsapp_webhook, name='twilio_whatsapp_webhook'),
]
```

#### 5. Configure Environment Variables

Add to `.env`:

```bash
# WhatsApp Configuration
WHATSAPP_PROVIDER=meta  # or 'twilio' or '360dialog'

# Meta WhatsApp Business API
WHATSAPP_ACCESS_TOKEN=your-meta-access-token
WHATSAPP_PHONE_NUMBER_ID=your-phone-number-id
WHATSAPP_VERIFY_TOKEN=your-verify-token

# Twilio WhatsApp API
TWILIO_ACCOUNT_SID=your-twilio-account-sid
TWILIO_AUTH_TOKEN=your-twilio-auth-token
TWILIO_WHATSAPP_NUMBER=+14155238886

# 360Dialog WhatsApp API
DIALOG_360_API_KEY=your-360dialog-api-key
```

Add to `settings.py`:

```python
# WhatsApp Settings
WHATSAPP_PROVIDER = os.getenv('WHATSAPP_PROVIDER', 'meta')
WHATSAPP_ACCESS_TOKEN = os.getenv('WHATSAPP_ACCESS_TOKEN')
WHATSAPP_PHONE_NUMBER_ID = os.getenv('WHATSAPP_PHONE_NUMBER_ID')
WHATSAPP_VERIFY_TOKEN = os.getenv('WHATSAPP_VERIFY_TOKEN', 'krishi-mitra-verify')

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER')

DIALOG_360_API_KEY = os.getenv('DIALOG_360_API_KEY')
```

### Features Supported via WhatsApp

✅ **Text Queries**
- Farmers send text questions
- AI responds with agricultural advice
- Context-aware based on farmer profile

✅ **Voice Messages**
- Farmers send voice notes
- Automatic transcription to text
- AI responds in text (or audio if configured)

✅ **Image Analysis**
- Farmers send crop/pest photos
- AI analyzes and provides diagnosis
- Treatment recommendations

✅ **Multi-Language**
- Automatic language detection
- Responses in farmer's preferred language
- Support for 8+ Indian languages

✅ **Template Messages**
- Weather alerts
- Crop advisories
- Market price updates
- Scheduled reminders

### Usage Flow

1. **Farmer Sends Message**
   ```
   Farmer: "मेरी गेहूं की फसल में पीले पत्ते हैं"
   ```

2. **System Processes**
   - Webhook receives message
   - Identifies/creates farmer profile
   - Builds context (location, crops, etc.)
   - Sends to Bedrock (Claude)

3. **AI Responds**
   ```
   AI: "गेहूं में पीले पत्ते नाइट्रोजन की कमी या जलभराव का संकेत हो सकते हैं। 
   
   उपाय:
   1. मिट्टी की नमी जांचें
   2. यूरिया 50 किग्रा/हेक्टेयर डालें
   3. जिंक सल्फेट का छिड़काव करें
   
   पंजाब की जलवायु में गेहूं को पानी चाहिए लेकिन जलभराव नहीं।"
   ```

4. **Interaction Logged**
   - Query and response saved
   - Analytics updated
   - Available in web dashboard

### Testing WhatsApp Integration

#### Development (Twilio Sandbox)

1. **Join Sandbox**
   - Send "join <your-code>" to Twilio WhatsApp number
   - Example: "join happy-elephant"

2. **Test Messages**
   ```
   You: "What fertilizer for wheat?"
   Bot: "For wheat cultivation, nitrogen-based fertilizers..."
   ```

3. **Test Voice**
   - Send voice note in Hindi
   - Bot transcribes and responds

4. **Test Images**
   - Send crop photo
   - Bot analyzes and advises

#### Production (Meta WhatsApp Business)

1. **Get Approved**
   - Complete business verification
   - Get phone number approved
   - Create message templates

2. **Deploy Webhook**
   - Deploy Django app with HTTPS
   - Configure webhook URL in Meta dashboard
   - Verify webhook connection

3. **Go Live**
   - Share WhatsApp number with farmers
   - Monitor conversations in admin panel
   - Track analytics and usage

### WhatsApp vs Web Interface

| Feature | WhatsApp | Web Interface |
|---------|----------|---------------|
| **Accessibility** | High (familiar app) | Medium (requires browser) |
| **Internet** | Low bandwidth | Higher bandwidth |
| **Registration** | Auto-created | Manual with approval |
| **Rich UI** | Limited | Full dashboard |
| **Voice** | Native support | Web Audio API |
| **Images** | Native support | Upload form |
| **Analytics** | Basic | Comprehensive |
| **Admin Control** | Limited | Full admin panel |
| **Cost** | Per message | Hosting only |

### Best Practices

1. **Response Time**
   - Keep responses under 1600 characters
   - Split long responses into multiple messages
   - Use bullet points for clarity

2. **Language Detection**
   - Auto-detect language from first message
   - Store preference in farmer profile
   - Respond in same language

3. **Error Handling**
   - Graceful fallbacks for API failures
   - Retry logic for failed messages
   - User-friendly error messages

4. **Rate Limiting**
   - Implement per-user rate limits
   - Prevent spam and abuse
   - Monitor usage patterns

5. **Privacy & Security**
   - Encrypt sensitive data
   - Comply with WhatsApp policies
   - Respect user privacy

6. **Template Messages**
   - Pre-approve templates with Meta
   - Use for proactive notifications
   - Weather alerts, price updates

### Cost Comparison

**1,000 farmers, 10 messages/month each = 10,000 messages**

| Provider | Cost/Month | Notes |
|----------|------------|-------|
| **Meta WhatsApp** | $42 | User-initiated free for 24h |
| **Twilio** | $50 | Simple pricing, no free tier |
| **360Dialog** | €42 (~$45) | European pricing |
| **Web Interface** | $56 | Hosting + AWS services |

**Recommendation**: Use WhatsApp for farmer-facing interactions, web interface for admin/analytics.

### Monitoring & Analytics

Track WhatsApp metrics in Django admin:

```python
# farmers/admin.py
class InteractionAdmin(admin.ModelAdmin):
    list_display = ['farmer', 'interaction_type', 'created_at']
    list_filter = ['interaction_type', 'created_at']
    search_fields = ['farmer__phone_number', 'query']
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Filter WhatsApp interactions
        return qs.filter(interaction_type__startswith='whatsapp_')
```

### Troubleshooting

**Webhook not receiving messages**:
- Check webhook URL is HTTPS
- Verify webhook token matches
- Check firewall/security groups
- Test with webhook tester tools

**Messages not sending**:
- Verify API credentials
- Check phone number format (+91...)
- Ensure 24-hour window for user-initiated
- Use templates for business-initiated

**Audio/Image not working**:
- Check media download permissions
- Verify S3 upload configuration
- Test media URL accessibility
- Check file size limits

### Resources

- **Meta WhatsApp Business API**: https://developers.facebook.com/docs/whatsapp
- **Twilio WhatsApp API**: https://www.twilio.com/docs/whatsapp
- **360Dialog**: https://docs.360dialog.com/
- **WhatsApp Business Policy**: https://www.whatsapp.com/legal/business-policy

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Reporting Issues

1. Check existing issues first
2. Provide detailed description
3. Include error messages and logs
4. Specify your environment (OS, Python version, etc.)

### Submitting Pull Requests

1. Fork the repository
2. Create a feature branch
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes
4. Write/update tests
5. Update documentation
6. Commit with clear messages
   ```bash
   git commit -m "Add: feature description"
   ```
7. Push to your fork
   ```bash
   git push origin feature/your-feature-name
   ```
8. Create Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Write docstrings for functions
- Add comments for complex logic
- Keep functions small and focused
- Write tests for new features
- Update README for new features

### Code Style

```bash
# Format code
black .

# Check style
flake8 .

# Run tests
python manage.py test
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support & Contact

### Documentation

- **Quick Start**: [QUICKSTART.md](QUICKSTART.md)
- **Registration Guide**: [REGISTRATION-GUIDE.md](REGISTRATION-GUIDE.md)
- **Multi-Language**: [MULTI-LANGUAGE-GUIDE.md](MULTI-LANGUAGE-GUIDE.md)
- **Login Guide**: [LOGIN-GUIDE.md](LOGIN-GUIDE.md)
- **Password Reset**: [PASSWORD-RESET-GUIDE.md](PASSWORD-RESET-GUIDE.md)
- **Bedrock Workflow**: [BEDROCK-WORKFLOW-GUIDE.md](BEDROCK-WORKFLOW-GUIDE.md)
- **Access Info**: [ACCESS-INFO.md](ACCESS-INFO.md)

### Resources

- **Django Documentation**: https://docs.djangoproject.com/
- **AWS Bedrock**: https://aws.amazon.com/bedrock/
- **AWS Boto3**: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
- **Bootstrap 5**: https://getbootstrap.com/docs/5.0/

### Project Links

- **Repository**: <your-repo-url>
- **Issues**: <your-repo-url>/issues
- **Wiki**: <your-repo-url>/wiki

---

## 🙏 Acknowledgments

- **AWS AI for Bharat Hackathon** for the opportunity
- **Django Community** for the excellent framework
- **AWS** for AI services (Bedrock, Transcribe, Polly)
- **Bootstrap** for UI components
- **Indian Farmers** for inspiration and feedback

---

## 📊 Project Status

- ✅ **Core Features**: Complete
- ✅ **AWS Integration**: Functional (mock + real modes)
- ✅ **Multi-Language**: 9 languages supported
- ✅ **Admin Panel**: Full management capabilities
- ✅ **Documentation**: Comprehensive guides
- 🚧 **Mobile App**: Planned
- 🚧 **Advanced Analytics**: In progress
- 🚧 **Community Forum**: Planned

---

<div align="center">

**Made with ❤️ for Indian Farmers**

[⬆ Back to Top](#-ai-krishi-mitra---agricultural-ai-assistant)

</div>
