from django.shortcuts import render, redirect
from .myforms import MovieForm, FilterForm
from .models import MoviesDB
from .botlib import getmovies

filtered = None


def index(req):
    return render(req, 'index.html',
                  context={'form': MovieForm(), 'filterform': FilterForm(), 'filtered': filtered})


def add1(req):
    if req.POST:
        movie = MoviesDB()
        m = MoviesDB.objects.all()
        movie.id = m[len(m) - 1].id + 1
        movie.title = req.POST.get('title')
        movie.country = req.POST.get('country')
        movie.year = req.POST.get('year')
        movie.save()
        return redirect('index')


def dbfilter(req):
    query_f = {}
    query_e = {}
    global filtered
    if req.POST:
        tipe_c_filter = req.POST.get('tipe_c_filter')
        country_data = req.POST.get('country_data')
        tipe_y_filter = req.POST.get('tipe_y_filter')
        year_data = req.POST.get('year_data')
        if country_data:
            if tipe_c_filter:
                query_e.update({'country': country_data})
            else:
                query_f.update({'country': country_data})
        if year_data:
            if tipe_y_filter:
                query_e.update({'year': year_data})
            else:
                query_f.update({'year': year_data})
    filtered = MoviesDB.objects.filter(**query_f).exclude(**query_e)
    return redirect('index')


def kinopoisk(req):
    global filtered
    movies_list = getmovies()
    for i, m in enumerate(movies_list):
        movie = MoviesDB()
        movie.id = i + 1
        movie.title = m['title']
        movie.country = m['country']
        movie.year = m['year']
        movie.save()
    filtered = MoviesDB.objects.all()
    return redirect('index')
