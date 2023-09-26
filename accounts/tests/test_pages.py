from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from ..views import SignupPageView


class SignupPageTests(TestCase):
    username = "newuser"
    email = "newuser@example.com"

    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_page_status(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(  # noqa: F841
            self.username, self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)

    def test_signup_view(self):
        view = resolve("/accounts/signup/")
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__,
        )


class AccountPagesTest(TestCase):
    def test_login_page_status(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)

    def test_logout_page_status(self):
        response = self.client.get("/accounts/logout/")
        self.assertEqual(response.status_code, 302)


class AdminPageTests(TestCase):
    def test_admin_page_status(self):
        response = self.client.get("/resources/login/")
        self.assertEqual(response.status_code, 200)
