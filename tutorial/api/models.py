from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=256)
    year = models.IntegerField()

class History(models.Model):
    historyLink = models.CharField(max_length=45)


class Bookmark(models.Model):
    bookmarkLink = models.CharField(max_length=45)

