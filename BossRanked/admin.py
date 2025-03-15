from django.contrib import admin
from . import models
from .models import Game, User, Review, Admin, Genre, ReviewAction

# Register your models here.
admin.site.register(Game)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(Admin)
admin.site.register(Genre)
admin.site.register(ReviewAction)