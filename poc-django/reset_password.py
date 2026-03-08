#!/usr/bin/env python
"""Reset password for testfarmer"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'krishi_mitra.settings')
django.setup()

from django.contrib.auth.models import User

# Reset testfarmer password
try:
    user = User.objects.get(username='testfarmer')
    user.set_password('test123')
    user.save()
    print(f"✅ Password reset for user: {user.username}")
    print(f"   Username: testfarmer")
    print(f"   Password: test123")
    print(f"   Is active: {user.is_active}")
    
    # Check profile
    if hasattr(user, 'farmer_profile'):
        profile = user.farmer_profile
        print(f"   Has profile: Yes")
        print(f"   Approval status: {profile.approval_status}")
        print(f"   Language: {profile.language}")
    else:
        print(f"   Has profile: No")
        
except User.DoesNotExist:
    print("❌ User 'testfarmer' does not exist")
