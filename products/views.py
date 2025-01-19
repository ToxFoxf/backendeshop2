from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def hi(request):
   return HttpResponse("hi")
    