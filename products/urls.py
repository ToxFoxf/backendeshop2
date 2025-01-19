from . import views
from django.urls import path

urlpatterns =[
    path("http://localhost:3000/hi", views.hi)
]