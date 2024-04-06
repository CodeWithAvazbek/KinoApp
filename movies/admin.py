from django.contrib import admin
from .models import Genre, Movie


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Movie)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'release_year', 'date_created']
