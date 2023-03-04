from django.urls import path, include  # NOQA
from . import views

urlpatterns = [path("", views.home, name="home")]
