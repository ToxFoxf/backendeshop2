from . import views
from django.urls import path

urlpatterns =[
    path("hi/", views.hi)
]