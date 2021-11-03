from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import History, Bookmark


#translating models into other formats
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('id', 'historyLink')

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('id', 'bookmarkLink')
