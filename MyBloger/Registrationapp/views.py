from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from .forms import RegistrationForm

User = get_user_model()

class Registration(SuccessMessageMixin, CreateView):
    
    model = User
    form_class = RegistrationForm
    template_name = 'Registrationapp/Register.html'
    success_url = '/'
    success_message = '%(username)s Account is created.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Register | Posts'
        return context
    