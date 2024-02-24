from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError

User = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "email",
            "username",
        )


class CustomUserCreationForm(UserCreationForm):
    error_message = UserCreationForm.error_messages.update(
        {"duplicate_username": "This username has already been taken."}  # fmt: skip
    )

    class Meta:
        model = User
        fields = (
            "email",
            "username",
        )

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])
