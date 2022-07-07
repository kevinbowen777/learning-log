from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse  # noqa:F401

from ..models import Entry, Topic  # noqa:F401
from ..views import topic, topics  # noqa:F401


class TopicsPageViewTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="kevin",
            email="kevin@example.com",
            password="T3stP@5s123",
        )

        self.topic = Topic.objects.create(
            text="A Topic title",
            owner=self.user,
        )

        self.entry = Topic.objects.create(
            text="Entry text",
            owner=self.user,
        )

    def test_topic_content(self):
        self.assertEqual(f"{self.topic.text}", "A Topic title")
        self.assertEqual(f"{self.topic.owner}", "kevin")
