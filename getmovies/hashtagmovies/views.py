from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from math import ceil
# import requests
from .models import Movies,Contact
from imdb import IMDb
import csv


def index(request):
    ia = IMDb()
    temp = 0
    posts = Movies.objects.all().order_by('-p_id')[0:30]
    # relatedPosts = Movies.objects.filter(genres__icontains=post.genres).order_by('-p_id')[0:3]
    # latestPosts = Movies.objects.all().order_by('-p_id')[0:3]
    context = {'posts': posts}
    return render(request, 'hashtagmovies/index.html', context)

def contact(request):
    messages.success(request, 'Welcome to contact')
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, desc=desc)
            contact.save()
            messages.success(request, "Your message has been delivered")
    return render(request, 'hashtagmovies/contact.html')


def about(request):
    return render(request, 'hashtagmovies/about.html')





def search(request):
    query = request.GET['query']
    ia = IMDb()
    allPosts = []
    if not Movies.objects.filter(title__icontains=query).exists():
        dataset2 = ia.search_movie((str(query)))
        # print(dataset)
        for i in dataset2:
            # print(i.movieID)
            dataset = ia.get_movie(i.movieID)
            cast_t = ''
            genres_t = ''
            runtimes_t = ''
            countries_t = ''
            language_codes_t = ''
            certificates_t = ''
            languages_t = ''
            director_t = ''
            plot_t = ''
            if dataset.get('cast', None):
                for j in dataset['cast']:
                    cast_t = cast_t + str(j) + ","
            else:
                cast_t = '/NA'
            if dataset.get('genres', None):
                for j in dataset.get('genres', None):
                    genres_t = genres_t + str(j) + " "
            else:
                genres_t = '/NA'
            if dataset.get('runtimes', None):
                for j in dataset.get('runtimes', None):
                    runtimes_t = runtimes_t + str(j) + ","
            else:
                runtimes_t = '/NA'
            if dataset.get('countries', None):
                for j in dataset.get('countries', None):
                    countries_t = countries_t + str(j) + ","
            else:
                countries_t = '/NA'
            if dataset.get('language codes', None):
                for j in dataset.get('language codes', None):
                    language_codes_t = language_codes_t + str(j) + ","
            else:
                language_codes_t = '/NA'
            if dataset.get('certificates', None):
                for j in dataset.get('certificates', None):
                    certificates_t = certificates_t + str(j) + ","
            else:
                certificates_t = '/NA'
            if dataset.get('languages', None):
                for j in dataset.get('languages', None):
                    languages_t = languages_t + str(j) + ","
            else:
                languages_t = '/NA'
            if dataset.get('directors', None):
                for j in dataset.get('directors', None):
                    director_t = director_t + str(j) + ","
            else:
                director_t = '/NA'
            if dataset.get('plot', None):
                for j in dataset.get('plot', None):
                    plot_t = plot_t + str(j) + "."
            else:
                plot_t = '/NA'

            if not Movies.objects.filter(title=dataset.get('title', None)).exists():
                Movies(cast=cast_t,
                       movie_id=i.movieID,
                       genres=genres_t,
                       runtimes=runtimes_t,
                       countries=countries_t,
                       language_codes=language_codes_t,
                       aspect_ratio=dataset.get('aspect ratio', None),
                       box_office=dataset.get('box office', None),
                       certificates=certificates_t,
                       air_date=dataset.get('original air date', None),
                       rating=dataset.get('rating', None),
                       votes=dataset.get('votes', None),
                       cover_url=dataset.get('cover url', None),
                       plot_outline=dataset.get('plot outline', None),
                       languages=languages_t,
                       title=dataset.get('title', None),
                       year=dataset.get('year', None),
                       director=director_t,
                       plot=plot_t,
                       long_imdb_title=dataset.get('long imdb title', None),
                       full_size_cover_url=dataset.get('full-size cover url', None)
                       ).save()

            allPosts = (Movies.objects.filter(title__icontains=query).order_by('-p_id'))
            # print(allPosts)
            params = {'allPosts': allPosts}
    else:
        allPosts = (Movies.objects.filter(title__icontains=query).order_by('-p_id'))
        params = {'allPosts': allPosts}
    return render(request, 'hashtagmovies/search.html', params)


