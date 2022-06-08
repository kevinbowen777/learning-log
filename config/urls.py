from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),
    # User management
    path("accounts/", include("allauth.urls")),
    # Local apps
    path("accounts/", include("accounts.urls")),
    path("", include("learning_logs.urls")),
    path("", include("pages.urls")),
]

if settings.DEBUG:
    import debug_toolbar  # noqa: F401

    urlpatterns = [
        path("__debug__/", include("debug_toolbar.urls")),
    ] + urlpatterns
