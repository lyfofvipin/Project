from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from .models import Post

Posts = Post.objects.all()

class HomePage(TemplateView):

    template_name = 'Posts/Home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home | Posts"
        context["Posts"] = Posts
        return context