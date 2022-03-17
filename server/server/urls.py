"""server URL Configuration"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_resp)
]