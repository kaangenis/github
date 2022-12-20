from django.urls import path
from . import views

#http://127.0.0.1:8000/
#http://127.0.0.1:8000/home
#http://127.0.0.1:8000/movies
#http://127.0.0.1:8000/3
#http://127.0.0.1:8000/walking-dead



urlpatterns = [

    path("", views.home),
    path("home", views.home),
    path("moviepage", views.moviepage)




]