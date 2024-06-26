from django.shortcuts import render, get_object_or_404
from .models import Genre, Movie
from django.http import Http404


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    # try:
    #     movie = Movie.objects.get(pk=movie_id)
    #     return render(request, 'movies/datail.html', {'movie': movie})
    # except Movie.DoesNotExist:
    #     raise Http404()
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/datail.html', {'movie': movie})