import uuid
from django.db import models


class Note(models.Model):
    content = models.TextField()

    def __unicode__(self):
        return self.content


class Post(models.Model):
    uuid = models.CharField(max_length=16, default=uuid.uuid4, primary_key=True)
    content = models.TextField()

    def __unicode__(self):
        return self.content
