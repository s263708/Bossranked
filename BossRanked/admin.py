from django.contrib import admin
from . import models
from .models import Game

# Register your models here.
admin.site.register(Game)