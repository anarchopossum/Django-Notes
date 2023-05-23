from django.urls import path

from . import views

urlpatterns = [
    # We change this first line to incorporate the class Home instead
    path('home', views.HomeView.as_view()),
    path('authorized', views.AuthorizedView.as_view())
]