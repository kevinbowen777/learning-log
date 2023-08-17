from django.core.mail import BadHeaderError
from django.test import SimpleTestCase


class ContactFormTests(SimpleTestCase):
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

    def test_contact_form_is_invalid(self):
        response = self.client.post(
            "/contact/",
            data={
                "from_email": "john@example.com",
                "subject": "Test Email",
                "not_a_form_field": "This is a test",
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_header_injection(self):
        error_occured = True
        try:
            self.client.post(
                "/contact/",
                data={
                    "from_email": "joe@example.com",
                    "subject": "Subject\nInjectionTest",
                    "message": "This is a test of a BadHeaderError",
                },
            )
            error_occured = False
        except BadHeaderError:
            error_occured = True
        self.assertFalse(error_occured)
