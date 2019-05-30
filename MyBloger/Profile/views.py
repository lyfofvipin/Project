from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Profile
from .forms import UserDetailUpdateForm, UserProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView

User = get_user_model()


class Profile(LoginRequiredMixin, UpdateView):

    model = User
    form_class = UserDetailUpdateForm
    second_form_class = UserProfileUpdateForm
    template_name = "Profile/Profile.html"
    success_url = "/profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pro_form'] = self.second_form_class(self.request.POST, instance=self.object.user.profile)
        context['title'] = 'Profile | Post'
        return context

    def form_valid(self, form):
        pro_form = UserProfileUpdateForm(self.request.POST, instance=self.object.user.profile)
        if pro_form.is_valid(form):
            pro_form.save()
        return super().form_valid()

    def get_object(self):
        return self.request.user.profile