from django.test import TestCase


class LearningLogsTests(TestCase):
    def test_topics_page_status_code(self):
        response = self.client.get("/topics/")
        self.assertEqual(response.status_code, 302)

    def test_new_topic_page_status_code(self):
        response = self.client.get("/new_topic/")
        self.assertEqual(response.status_code, 302)
