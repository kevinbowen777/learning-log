from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from ..models import Entry, Topic  # noqa:F401
from ..views import topic, topics  # noqa:F401


class TopicPageViewTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="kevin",
            email="kevin@example.com",
            password="secret",
        )

        self.topic = Topic.objects.create(
            text="A Topic title",
            owner=self.user,
        )

        self.entry = Topic.objects.create(
            # topic = self.entry.topic,
            text="Entry text",
            owner=self.user,
        )

    def test_topic_content(self):
        self.assertEqual(f"{self.topic.text}", "A Topic title")
        self.assertEqual(f"{self.topic.owner}", "kevin")

    def test___str__(self):
        assert self.topic.__str__() == self.topic.text
        assert str(self.topic) == self.topic.text

    def test_topic_create_view(self):
        self.client.login(email="kevin@example.com", password="secret")
        response = self.client.post(
            reverse("new_topic"),
            {
                "text": "This is a new topic",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Topic.objects.last().text, "This is a new topic")
        self.assertEqual(Topic.objects.first().text, "A Topic title")
        self.assertTemplateUsed("learning_logs/new_topic.html")
        # self.assertEqual(Article.objects.last().body, "Nice body content")

    def test_topic_list_single(self):
        self.client.login(email="kevin@example.com", password="secret")
        response = self.client.get(
            reverse("topic", args={self.topic.id}),
            # reverse("topic"),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Topic.objects.first().text, "A Topic title")
        self.assertTemplateUsed("learning_logs/topic.html")

    def test_topics_list_page(self):
        self.client.login(email="kevin@example.com", password="secret")
        response = self.client.get(
            # reverse("topics", args={self.topic.id}),
            reverse("topics"),
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("learning_logs/topics.html")
        # self.assertEqual(Topic.objects.first().text, "A Topic title")

    def test_create_new_entry(self):
        self.client.login(email="kevin@example.com", password="secret")
        response = self.client.post(
            reverse("new_entry", args={self.topic.id}),
            {
                "text": "This is a new entry",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed("learning_logs/new_entry.html")

    """
    def test_create_new_entry(self):
        self.client.login(email="kevin@example.com", password="secret")
        response = self.client.post(
            reverse("edit_entry", args={self.entry.id}),
            {
                "text": "This is an edited entry",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed("learning_logs/edit_entry.html")
    """
