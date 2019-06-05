from django.contrib import admin
from .models import Post
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()

class UserAdmin(UserAdmin):
    model = User

admin.site.register(Post)
admin.site.register(User, UserAdmin)