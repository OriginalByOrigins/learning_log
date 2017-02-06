from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning abourt"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """Return a string representation of the model (the Topic)."""
        # What to show when refering to the topic
        return self.text


class Entry(models.Model):
    """Somthing specific learned about a topic"""
    # Connect an entry to a topic using the topic's key(ID)
    topic = models.ForeignKey(Topic)

    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Additional information of an entry"""
        # Tell Bjango to use entries as entry's plural form(not entrys)
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model (the Entry)."""
        return self.text[:50] + '...'