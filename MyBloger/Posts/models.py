from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    
    email = models.EmailField()
    pet_name = models.CharField(default='Not have any pet', max_length=50)

class Post(models.Model):

    Title = models.CharField(default='Title Of Post', max_length=50)
    Content = models.TextField()
    Publish_date = models.DateTimeField(auto_now_add=True)
    Last_updated = models.DateTimeField(auto_now=True)
    Auther = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
            