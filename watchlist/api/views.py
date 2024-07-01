from django.shortcuts import render
from watchlist.models import Movie
from watchlist.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)  # Correct usage of many=True
        return Response(serializer.data)
    if request.method == 'POST':
        # Serialize the request
        serializer = MovieSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=404)
    if request.method == 'PUT':
        """ PUT -> updating every field. But patch is updating one field """
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204)

    
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
