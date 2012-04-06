from haystack import indexes, __version__ as haystack_version
from .models import Note, Post

from celery_haystack.indexes import CelerySearchIndex

if haystack_version[:2] < (2, 0):
    from haystack import site
    class Indexable(object):
        pass
    indexes.Indexable = Indexable
else:
    site = None


class NoteIndex(CelerySearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='content')

    def get_model(self):
        return Note


class PostIndex(CelerySearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='content')

    def get_model(self):
        return Post


if site:
    site.register(Note, NoteIndex)
    site.register(Post, PostIndex)
