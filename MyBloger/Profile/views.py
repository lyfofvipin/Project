from django.shortcuts import render
from django.views.generic import TemplateView

class Profile(TemplateView):

    template_name = 'Profile/Profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Profile | Post"
        return context
    