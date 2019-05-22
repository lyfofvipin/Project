from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class HomePage(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Home Page")