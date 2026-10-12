from django.contrib.auth import get_user_model
from factory.declarations import PostGenerationMethodCall
from factory.faker import Faker
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    username = Faker("user_name")
    email = Faker("email")
    name = Faker("name")
    password = PostGenerationMethodCall("set_password", "P@s5word")

    class Meta:
        model = get_user_model()
        django_get_or_create = ["username"]
        skip_postgeneration_save = True
