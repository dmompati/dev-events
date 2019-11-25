from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    venue = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_time = models.CharField(max_length=200)
    end_time =  models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    short_description = models.CharField(max_length=100)
    event_description = models.TextField(max_length=600)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    event_image = models.ImageField(upload_to = 'event_pics/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.event_image.path)

        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.event_image.path)

