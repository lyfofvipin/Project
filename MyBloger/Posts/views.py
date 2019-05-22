from django.shortcuts import render
from django.http import HttpResponse
from django.views import Views

class HomePage(View):

    def get(self, request, *args, **kwargs):
        context = {'Helloworld':"Hellow world!","Title":"Title"}
        return HttpResponse(context)