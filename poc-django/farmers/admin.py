"""
Admin configuration for farmers app
"""
from django.contrib import admin
from django.utils import timezone
from django.urls import reverse
from django.utils.html import format_html
from .models import FarmerProfile, Conversation, Message, Interaction, WeatherData


@admin.register(FarmerProfile)
class FarmerProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'location', 'language', 'approval_status', 'reset_password_link', 'created_at']
    list_filter = ['approval_status', 'language', 'state', 'created_at']
    search_fields = ['user__username', 'phone_number', 'location', 'user__first_name', 'user__last_name']
    readonly_fields = ['created_at', 'updated_at', 'approved_by', 'approved_at', 'reset_password_link']
    
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'phone_number', 'language', 'reset_password_link')
        }),
        ('Location Details', {
            'fields': ('location', 'state', 'district')
        }),
        ('Farm Details', {
            'fields': ('crops', 'farm_size')
        }),
        ('Approval Status', {
            'fields': ('approval_status', 'approved_by', 'approved_at', 'rejection_reason')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    
    actions = ['approve_farmers', 'reject_farmers', 'reset_passwords']
    
    def reset_password_link(self, obj):
        """Display link to reset user password"""
        if obj.user:
            url = reverse('admin:auth_user_password_change', args=[obj.user.id])
            return format_html('<a href="{}" class="button">Reset Password</a>', url)
        return '-'
    reset_password_link.short_description = 'Password Reset'
    
    def approve_farmers(self, request, queryset):
        """Approve selected farmer registrations"""
        updated = queryset.filter(approval_status='pending').update(
            approval_status='approved',
            approved_by=request.user,
            approved_at=timezone.now()
        )
        self.message_user(request, f'{updated} farmer(s) approved successfully.')
    approve_farmers.short_description = 'Approve selected farmers'
    
    def reject_farmers(self, request, queryset):
        """Reject selected farmer registrations"""
        updated = queryset.filter(approval_status='pending').update(
            approval_status='rejected',
            approved_by=request.user,
            approved_at=timezone.now()
        )
        self.message_user(request, f'{updated} farmer(s) rejected.')
    reject_farmers.short_description = 'Reject selected farmers'
    
    def reset_passwords(self, request, queryset):
        """Redirect to password reset for selected farmers"""
        if queryset.count() == 1:
            farmer = queryset.first()
            url = reverse('admin:auth_user_password_change', args=[farmer.user.id])
            from django.shortcuts import redirect
            return redirect(url)
        else:
            self.message_user(request, 'Please select only one farmer to reset password.', level='warning')
    reset_passwords.short_description = 'Reset password for selected farmer'


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ['id', 'farmer', 'title', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'conversation', 'sender_type', 'message_type', 'created_at']
    list_filter = ['sender_type', 'message_type']


@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ['farmer', 'interaction_type', 'created_at']
    list_filter = ['interaction_type']


@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ['location', 'temperature', 'humidity', 'conditions']
