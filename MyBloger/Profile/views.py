from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Profile
from Posts.models import Post
from django.views.generic import ListView
from .forms import UserDetailUpdateForm, UserProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView

User = get_user_model()


class ProfileUpdaeView(LoginRequiredMixin, UpdateView):

    model = User
    form_class = UserProfileUpdateForm
    second_form_class = UserDetailUpdateForm
    template_name = "Profile/Profile.html"
    success_url = "/profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pro_form'] = self.second_form_class(self.request.POST or None, instance=self.object.user)
        context['title'] = 'Profile | Post'
        return context

    def form_valid(self, form):
        pro_form = UserDetailUpdateForm(self.request.POST, instance=self.object.user)
        if pro_form.is_valid():
            pro_form.save()
        return super().form_valid(form)

    def get_object(self):
        return self.request.user.profile