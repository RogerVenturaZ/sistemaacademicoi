from django.shortcuts import render,rendirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
# Create your views here.

class Index(View):
    def get(self , request, *args, ** kwargs):
        return render (request, 'index.html')
    def post(self, request):
        pass