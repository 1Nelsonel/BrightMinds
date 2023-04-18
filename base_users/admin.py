from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserProfile,Payment


# Define an inline for UserProfile to be included in the UserAdmin
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


# Define a new UserAdmin with the UserProfileInline included
class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )


# Re-register the UserAdmin with our custom version
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile_number', 'id_number')
    list_filter = ('user__is_superuser',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'amount', 'phone_number', 'reference', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('transaction_id', 'phone_number', 'reference')
    readonly_fields = ('transaction_id', 'amount', 'phone_number', 'reference', 'status', 'status_description', 'created_at')