from django.db import models
from django.utils import timezone
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
    slug = models.SlugField(max_length=250)
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

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    message = models.TextField()
    def __str__(self):
        return self.name