from django.urls import path

from .views import UserDetailView, UserRedirectView, UserUpdateView

urlpatterns = [
    path("~redirect/", UserRedirectView.as_view(), name="redirect"),
    path("~update/", UserUpdateView.as_view(), name="user_update"),
    path("<str:username>/", UserDetailView.as_view(), name="user_detail"),
]
