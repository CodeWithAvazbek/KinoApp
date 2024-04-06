from django.urls import path
from .views import index, detail


urlpatterns = [
    path('', index, name="movies_index"),
    path('<int:movie_id>/', detail, name='movies_detail'),
]