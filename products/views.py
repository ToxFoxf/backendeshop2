from django.shortcuts import render
from django.http import JsonResponse
from .models import Product


def hi(request):
   return JsonResponse({"message": "hi"}, safe=False)
    