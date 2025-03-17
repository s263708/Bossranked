from django.contrib import admin
from .models import Genre, Game, User, Review

# Register your models here.
admin.site.register(Genre)
admin.site.register(Game)
admin.site.register(User)
admin.site.register(Review)