from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class News(models.Model):

    class Status(models.TextChoices):
        draft = "DR", "Draft"
        published = "PT", "Published"
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.draft)

    class Meta:
        ordering = ['-publish_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single_page', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    message = models.TextField()
    def __str__(self):
        return self.name

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name = 'comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
