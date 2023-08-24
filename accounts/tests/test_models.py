from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="kevin",
            email="kevin@example.com",
            password="T3stP@5s123",
        )

        self.super_user = User.objects.create_superuser(
            username="superadmin",
            email="superadmin@example.com",
            password="T3stP@5s123",
        )

    def test___str__(self):
        assert self.user.__str__() == self.user.username
        assert str(self.user) == self.user.username

    def test_user_get_absolute_url(self):
        assert self.user.get_absolute_url() == f"/accounts/{self.user.username}/"

    def test_create_user(self):
        self.assertEqual(self.user.username, "kevin")
        self.assertEqual(self.user.email, "kevin@example.com")
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_user_asserts(self):
        User = get_user_model()
        try:
            self.assertIsNotNone(self.user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(username="", email="", password="foo")

    def test_create_superuser(self):
        self.assertEqual(self.super_user.username, "superadmin")
        self.assertEqual(self.super_user.email, "superadmin@example.com")
        self.assertTrue(self.super_user.is_active)
        self.assertTrue(self.super_user.is_staff)
        self.assertTrue(self.super_user.is_superuser)

    def test_superuser_asserts(self):
        User = get_user_model()
        try:
            self.assertIsNotNone(self.super_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username="",
                email="super@user.com",
                password="foo",
                is_superuser=False,
            )
