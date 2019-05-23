from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

class HomePage(TemplateView):

    template_name = 'Posts/Home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Home | Posts"
        return context