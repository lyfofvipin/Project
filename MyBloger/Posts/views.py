from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView


Posts = [
    {
    "Title" : "First Post Title",
    "Content" : "First post content !",
    "Publish_date" : "Published date time",
    "Last_updated" : "Last Update time",
    "Auther" : "Auther of the post"
    }
]

class HomePage(TemplateView):

    template_name = 'Posts/Home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home | Posts"
        context["Posts"] = Posts
        return context