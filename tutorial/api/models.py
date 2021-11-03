from django.db import models


class History(models.Model):
    historyLink = models.CharField(max_length=45)


class Bookmark(models.Model):
    bookmarkLink = models.CharField(max_length=45)

