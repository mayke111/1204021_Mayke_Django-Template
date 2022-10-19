from importlib.resources import path
from pathlib import PurePath
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    
    ]