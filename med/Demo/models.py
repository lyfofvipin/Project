from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Meds(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    qunt = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog-home')

class User_type(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_buyer = models.BooleanField(default=False)
    is_saler = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
