# Farmer Registration System - User Guide

## Overview

The AI Krishi Mitra platform now features a simplified farmer registration process with:
- Language-first approach (select language before filling the form)
- Voice input support for all text fields
- Comma-separated crop selection
- Admin approval workflow
- Multi-language support (8 Indian languages)

## Registration Flow

### For Farmers

#### Step 1: Access Registration Page
-  click "Register" from the home page

#### Step 2: Select Preferred Language
**This is the first and most important step!**

Choose your preferred language from:
- English (en)
- Hindi (hi)
- Telugu (te)
- Tamil (ta)
- Marathi (mr)
- Kannada (kn)
- Bengali (bn)
- Gujarati (gu)

Once selected, you can fill the rest of the form using:
- **Text input**: Type normally
- **Voice input**: Click the 🎤 button next to any field and speak in your selected language

#### Step 3: Account Details
Fill in:
- **Username**: Unique username for login
- **Password**: Secure password
- **Confirm Password**: Re-enter password

#### Step 4: Personal Details
- **Full Name** (optional): Your complete name
  - Can use voice input 🎤

#### Step 5: Contact Information
- **Phone Number**: Your mobile number (format: +91XXXXXXXXXX)

#### Step 6: Location Details
All fields support voice input:
- **Village/City**: Your location
- **State**: Your state
- **District**: Your district

#### Step 7: Farm Details
- **Crops**: Enter crop names separated by commas
  - Example: `rice, wheat, cotton`
  - Example: `धान, गेहूं, कपास` (in Hindi)
  - Can use voice input 🎤
  
- **Farm Size**: Size in hectares (optional)

#### Step 8: Submit
- Click "Register" button
- You'll be redirected to a pending approval page

### Voice Input Feature

**How to use voice input:**

1. Select your language first (Step 2)
2. Click the 🎤 microphone button next to any field
3. Allow microphone access when prompted
4. Speak clearly in your selected language
5. Click the ⏹️ stop button when done
6. The transcribed text will appear in the field

**Supported fields for voice input:**
- Full Name
- Village/City
- State
- District
- Crops (comma-separated)

**Tips for best results:**
- Speak clearly and at a moderate pace
- Minimize background noise
- For crops, say: "rice comma wheat comma cotton"
- The system will transcribe in your selected language

### After Registration

**Pending Approval:**
- Your account is created but inactive
- You'll see a "Registration Pending" page
- Admin will review your details
- Typical approval time: 24-48 hours

**What you can do while pending:**
- Browse public pages (Home, Knowledge Base, Weather)
- Cannot access Dashboard or Chat until approved

**After Approval:**
- Login with your username and password
- Access all features (Dashboard, Chat, etc.)
- Start using AI-powered agricultural assistance

**If Rejected:**
- You'll see the rejection reason
- Can register again with correct information
- Contact support for assistance

## For Admins

### Accessing Admin Panel

1. Visit: http://127.0.0.1:8000/admin/
2. Login with superuser credentials:
   - Username: `admin`
   - Password: ` `

### Reviewing Registrations

#### View Pending Registrations

1. Go to Admin Panel → Farmer Profiles
2. Filter by "Approval Status" → "Pending Approval"
3. You'll see all pending farmer registrations

#### Approve Farmers

**Method 1: Bulk Approval**
1. Select farmers using checkboxes
2. Choose "Approve selected farmers" from Actions dropdown
3. Click "Go"
4. Farmers can now login and access the system

**Method 2: Individual Approval**
1. Click on a farmer profile
2. Change "Approval status" to "Approved"
3. Save
4. The "Approved by" and "Approved at" fields are auto-filled

#### Reject Farmers

**Method 1: Bulk Rejection**
1. Select farmers using checkboxes
2. Choose "Reject selected farmers" from Actions dropdown
3. Click "Go"

**Method 2: Individual Rejection with Reason**
1. Click on a farmer profile
2. Change "Approval status" to "Rejected"
3. Enter "Rejection reason" (e.g., "Invalid phone number", "Incomplete information")
4. Save
5. Farmer will see this reason when they login

### Admin Panel Features

**List View:**
- User
- Phone Number
- Location
- Language
- Approval Status
- Created At

**Filters:**
- Approval Status (Pending/Approved/Rejected)
- Language
- State
- Created Date

**Search:**
- Username
- Phone Number
- Location
- First Name
- Last Name

**Bulk Actions:**
- Approve selected farmers
- Reject selected farmers

## Technical Details

### Database Schema

**New Fields in FarmerProfile:**
```python
approval_status = CharField(choices=['pending', 'approved', 'rejected'], default='pending')
approved_by = ForeignKey(User, null=True)  # Admin who approved
approved_at = DateTimeField(null=True)     # Approval timestamp
rejection_reason = TextField(blank=True)    # Reason for rejection
```

