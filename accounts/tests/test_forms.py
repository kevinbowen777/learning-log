import pytest

from ..forms import CustomUserCreationForm
from .factories import UserFactory

pytestmark = pytest.mark.django_db


class TestUserCreationForm:
    def test_clean_username(self):
        user = UserFactory.build()

        form = CustomUserCreationForm(
            # fmt: off
            {
                "username": user.username,
                "password1": user._password,
                "password2": user._password,
            }
            # fmt: on
        )

        assert form.is_valid()
        assert form.clean_username() == user.username

        # Creating a user.
        form.save()

        # The user with proto_user params already exists,
        # hence cannot be created.
        form = CustomUserCreationForm(
            # fmt: off
            {
                "username": user.username,
                "password1": user._password,
                "password2": user._password,
            }
            # fmt: on
        )

        assert not form.is_valid()
        assert len(form.errors) == 1
        assert "username" in form.errors
