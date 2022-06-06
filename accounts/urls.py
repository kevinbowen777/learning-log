from django.urls import path

from .views import SignupPageView

# app_name = "accounts"
urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
]