**Additional Languages:**
- Kannada (kn)
- Bengali (bn)
- Gujarati (gu)

### API Endpoints

**Registration:**
- URL: `/register/`
- Method: GET (show form), POST (submit)
- Public access

**Voice Transcription:**
- URL: `/api/transcribe-voice/`
- Method: POST
- Parameters:
  - `audio`: Audio file (OGG format)
  - `language`: Language code (en, hi, te, etc.)
  - `field_name`: Target field name
- Returns: `{success: true, transcript: "text", field_name: "field"}`

**Registration Status:**
- URL: `/registration/pending/`
- Shows pending approval message
- Public access (for registered users)

### Access Control

**Before Approval:**
- Can access: Home, Knowledge Base, Weather, Login, Logout
- Cannot access: Dashboard, Chat, Profile Setup

**After Approval:**
- Full access to all features

**If Rejected:**
- Can see rejection reason
- Can register again
- Cannot access protected pages

## Testing the Registration System

### Test Scenario 1: Text Registration

1. Go to http://127.0.0.1:8000/register/
2. Select language: English
3. Fill all fields by typing
4. Crops: `rice, wheat, cotton`
5. Submit
6. Verify pending page appears
7. Login to admin panel
8. Approve the farmer
9. Login as farmer
10. Verify dashboard access

### Test Scenario 2: Voice Registration

1. Go to http://127.0.0.1:8000/register/
2. Select language: Hindi
3. Click 🎤 on "Full Name" field
4. Speak: "राम कुमार"
5. Verify transcription
6. Repeat for other fields
7. Submit and verify

### Test Scenario 3: Admin Approval

1. Create 3 test registrations
2. Login to admin panel
3. Select all 3 farmers
4. Use bulk approve action
5. Verify all are approved
6. Login as each farmer
7. Verify access granted

### Test Scenario 4: Rejection

1. Create a test registration
2. Login to admin panel
3. Open the farmer profile
4. Set status to "Rejected"
5. Add reason: "Invalid phone number"
6. Save
7. Login as that farmer
8. Verify rejection message with reason

## Troubleshooting

### Voice Input Not Working

**Issue:** Microphone button doesn't work

**Solutions:**
1. Check browser permissions (allow microphone access)
2. Use Chrome/Firefox (best support)
3. Check if HTTPS is enabled (required for microphone)
4. Try typing instead

**Issue:** Transcription fails

**Solutions:**
1. Ensure language is selected first
2. Speak clearly and slowly
3. Check internet connection (AWS Transcribe needs connectivity)
4. In mock mode, transcription may not work - type manually

### Registration Issues

**Issue:** "Username already exists"

**Solution:** Choose a different username

**Issue:** "Phone number already registered"

**Solution:** This phone number is already in the system. Contact admin or use a different number.

**Issue:** Can't access dashboard after registration

**Solution:** Your account is pending approval. Wait for admin approval (24-48 hours).

### Admin Issues

**Issue:** Can't see pending registrations

**Solution:** 
1. Check filter settings
2. Ensure you're logged in as admin/superuser
3. Refresh the page

**Issue:** Bulk actions not working

**Solution:**
1. Ensure farmers are selected (checkboxes)
2. Choose action from dropdown
3. Click "Go" button

## Best Practices

### For Farmers

1. **Select language first** - This is crucial for voice input
2. **Use voice for long text** - Easier than typing on mobile
3. **Speak clearly** - Better transcription accuracy
4. **Verify transcription** - Check text before submitting
5. **Provide accurate information** - Helps with approval
6. **Use comma separation for crops** - e.g., "rice, wheat, cotton"

### For Admins

1. **Review regularly** - Check pending registrations daily
2. **Verify phone numbers** - Ensure valid format
3. **Check location details** - Verify state/district match
4. **Provide clear rejection reasons** - Helps farmers understand
5. **Use bulk actions** - Faster for multiple approvals
6. **Monitor approval metrics** - Track approval rates

## Security Features

1. **Password validation** - Secure password requirements
2. **Unique constraints** - Username and phone number must be unique
3. **CSRF protection** - All forms protected
4. **Admin-only approval** - Only superusers can approve
5. **Audit trail** - Tracks who approved and when
6. **Session management** - Secure login/logout

## Future Enhancements

Planned features:
1. Email notifications on approval/rejection
2. SMS notifications
3. Farmer can edit profile after approval
4. Bulk upload of farmers (CSV)
5. Advanced filtering in admin
6. Registration analytics dashboard
7. Multi-step form with progress indicator
8. Photo upload for verification
9. Aadhaar integration
10. Regional language UI translation

## Support

For issues or questions:
- Check this guide first
- Review RUNNING.md for general setup
- Check server logs for errors
- Contact system administrator

---

**Registration System Version:** 1.0  
**Last Updated:** March 8, 2026  
**Django Version:** 5.0.1  
**Python Version:** 3.11+
