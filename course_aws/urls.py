from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cpu-usage", views.cpu_usage, name="cpu_usage"),
    path("cpu-load", views.cpu_load, name="cpu_load"),
    path("process", views.process, name="process"),
]
