from django.test import SimpleTestCase
from django.urls import reverse


class ContactFormTests(SimpleTestCase):
    def setUp(self):
        url = reverse("contact")
        self.response = self.client.get(url)
        self.form_data = {
            "from_email": "joe@example.com",
            "subject": "Test Email",
            "message": "This is a test email",
        }

    def test_contact_page_form_is_valid(self):
        response = self.client.post(
            "/contact/",
            data={
                "from_email": "joe@example.com",
                "subject": "Test Email",
                "message": "This is a test email",
            },
        )
        self.assertEqual(response.status_code, 302)
