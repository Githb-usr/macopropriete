from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import User

class UserAdmin(admin.ModelAdmin):
    """
    Display of User in the back office
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    empty_value_display = '-empty-'
    list_display = ('email','username', 'status', 'is_active', 'is_staff',
                    'date_joined', 'last_login', 'updated_at', 'user_type',
                    'first_name', 'last_name', 'contact_email', 'phone_number',
                    'avatar', 'about', 'is_resident', 'is_union_council',)
    fieldsets = (
        ('Compte', {'fields': ('email', 'password', 'status',)}),
        ('Personne', {'fields': ('user_type', 'first_name', 'last_name', 'contact_email', 'phone_number',
                    'username', 'avatar', 'about',)}),
        ('Statuts', {'fields': ('is_active', 'is_resident', 'is_union_council', 'is_staff',)}),
    )
    list_editable = ('user_type', 'first_name', 'last_name', 'contact_email', 'phone_number', 
                     'is_resident', 'is_union_council',)
    list_filter = ('date_joined', 'is_active','is_resident', 'is_union_council', 'is_staff',)
    ordering = ('last_name',)
    search_fields = ('email', 'first_name', 'last_name',)

admin.site.register(User, UserAdmin)
