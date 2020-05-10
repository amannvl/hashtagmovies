from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    #path("details/<int:id>/", views.details, name="details"),
    path("search/", views.search, name="search"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("advancesearch/", views.advancesearch, name="advancesearch"),
    path("moviepost/<str:movie_id>", views.moviepost, name="moviepost"),
    path("<str:cat>/", views.catwise, name="catwise"),

]
