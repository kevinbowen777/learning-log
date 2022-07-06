from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = [
        "email",
        "username",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets
    fieldsets[1][1]["fields"] = fieldsets[1][1]["fields"] + (
        "age",
        "country",
        "profile_pic",
        "bio",
    )


admin.site.register(User, CustomUserAdmin)
