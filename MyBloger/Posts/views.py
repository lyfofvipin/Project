from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

Posts = Post.objects.all()

class HomePage(ListView):

    model = Post
    template_name = 'Posts/Home.html'
    context_object_name = 'Posts'
    ordering = ['-Publish_date']

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

class PostUpdaeView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

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

def PostDeliteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete | Posts"
        return context