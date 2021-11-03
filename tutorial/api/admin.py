from django.contrib import admin
from .models import History
from .models import Bookmark

admin.site.register(History)
admin.site.register(Bookmark)