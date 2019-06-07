from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

User = get_user_model()

# Posts = Post.objects.all()


class UserPostDetaileView(ListView):
    
    model = Post
    template_name = 'Posts/user_post_details.html'
    context_object_name = 'Posts'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(Auther=user).order_by('-Publish_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "User | Posts"
        return context

class HomePage(ListView):

    model = Post
    template_name = 'Posts/Home.html'
    context_object_name = 'Posts'
    ordering = ['-Publish_date']
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home | Posts"
        return context

class PostDetaileView(DetailView):

    model = Post
    template_name = 'Posts/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Detail | Posts'
        return context

class PostCreateView(LoginRequiredMixin, CreateView):

    model = Post
    fields = ['Title', 'Content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New | Posts"
        return context
    
    def form_valid(self, form):
        form.instance.Auther = self.request.user
        return super().form_valid(form)

class PostUpdaeView(LoginRequiredMixin, UpdateView):

    model = Post
    fields = ['Title', 'Content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Title | Posts"
        return context
    
    def test_func(self):
        post = self.get_object()
        if  self.request.user == post.Auther:
            return True
        return False

class PostDeliteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):

    model = Post
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete | Posts"
        return context

    def test_func(self):
        post = self.get_object()
        if  self.request.user == post.Auther:
            return True
        return False        