from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Profile_pic = models.ImageField(default='default.jpg', upload_to='ProfilePics')

    def  __str__(self):
        return self.user.username