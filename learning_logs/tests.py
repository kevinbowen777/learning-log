from django.test import SimpleTestCase


class LearninLogsTests(SimpleTestCase):
    def test_homepage_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_topics_page_status_code(self):
        response = self.client.get("/topics/")
        self.assertEqual(response.status_code, 302)

    def test_login_page_status(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)

    def test_logout_page_status(self):
        response = self.client.get("/accounts/logout/")
        self.assertEqual(response.status_code, 200)

    def test_register_page_status(self):
        response = self.client.get("/accounts/register/")
        self.assertEqual(response.status_code, 200)
