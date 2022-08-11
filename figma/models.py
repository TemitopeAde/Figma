from sqlite3 import Timestamp
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class SourceModel(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField()
    description = models.TextField()
    link = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Stories (models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    created_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='stories_posts', blank=True, null=True)
    # source = models.CharField(max_length=100, default="The Economist")
    source = models.ForeignKey(to=SourceModel, on_delete=models.CASCADE)


    class Meta:
        ordering = ['-created_on']

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Hashes(models.Model):
    title = models.CharField(max_length=100)
    # created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('hashed-detail', kwargs={'slug': self.slug})
