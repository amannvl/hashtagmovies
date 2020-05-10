from datetime import datetime
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.forms import DateField
from time import gmtime, strftime

#
# class Movies(models.Model):
#     imdbId = models.CharField(max_length=50)
#     titleType = models.CharField(max_length=150)
#     primaryTitle = models.CharField(max_length=350, default="")
#     originalTitle = models.CharField(max_length=350, default="")
#     isAdult = models.CharField(max_length=80, default="")
#     startYear = models.CharField(max_length=50, default="")
#     endYear = models.CharField(null=True, max_length=20, blank=True, default="")
#     runtimeMinutes = models.CharField(max_length=100, default="")
#     genres = models.CharField(max_length=500, default="")
#     averageRating = models.CharField(max_length=50, default="")
#     cover_url = models.URLField(null=True, blank=True, default="")
#     plot = models.TextField(default="")
#
#
#
#
#     def __str__(self):
#         return self.imdbId
#
#
# class Moviedata(models.Model):
#     imdb_id = models.CharField(max_length=100)
#     isAdult = models.CharField(max_length=80, default="")
#     cast = models.TextField(default="")
#     genres = models.CharField(max_length=120, default="")
#     runtimes = models.CharField(max_length=50, default="")
#     countries = models.CharField(max_length=200, default="")
#     box_office = models.CharField(max_length=350, default="")
#     certificates = models.TextField(default="")
#     air_date = models.CharField(max_length=120, default="")
#     rating = models.CharField(max_length=100, default="")
#     cover_url = models.URLField(null=True, blank=True, default="")
#     plot_outline = models.TextField(null=True, default="")
#     languages = models.CharField(max_length=250, default="")
#     title = models.CharField(max_length=500, default="")
#     year = models.CharField(max_length=350, default="")
#     director = models.CharField(max_length=1000, default="")
#     plot = models.TextField(default="")
#     full_size_cover_url = models.URLField(null=True, blank=True, default="")
#
#     def __str__(self):
#         return self.imdb_id
#
# #
# # #
# #
# # class Bollywood(models.Model):
# #     title_x = models.CharField(max_length=200, default="")
# #     imdb_id = models.CharField(max_length=100)
# #     poster_path = models.URLField(null=True, blank=True, default="")
# #     wiki_link = models.URLField(null=True, blank=True, default="")
# #     title_y = models.CharField(max_length=200, default="")
# #     original_title = models.CharField(max_length=200, default="")
# #     is_adult = models.IntegerField(default="")
# #     movie_year_of_release = models.CharField(max_length=10, default=0)
# #     time = models.CharField(max_length=15, default="")
# #     genres = models.CharField(max_length=120, default="")
# #     imdb_rating = models.CharField(max_length=100, default="")
# #     imdb_votings = models.CharField(max_length=15, default="")
# #     story = models.TextField(default="")
# #     summary = models.TextField(default="")
# #     tagline = models.TextField(default="")
# #     actors = models.CharField(max_length=500, default="")
# #     wins_nominations = models.CharField(max_length=120, default="")
# #     release_date = models.CharField(max_length=100, default="")
# #
# #     def __str__(self):
# #         return self.imdb_id
# #
# # #

# #
# class List(models.Model):
#     imdb_id = models.CharField(max_length=100)
#     color = models.CharField(max_length=100)
#     director_name = models.CharField(max_length=250)
#     cast = models.CharField(max_length=800,default="")
#     genres = models.CharField(max_length=500,default="")
#     runtime = models.CharField(max_length=150, default="")
#     title = models.CharField(max_length=450, default="")
#     plot_keywords = models.CharField(max_length=550, default="")
#     release_date = models.CharField(max_length=200, default="")
#     language = models.CharField(max_length=200, default="")
#     country = models.CharField(max_length=200, default="")
#     poster_path = models.URLField(null=True, blank=True, default="")
#     tagline = models.TextField(default="")
#     gross = models.CharField(max_length=200, default="")
#     budget = models.CharField(max_length=200, default="")
#     plot = models.TextField(default="")
#
#     def __str__(self):
#         return self.title

class Movies(models.Model):
    p_id = models.AutoField(primary_key=True)
    movie_id = models.CharField(max_length=20)
    cast = models.TextField(null=True,default="")
    genres = models.CharField(null=True,max_length=120, default="")
    runtimes = models.CharField(null=True,max_length=50, default="")
    countries = models.CharField(null=True,max_length=200, default="")
    language_codes = models.CharField(null=True,max_length=125, default="")
    aspect_ratio = models.CharField(null=True,max_length=350, default="")
    box_office = models.CharField(null=True,max_length=350, default="")
    certificates = models.TextField(null=True,default="")
    # release_date = models.CharField(max_length=120,default="")
    air_date = models.CharField(null=True,max_length=120, default="")
    rating = models.CharField(null=True,max_length=100, default="")
    votes = models.CharField(null=True,max_length=15, default="")
    cover_url = models.URLField(null=True, blank=True, default="")
    plot_outline = models.TextField(null=True,default="")
    languages = models.CharField(null=True,max_length=100, default="")
    title = models.CharField(max_length=250, default="")
    year = models.CharField(null=True,max_length=350, default="")
    director = models.CharField(null=True,max_length=500, default="")
    # writer = models.CharField(max_length=500, default="")
    # producers = models.CharField(max_length=500, default="")
    plot = models.TextField(null=True,default="")
    long_imdb_title = models.CharField(max_length=300, default="")
    full_size_cover_url = models.URLField(null=True, blank=True, default="")

    def __str__(self):
        return self.movie_id

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name


