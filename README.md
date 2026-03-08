# 🌾 AI Krishi Mitra - Agricultural AI Assistant Platform

> A comprehensive agricultural advisory platform powered by AWS AI services, designed to help Indian farmers with intelligent crop management, pest control, weather insights, and farming best practices.

[![Django](https://img.shields.io/badge/Django-5.0-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![AWS](https://img.shields.io/badge/AWS-Bedrock%20%7C%20S3%20%7C%20Polly%20%7C%20Transcribe-orange.svg)](https://aws.amazon.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Quick Start](#quick-start)
- [Available Implementations](#available-implementations)
- [Documentation](#documentation)
- [Architecture](#architecture)
- [Cost Analysis](#cost-analysis)
- [Deployment Options](#deployment-options)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

AI Krishi Mitra is a complete agricultural advisory platform that leverages AWS AI services to provide intelligent, personalized farming advice to Indian farmers. The platform supports multiple interfaces (web and WhatsApp) and offers comprehensive features including:

- 🤖 AI-powered agricultural advice using AWS Bedrock (Claude 3)
- 🗣️ Voice interaction in 9 Indian languages
- 📸 Image-based crop and pest diagnosis
- 🌦️ Real-time weather information and advisories
- 👥 Complete user management and admin dashboard
- 📊 Analytics and interaction tracking
- 🌐 Multi-language support (Hindi, English, Telugu, Tamil, Marathi, Punjabi, Kannada, Bengali, Gujarati)

---

## 📁 Project Structure

```
ai-krishi-mitra/
│
├── � poc-django/                    # Django Web Application (Primary Implementation)
│   ├── � krishi_mitra/              # Django project configuration
│   ├── 📂 farmers/                   # Main application (models, views, templates)
│   ├── 📂 aws_services/              # AWS integrations (Bedrock, S3, Transcribe, Polly)
│   ├── 📂 static/                    # Static files (CSS, JS, images)
│   ├── 📂 media/                     # User-uploaded files
│   ├── 📄 requirements.txt           # Python dependencies
│   ├── 📄 manage.py                  # Django management script
│   ├── 📄 README.md                  # Detailed Django app documentation
│   └── 📄 *.md                       # Various guides (setup, features, etc.)
│
├── 📂 data-set/                      # Sample data and datasets
│   ├── advisories.json               # Agricultural advisories
│   ├── crops.json                    # Crop information
│   ├── diseases.json                 # Disease database
│   ├── farmers.json                  # Sample farmer data
│   ├── market-prices.json            # Market price data
│   ├── weather.json                  # Weather data samples
│   └── README.md                     # Dataset documentation
│
├── 📂 specs/                         # Project specifications
│   └── 📂 ai-krishi-mitra/
│       ├── requirements.md           # Project requirements
│       ├── design.md                 # System design document
│       ├── tasks.md                  # Implementation tasks
│       ├── minimal-tasks.md          # MVP task list
│       └── *.md                      # Additional specs
│
├── 📄 README.md                      # This file (project overview)
└── 📄 TeamCore_ProjectsPPT.pptx      # Project presentation
```

---

## ✨ Key Features

### For Farmers

✅ **Intelligent Chat Interface**
- Real-time AI-powered agricultural advice
- Context-aware responses based on farmer profile
- Conversation history and session management

✅ **Multi-Modal Interaction**
- Text queries with instant responses
- Voice input/output in 9 Indian languages
- Image upload for crop/pest diagnosis

✅ **Personalized Dashboard**
- Weather widget with 7-day forecast
- Recent conversations and interactions
- Profile management and settings

✅ **Knowledge Base**
- Comprehensive crop information
- Pest and disease database
- Best practices and farming tips

✅ **WhatsApp Integration** (Optional)
- Familiar messaging interface
- No app installation required
- Low bandwidth requirements

### For Administrators

✅ **User Management**
- Farmer registration approval workflow
- Profile management and verification
- Password reset capabilities

✅ **Content Management**
- Knowledge base editing
- Weather data management
- System configuration

✅ **Analytics & Monitoring**
- Interaction tracking and logging
- Usage statistics and reports
- Performance monitoring

---

## 🛠️ Technology Stack

### Backend
- **Framework**: Django 5.0
- **Language**: Python 3.11
- **Database**: SQLite (dev), PostgreSQL (prod)
- **Web Server**: Gunicorn + Nginx
- **AWS SDK**: boto3

### Frontend
- **HTML5** + **CSS3** + **JavaScript (ES6+)**
- **Bootstrap 5** for responsive UI
- **Web Audio API** for voice recording
- **Fetch API** for AJAX requests

### AWS Services
- **Bedrock**: AI responses (Claude 3 Haiku)
- **Transcribe**: Speech-to-text (8 languages)
- **Polly**: Text-to-speech (Neural voices)
- **S3**: Media file storage
- **IAM**: Access management

### Optional Integrations
- **WhatsApp Business API** (Meta/Twilio/360Dialog)
- **Weather APIs** (OpenWeatherMap, etc.)
- **Payment Gateways** (for premium features)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git
- AWS Account (optional for development)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-krishi-mitra
   ```

2. **Navigate to Django application**
   ```bash
   cd poc-django
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your settings (AWS credentials optional for dev)
   ```

5. **Initialize database**
   ```bash
   python manage.py migrate
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Web Interface: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/
   - Login: `admin` / `admin1234` or `testfarmer` / `test123`

For detailed setup instructions, see the Django application documentation in the `poc-django/` directory.

---

## 📦 Available Implementations

### 1. Django Web Application (Primary)

**Location**: `poc-django/`

**Features**:
- Full-featured web interface
- Complete user management
- Admin dashboard
- Real AWS integration
- Multi-language support
- Voice and image support

**Best For**:
- Web-based farmer portals
- Extension officer dashboards
- Desktop/tablet access
- Administrative management

**Documentation**: See `poc-django/` directory for complete documentation

### 2. WhatsApp Integration (Add-on)

**Integration**: Can be added to Django app

**Features**:
- WhatsApp Business API support
- Text, voice, and image messages
- Auto-registration from WhatsApp
- Template messages for notifications

**Best For**:
- Farmers familiar with WhatsApp
- Low bandwidth environments
- Mobile-first approach
- Feature phone users

**Documentation**: See `poc-django/` directory for WhatsApp integration guide

---

## 📚 Documentation

All detailed documentation is available in the `poc-django/` directory:

- Complete Django application guide
- Quick start and setup instructions
- Feature-specific guides (registration, multi-language, login, etc.)
- AWS Bedrock workflow details
- WhatsApp integration guide
- Deployment instructions
- Troubleshooting guides

For project specifications, see the `specs/ai-krishi-mitra/` directory.

---

## 🏗️ Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        User Interfaces                       │
│  ┌──────────────────┐              ┌──────────────────┐    │
│  │  Web Browser     │              │  WhatsApp        │    │
│  │  (Farmers/Admin) │              │  (Farmers)       │    │
│  └────────┬─────────┘              └────────┬─────────┘    │
└───────────┼──────────────────────────────────┼──────────────┘
            │                                  │
            ▼                                  ▼
┌─────────────────────────────────────────────────────────────┐
│                   Django Web Application                     │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Views & API Endpoints                               │  │
│  │  - Authentication & Authorization                    │  │
│  │  - Chat, Voice, Image Processing                     │  │
│  │  - Dashboard, Profile Management                     │  │
│  │  - Knowledge Base, Weather                           │  │
│  │  - WhatsApp Webhooks                                 │  │
│  └────────────────────┬─────────────────────────────────┘  │
│                       │                                      │
│  ┌────────────────────▼─────────────────────────────────┐  │
│  │  Business Logic Layer                                │  │
│  │  - Context Building                                  │  │
│  │  - Message Processing                                │  │
│  │  - Interaction Logging                               │  │
│  └────────────────────┬─────────────────────────────────┘  │
│                       │                                      │
│  ┌────────────────────▼─────────────────────────────────┐  │
│  │  Data Layer                                          │  │
│  │  - FarmerProfile, Conversation, Message             │  │
│  │  - Interaction, WeatherData                         │  │
│  │  - SQLite/PostgreSQL                                │  │
│  └────────────────────┬─────────────────────────────────┘  │
│                       │                                      │
│  ┌────────────────────▼─────────────────────────────────┐  │
│  │  AWS Service Layer                                   │  │
│  │  - BedrockService (AI)                              │  │
│  │  - TranscribeService (Voice-to-Text)                │  │
│  │  - PollyService (Text-to-Speech)                    │  │
│  │  - S3Service (File Storage)                         │  │
│  │  - WeatherService                                   │  │
│  └────────────────────┬─────────────────────────────────┘  │
└─────────────────────────┼──────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                     AWS Cloud Services                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Bedrock    │  │  Transcribe  │  │    Polly     │     │
│  │  (Claude 3)  │  │ (Voice→Text) │  │ (Text→Voice) │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │      S3      │  │     IAM      │  │  CloudWatch  │     │
│  │   (Storage)  │  │   (Access)   │  │  (Monitoring)│     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
```

### Request Flow

**Text Query**:
```
Farmer → Django View → Build Context → Bedrock (Claude) → 
AI Response → Save to DB → Return to Farmer
```

**Voice Query**:
```
Farmer → Upload Audio → S3 → Transcribe → Text → 
Bedrock (Claude) → AI Response → Polly → Audio → Farmer
```

**Image Query**:
```
Farmer → Upload Image → S3 → Build Context → 
Bedrock (Claude) → AI Analysis → Return to Farmer
```

---

## 💰 Cost Analysis

### Development (Local)

| Component | Cost |
|-----------|------|
| Django Development | Free |
| SQLite Database | Free |
| AWS (Mock Mode) | Free |
| **Total** | **$0/month** |

### Production Costs

#### Small Scale (1,000 farmers, 10 queries/month)

| Service | Monthly Cost |
|---------|--------------|
| EC2 t3.small | $15 |
| RDS PostgreSQL | $15 |
| S3 Storage | $0.25 |
| Bedrock (Claude 3 Haiku) | $2.50 |
| Transcribe | $2.40 |
| Polly | $0.80 |
| Data Transfer | $4.50 |
| Load Balancer | $16 |
| **Total** | **~$56/month** |

#### Medium Scale (10,000 farmers, 10 queries/month)

| Service | Monthly Cost |
|---------|--------------|
| EC2 t3.medium (2x) | $60 |
| RDS PostgreSQL | $30 |
| S3 | $2.50 |
| Bedrock | $25 |
| Transcribe | $24 |
| Polly | $8 |
| Data Transfer | $45 |
| Load Balancer | $16 |
| **Total** | **~$210/month** |

#### With WhatsApp Integration

Add to above costs:

| Provider | Cost (10,000 messages/month) |
|----------|------------------------------|
| Meta WhatsApp Business | $42 |
| Twilio WhatsApp | $50 |
| 360Dialog | €42 (~$45) |

### Cost Optimization

- Use AWS Reserved Instances (30-40% savings)
- Implement caching to reduce API calls
- Use S3 lifecycle policies for old files
- Enable CloudFront CDN for static content
- Monitor and set billing alerts

---

## 🚢 Deployment Options

### 1. AWS Elastic Beanstalk (Recommended)

**Pros**:
- Managed platform
- Auto-scaling
- Easy deployment
- Integrated monitoring

**Setup**:
```bash
cd poc-django
eb init -p python-3.11 krishi-mitra
eb create krishi-mitra-prod
eb deploy
```

### 2. AWS EC2 + RDS

**Pros**:
- Full control
- Customizable
- Cost-effective for scale

**Setup**: See deployment documentation in `poc-django/` directory

### 3. Docker + AWS ECS

**Pros**:
- Containerized
- Portable
- Scalable

**Setup**:
```bash
docker build -t krishi-mitra .
docker push <ecr-repo>
# Deploy to ECS
```

### 4. Heroku (Quick Deploy)

**Pros**:
- Fastest deployment
- Free tier available
- Simple management

**Setup**:
```bash
heroku create krishi-mitra
git push heroku main
```

---

## 🔒 Security Features

- ✅ CSRF protection enabled
- ✅ XSS prevention
- ✅ SQL injection protection
- ✅ Secure password hashing (PBKDF2)
- ✅ HTTPS in production
- ✅ AWS IAM role-based access
- ✅ Environment variable secrets
- ✅ Session security
- ✅ Rate limiting (configurable)
- ✅ Input validation and sanitization

---

## 🧪 Testing

### Run Tests

```bash
cd poc-django
python manage.py test
```

### Test Coverage

```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

### Load Testing

```bash
pip install locust
locust -f locustfile.py
```

---

## 📊 Project Status

| Component | Status |
|-----------|--------|
| Core Features | ✅ Complete |
| AWS Integration | ✅ Functional (mock + real) |
| Multi-Language | ✅ 9 languages |
| Admin Panel | ✅ Full management |
| Documentation | ✅ Comprehensive |
| WhatsApp Integration | ✅ Implementation guide |
| Mobile App | 🚧 Planned |
| Advanced Analytics | 🚧 In progress |
| Community Forum | 🚧 Planned |

---

## 🤝 Contributing

We welcome contributions! Here's how:

### Ways to Contribute

1. **Report Bugs**: Open an issue with details
2. **Suggest Features**: Share your ideas
3. **Submit Code**: Create pull requests
4. **Improve Docs**: Fix typos, add examples
5. **Test**: Try the app and provide feedback

### Development Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Write/update tests
5. Update documentation
6. Commit (`git commit -m 'Add amazing feature'`)
7. Push (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Code Standards

- Follow PEP 8 for Python code
- Write docstrings for functions
- Add comments for complex logic
- Keep functions small and focused
- Write tests for new features

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **AWS AI for Bharat Hackathon** for the opportunity
- **Django Community** for the excellent framework
- **AWS** for AI services (Bedrock, Transcribe, Polly)
- **Bootstrap** for UI components
- **Indian Farmers** for inspiration and feedback
- **Open Source Community** for tools and libraries

---

## 📞 Support & Contact

### Get Help

- **Documentation**: See `poc-django/` directory for complete guides
- **Issues**: Open a GitHub issue
- **Discussions**: Use GitHub Discussions

### Resources

- **Django Documentation**: https://docs.djangoproject.com/
- **AWS Bedrock**: https://aws.amazon.com/bedrock/
- **AWS Boto3**: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
- **Bootstrap**: https://getbootstrap.com/docs/5.0/
- **WhatsApp Business API**: https://developers.facebook.com/docs/whatsapp
- **Twilio WhatsApp**: https://www.twilio.com/docs/whatsapp

---

## 🎯 Roadmap

### Phase 1: MVP (Completed ✅)
- [x] Django web application
- [x] AWS Bedrock integration
- [x] Multi-language support
- [x] Voice and image support
- [x] Admin dashboard
- [x] WhatsApp integration guide

### Phase 2: Enhancement (In Progress 🚧)
- [ ] Advanced analytics dashboard
- [ ] Expert consultation booking
- [ ] Community forum

### Phase 3: Scale (Planned 📋)
- [ ] WhatsApp integration 
- [ ] Multi-tenant architecture
- [ ] API marketplace
- [ ] Machine learning models
- [ ] Offline mode
- [ ] Regional language expansion

---

<div align="center">

## 🌾 Made with ❤️ for Indian Farmers

**Empowering Agriculture Through AI**

[⬆ Back to Top](#-ai-krishi-mitra---agricultural-ai-assistant-platform)

</div>
