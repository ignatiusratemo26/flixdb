from django.shortcuts import render
from watchlist.models import Movie
from django.http import JsonResponse

def movie_list(request):
    # to get all the objects in the movies model
    movies = Movie.objects.all()
    data = {'movies': list(movies.values())}
    return JsonResponse(data)

# to fetch data for a specific movie
def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    print(movie.name)
    data = {'name': movie.name,
            'description': movie.desc,
            'active': movie.active}
    return JsonResponse(data)
