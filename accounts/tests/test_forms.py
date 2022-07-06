import pytest

from .factories import UserFactory
from ..forms import CustomUserCreationForm

pytestmark = pytest.mark.django_db


class TestUserCreationForm:
    def test_clean_username(self):
        user = UserFactory.build()

        form = CustomUserCreationForm(
            {
                "username": user.username,
                "password1": user._password,
                "password2": user._password,
            }
        )

        assert form.is_valid()
        assert form.clean_username() == user.username

        # Creating a user.
        form.save()

        # The user with proto_user params already exists,
        # hence cannot be created.
        form = CustomUserCreationForm(
            {
                "username": user.username,
                "password1": user._password,
                "password2": user._password,
            }
        )

        assert not form.is_valid()
        assert len(form.errors) == 1
        assert "username" in form.errors
