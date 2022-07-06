from accounts.models import CustomUser
from accounts.tests.factories import UserFactory
from django.test import RequestFactory
import pytest


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> CustomUser:
    return UserFactory()


@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()
