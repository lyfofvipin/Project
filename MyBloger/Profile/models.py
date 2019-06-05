from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Profile_pic = models.ImageField(default='default.jpg', upload_to='ProfilePics')

    def  __str__(self):
        return self.user.username

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.Profile_pic.path)

    #     if img.height > 300 and img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.Profile_pic.path)