from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Movie, History, Bookmark


#translating models into other formats

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'desc', 'year')

class MovieMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title')

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('id', 'historyLink')

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('id', 'bookmarkLink')
