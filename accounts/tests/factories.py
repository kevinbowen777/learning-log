from typing import ClassVar

from django.contrib.auth import get_user_model
from factory.declarations import PostGenerationMethodCall
from factory.django import DjangoModelFactory
from factory.faker import Faker


class UserFactory(DjangoModelFactory):
    username = Faker("user_name")
    email = Faker("email")
    name = Faker("name")
    password = PostGenerationMethodCall("set_password", "P@s5word")

    class Meta:
        model = get_user_model()
        django_get_or_create: ClassVar[list[str]] = ["username"]
        skip_postgeneration_save = True
