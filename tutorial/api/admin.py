from django.contrib import admin
from .models import Movie
from .models import History
from .models import Bookmark

admin.site.register(Movie)
admin.site.register(History)
admin.site.register(Bookmark)