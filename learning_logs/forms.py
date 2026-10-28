from typing import ClassVar

from django import forms

from .models import Entry, Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields: ClassVar[list[str]] = ["text"]
        labels: ClassVar[dict[str, str]] = {"text": ""}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields: ClassVar[list[str]] = ["text"]
        labels: ClassVar[dict[str, str]] = {"text": "Entry:"}
        widgets: ClassVar[dict[str, str]] = {"text": forms.Textarea(attrs={"cols": 40})}
