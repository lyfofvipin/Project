from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    pass

class Post(models.Model):

    Auther = models.CharField(max_length=50)
    Content = models.CharField(max_length=1000)
    Publish_date = models.DateTimeField('pubdate')