# AI Krishi Mitra - Dummy Data Documentation

## Overview
This directory contains comprehensive dummy data for the AI Krishi Mitra platform, covering all major entities and interactions in the system.

## Data Files

### 1. farmers.json
Contains farmer profile information including:
- Farmer ID and hashed phone number
- Personal details (name, language preference)
- Location (state, district, tehsil, village)
- Farm details (size, soil type, crops grown)
- Registration and activity dates
- Premium subscription status

**Sample Size**: 5 farmers across different states and languages

### 2. crops.json
Comprehensive crop information including:
- Crop ID and name
- Varieties available
- Growth stages with duration
- Total crop duration
- Water requirements
- Suitable soil types
- Common diseases

**Crops Covered**: Rice, Wheat, Cotton

### 3. weather.json
Weather forecasts and alerts:
- Hyperlocal weather data (5km radius)
- Temperature, humidity, rainfall predictions
- Wind speed and UV index
- Weather conditions and alerts
- 48-hour and 7-day forecasts

**Locations**: Punjab, Telangana, Maharashtra, Tamil Nadu

### 4. farmer-profiles.json
Detailed farmer crop management data:
- Current crops being grown
- Sowing dates and growth stages
- Days after sowing (DAS)
- Soil test results (pH, NPK levels)
- Previous harvest data
- Pest history
- Farmer preferences (communication time, organic farming)

**Sample Size**: 3 detailed farmer profiles

### 5. conversations.json
WhatsApp voice conversation logs:
- Conversation ID and session details
- Message timestamps and types
- Voice transcriptions (original language + English translation)
- Audio URLs and confidence scores
- System responses with advisory IDs
- Conversation summaries and satisfaction scores

**Sample**: 1 complete Hindi conversation about wheat rust disease

### 6. advisories.json
Agricultural advisory recommendations:
- Advisory ID linked to farmer and crop
- Issue type (disease, pest, irrigation)
- Severity levels
- Detailed recommendations (chemical/organic treatments)
- Dosage, application methods, precautions
- Cost estimates
- Follow-up schedules
- Explanations based on crop stage and weather

**Sample Size**: 3 advisories (wheat disease, cotton pest, sugarcane irrigation)

### 7. diseases.json
Disease database with:
- Disease ID, name, and scientific name
- Affected crops
- Symptoms and identification
- Favorable conditions for disease spread
- Growth stages affected
- Severity levels
- Treatment options (chemical and organic)
- Prevention measures

**Diseases Covered**: Brown Rust (Wheat), Bacterial Blight (Cotton), Blast (Rice)

### 8. market-prices.json
Market price information:
- Commodity prices from various mandis
- MSP (Minimum Support Price) comparison
- Price trends (rising, stable, declining)
- Arrival quantities
- Quality grades
- Price alerts for farmers

**Markets**: Ludhiana, Warangal, Nashik, Coimbatore, Erode

### 9. notifications.json
Notification system data:
- Weather alerts
- Pest alerts
- Irrigation reminders
- Market price updates
- Follow-up reminders
- Notification preferences per farmer
- Delivery status and read receipts
- Quiet hours configuration

**Sample Size**: 5 notifications across different types

### 10. analytics.json
Platform-wide analytics and metrics:
- Total and active farmer counts
- Daily/monthly activity metrics
- Language distribution
- Crop distribution
- State-wise distribution
- Query type analysis
- Impact metrics (yield improvement, cost reduction)
- Technical performance (ASR accuracy, response time, uptime)

**Date**: February 28, 2026

## Data Relationships

```
farmers.json
    ↓
farmer-profiles.json (detailed crop data)
    ↓
conversations.json (farmer interactions)
    ↓
advisories.json (recommendations given)
    ↓
notifications.json (follow-ups and alerts)

crops.json ← Referenced by farmer-profiles and advisories
diseases.json ← Referenced by advisories
weather.json ← Used for advisory generation
market-prices.json ← Used for price alerts
analytics.json ← Aggregated platform metrics
```

## Usage Scenarios

### 1. Testing Voice Interaction Flow
Use `conversations.json` to test:
- Voice transcription accuracy
- Multi-turn conversation handling
- Context retention
- Response generation in regional languages

### 2. Testing Advisory Engine
Use combination of:
- `farmer-profiles.json` for farmer context
- `crops.json` for crop stage information
- `weather.json` for weather-based recommendations
- `diseases.json` for disease identification
- Generate advisories similar to `advisories.json`

### 3. Testing Notification System
Use `notifications.json` to test:
- Alert generation and delivery
- Notification preferences
- Quiet hours enforcement
- Multi-channel delivery (WhatsApp, SMS)

### 4. Testing Analytics Dashboard
Use `analytics.json` to populate:
- Platform metrics dashboards
- Language and crop distribution charts
- Impact metrics visualization
- Technical performance monitoring

## Data Characteristics

### Realistic Indian Context
- Indian farmer names and locations
- Regional languages (Hindi, Telugu, Tamil, Marathi, Kannada)
- Indian crops and varieties
- Indian weather patterns
- MSP and mandi prices in INR
- Indian agricultural practices

### Temporal Consistency
- All dates aligned to February 2026
- Growth stages match sowing dates
- Weather forecasts are current
- Conversation timestamps are logical

### Multilingual Support
- Conversations in native scripts (Devanagari, Telugu, Tamil)
- English translations provided
- Language codes follow ISO standards (hi-IN, te-IN, etc.)

## Extension Points

To add more dummy data:

1. **More Farmers**: Add entries to `farmers.json` with different states/languages
2. **More Crops**: Extend `crops.json` with vegetables, pulses, etc.
3. **More Conversations**: Add conversations in other languages
4. **More Diseases**: Expand `diseases.json` with more crop diseases
5. **Seasonal Data**: Create weather/crop data for different seasons

## Data Volume Summary

| File | Records | Languages | States |
|------|---------|-----------|--------|
| farmers.json | 5 | 5 | 5 |
| crops.json | 3 | - | - |
| weather.json | 4 forecasts + 1 alert | - | 4 |
| farmer-profiles.json | 3 | - | 3 |
| conversations.json | 1 complete | 1 (Hindi) | 1 |
| advisories.json | 3 | 3 | 3 |
| diseases.json | 3 | - | - |
| market-prices.json | 5 prices + 2 alerts | - | 4 |
| notifications.json | 5 + 2 preferences | 4 | 4 |
| analytics.json | Platform-wide | 8 | 7 |

## Notes

- All phone numbers are hashed (SHA256) for privacy
- Audio URLs point to S3 bucket structure (not actual files)
- Prices are in Indian Rupees (INR)
- Dates use ISO 8601 format
- All data is fictional but realistic
