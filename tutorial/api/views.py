from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MovieSerializer, MovieMiniSerializer, HistorySerializer, BookmarkSerializer
from .models import Movie, History, Bookmark
from rest_framework.response import Response

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    #build-in method in django, overwrite the django with our own
    def list(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieMiniSerializer(movies, many=True)
        return Response(serializer.data)

class HistoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = History.objects.all()
    serializer_class = HistorySerializer


class BookmarkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