def advancesearch(request):
    query = request.GET['adquery']
    ia = IMDb()
    allPosts = []
    dataset2 = ia.search_movie((str(query)))
        # print(dataset)
    for i in dataset2:
        # print(i.movieID)
        dataset = ia.get_movie(i.movieID)
        cast_t = ''
        genres_t = ''
        runtimes_t = ''
        countries_t = ''
        language_codes_t = ''
        certificates_t = ''
        languages_t = ''
        director_t = ''
        plot_t = ''
        if dataset.get('cast', None):
            for j in dataset['cast']:
                cast_t = cast_t + str(j) + ","
        else:
            cast_t = '/NA'
        if dataset.get('genres', None):
            for j in dataset.get('genres', None):
                genres_t = genres_t + str(j) + " "
        else:
            genres_t = '/NA'
        if dataset.get('runtimes', None):
            for j in dataset.get('runtimes', None):
                runtimes_t = runtimes_t + str(j) + ","
        else:
            runtimes_t = '/NA'
        if dataset.get('countries', None):
            for j in dataset.get('countries', None):
                countries_t = countries_t + str(j) + ","
        else:
            countries_t = '/NA'
        if dataset.get('language codes', None):
            for j in dataset.get('language codes', None):
                language_codes_t = language_codes_t + str(j) + ","
        else:
            language_codes_t = '/NA'
        if dataset.get('certificates', None):
            for j in dataset.get('certificates', None):
                certificates_t = certificates_t + str(j) + ","
        else:
            certificates_t = '/NA'
        if dataset.get('languages', None):
            for j in dataset.get('languages', None):
                languages_t = languages_t + str(j) + ","
        else:
            languages_t = '/NA'
        if dataset.get('directors', None):
            for j in dataset.get('directors', None):
                director_t = director_t + str(j) + ","
            else:
                director_t = '/NA'
        if dataset.get('plot', None):
            for j in dataset.get('plot', None):
                plot_t = plot_t + str(j) + "."
        else:
            plot_t = '/NA'

        if not Movies.objects.filter(title=dataset.get('title', None)).exists():
                Movies(cast=cast_t,
                       movie_id=i.movieID,
                       genres=genres_t,
                       runtimes=runtimes_t,
                       countries=countries_t,
                       language_codes=language_codes_t,
                       aspect_ratio=dataset.get('aspect ratio', None),
                       box_office=dataset.get('box office', None),
                       certificates=certificates_t,
                       air_date=dataset.get('original air date', None),
                       rating=dataset.get('rating', None),
                       votes=dataset.get('votes', None),
                       cover_url=dataset.get('cover url', None),
                       plot_outline=dataset.get('plot outline', None),
                       languages=languages_t,
                       title=dataset.get('title', None),
                       year=dataset.get('year', None),
                       director=director_t,
                       plot=plot_t,
                       long_imdb_title=dataset.get('long imdb title', None),
                       full_size_cover_url=dataset.get('full-size cover url', None)
                       ).save()

        allPosts = (Movies.objects.filter(title__icontains=query).order_by('-p_id'))
            # print(allPosts)
        params = {'allPosts': allPosts}

    return render(request, 'hashtagmovies/search.html', params)

def moviepost(request, movie_id):
    post = (Movies.objects.filter(movie_id=movie_id).first())
    relatedPosts = Movies.objects.filter(genres__icontains=post.genres).order_by('-p_id')[0:3]
    latestPosts = Movies.objects.all().order_by('-p_id')[0:3]
    context = {'post': post, 'relatedPosts': relatedPosts, 'latestPosts': latestPosts}
    return render(request, 'hashtagmovies/moviepost.html', context)


def catwise(request, cat):
    catPosts = Movies.objects.filter(genres__icontains=cat).order_by('-p_id')
    context = {'catPosts': catPosts, 'cat': cat.upper()}
    return render(request, 'hashtagmovies/catwise.html', context)

#
# ['cast', 'genres', 'runtimes', 'countries', 'country codes', 'language codes', 'color info', 'aspect ratio',
#  'sound mix', 'box office', 'certificates', 'original air date', 'rating', 'votes', 'cover url', 'plot outline',
#  'languages', 'title', 'year', 'kind', 'directors', 'writers', 'producers', 'composers', 'cinematographers', 'editors',
#  'editorial department', 'casting directors', 'production designers', 'art directors', 'set decorators',
#  'costume designers', 'make up department', 'production managers', 'assistant directors', 'art department',
#  'sound department', 'special effects', 'visual effects', 'stunts', 'camera department', 'animation department',
#  'casting department', 'costume departmen', 'location management', 'music department', 'script department',
#  'transportation department', 'miscellaneous', 'thanks', 'akas', 'writer', 'director', 'production companies',
#  'distributors', 'special effects companies', 'other companies', 'plot', 'synopsis', 'canonical title',
#  'long imdb title', 'long imdb canonical title', 'smart canonical title', 'smart long imdb canonical title',
#  'full-size cover url']
