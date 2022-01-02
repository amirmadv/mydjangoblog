from types import BuiltinMethodType
from django.db import models
from django.db.models.fields import DateTimeField, SlugField

class Article(models.Model):
    title = models.CharField(max_length=100)
    Slug = models.SlugField()
    body = models.TextField()
    date =DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + ' ...'   
    