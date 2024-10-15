from django.contrib import admin
from django.contrib.auth import admin as admin_auth_django
from .models import User
from .forms import UserChangeForm, UserCreationForm

@admin.register(User)
class UsersAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User

    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('Sistemas', {'fields': ('sistemas',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'sistemas'),
        }),
    )