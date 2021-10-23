from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from config.settings import ACCOUNT_VALIDATION_URL, EMAIL_HOST_USER
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import User
from users.settings import ACCOUNT_VALIDATION_SUBJECT
from users.utils import get_random_string, generic_send_mail

class UserAdmin(admin.ModelAdmin):
    """
    Display of User in the back office
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    empty_value_display = '-empty-'
    list_display = ('email', 'password', 'status', 'is_active', 'is_staff',
                    'date_joined', 'last_login', 'updated_at', 'user_type',
                    'first_name', 'last_name', 'contact_email', 'phone_number',
                    'avatar', 'about', 'is_resident', 'is_union_council',)
    fieldsets = (
        ('Compte', {'fields': ('email', 'password', 'status', 'uuid')}),
        ('Personne', {'fields': ('user_type', 'first_name', 'last_name', 'contact_email', 'phone_number',
                    'avatar', 'about',)}),
        ('Statuts', {'fields': ('is_active', 'is_resident', 'is_union_council', 'is_staff',)}),
    )
    list_editable = ('password', 'user_type', 'first_name', 'last_name', 'contact_email', 'phone_number', 
                     'is_resident', 'is_union_council',)
    list_filter = ('date_joined', 'is_active','is_resident', 'is_union_council', 'is_staff',)
    ordering = ('last_name',)
    search_fields = ('email', 'first_name', 'last_name',)
    
    def save_model(self, request, obj, form, change):
            user_password = get_random_string(10)
            obj.set_password(user_password)
            super().save_model(request, obj, form, change)
            email_context = {
                'hostname': request.META['HTTP_HOST'],
                'validation_url': ACCOUNT_VALIDATION_URL,
                'password': user_password,
                'user_name': obj.get_full_name,
                'user_uuid': obj.uuid,
            }
            html_message = render_to_string('users/account_validation_mail.html', email_context)
            plain_message = strip_tags(html_message)
            from_email = EMAIL_HOST_USER
            print('TOTO', html_message)
            mail.send_mail(ACCOUNT_VALIDATION_SUBJECT, plain_message, from_email, [obj.email], html_message=html_message)

admin.site.register(User, UserAdmin)
