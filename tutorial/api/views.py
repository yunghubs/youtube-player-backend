from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import HistorySerializer, BookmarkSerializer
from .models import History, Bookmark
from rest_framework.response import Response


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
