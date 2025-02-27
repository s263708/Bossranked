from django.shortcuts import render
from .models import Game

# Create your views here.
def home(request):
    game=Game.objects.all()
    context={'game':game}
    return render (request, 'index.html', context )
