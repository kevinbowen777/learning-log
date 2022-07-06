"""Views for django-start user accounts."""
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    RedirectView,
    UpdateView,
)

from .forms import CustomUserCreationForm

User = get_user_model()


class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("account_login")
    template_name = "account/signup.html"


class UserDetailView(LoginRequiredMixin, DetailView):
    """Tell the view to index lookups by username."""

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"

    template_name = "account/user_detail.html"


class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = [
        "name",
        "bio",
        "country",
        "profile_pic",
    ]
    model = User

    def get_success_url(self):
        """Send the user back to their own page after a successful update."""
        return reverse(
            "user_detail",
            kwargs={"username": self.request.user.username},
        )

    def get_object(self):
        """Only get the user record for the user making the request."""
        return User.objects.get(username=self.request.user.username)

    template_name = "account/user_form.html"


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(
            "user_detail",
            kwargs={"username": self.request.user.username},
        )
