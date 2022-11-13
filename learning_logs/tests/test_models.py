from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Entry, Topic


class TopicModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="kevin",
            email="kevin@example.com",
            password="T3stP@5s123",
        )
        self.topic = Topic.objects.create(owner=self.user, text="just a test")
        self.entry = Entry.objects.create(topic=self.topic, text="Entry text")
        self.long_entry = Entry.objects.create(
            topic=self.topic,
            text="This is a long Entry text that should be concatenated.",
        )

    """
    def test_topic_content(self):
        topic = Topic.objects.get(id=1)
        self.text = f"{topic.text}"
        self.assertEqual(self.text, "just a test")
    """

    def test_topic___str__(self):
        self.assertEqual(str(self.topic), self.topic.text)

    def test_topic_get_absolute_url(self):
        assert self.topic.get_absolute_url() == f"/topics/{self.topic.id}/"

    """
    def test_entry_content(self):
        entry = Entry.objects.get(id=1)
        self.text = f"{entry.text}"
        self.assertEqual(self.text, "Entry text")
    """

    def test_entry__str__(self):
        if len(self.entry.text[:]) < 50:
            self.assertEqual(str(self.entry), self.entry.text)
        else:
            self.assertEqual(str(self.entry), f"{self.entry.text[:50]} ... ")

    def test_long_entry__str__(self):
        if len(self.long_entry.text[:]) < 50:
            self.assertEqual(str(self.long_entry), self.long_entry.text)
        else:
            self.assertEqual(
                str(self.long_entry), f"{self.long_entry.text[:50]}..."
            )
