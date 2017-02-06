from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """A webpage that lets user enter and submit a new topic."""
    class Meta:
        """Which model to base the form on and which fields included"""
        model = Topic
        fields = ['text']
        # Generate a label for the text field
        labels = {'text' : ''}

class EntryForm(forms.ModelForm):
    """A webpage that lets users enter and submit a new entry."""
    class Meta:
        """Which model to base the form on and which fields included."""
        model = Entry
        fields = ['text']
        labels = {'text' : ''}
        widgets = {'text' : forms.Textarea(attrs={'cols' : 80})}
