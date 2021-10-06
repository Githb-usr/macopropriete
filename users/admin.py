from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    """
    Display of User in the back office
    """
    list_display = ('email', 'password', 'username', 'is_active', 'is_staff',
                    'is_superuser', 'date_joined', 'last_login', 'updated_at', 'user_type',
                    'first_name', 'last_name', 'contact_email', 'phone_number', 'avatar',
                    'about', 'is_resident', 'is_union_council')

admin.site.register(User, UserAdmin)
