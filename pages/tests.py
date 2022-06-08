from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_homepage_contains_correct_html(self):
        response = self.client.get("/")
        self.assertContains(response, "Learning Log")

    def test_homepage_does_not_contain_incorrect_html(self):
        response = self.client.get("/")
        self.assertNotContains(
            response, "Hi there! I should not be on the page."
        )
