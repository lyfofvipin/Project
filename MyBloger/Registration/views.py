from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages

# class Register(CreateView):
    
#     model = User
#     form_class = UserRegistrationForm
#     template_name = 'Registration/Register.html'
#     success_url = 'Home'

#     def form_valid(self, form):
#         return super().form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = 'Register | User'
#         return context

def Register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            creater = form.cleaned_data.get('username')
            messages.sucess(request, f'Account Created for {creater}.')
            return redirect('Home')
    else:
        form = UserRegistrationForm()
    context = {'title':"Register | Posts", 'form':form}
    return render(request, 'Registration/Register.html', context)