from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def games(request):
    return render(request, 'games.html')
def login_view(request):
    return render(request, 'login.html')

from .models import Game
# Create your views here.
def home(request):
    game=Game.objects.all()
    context={'game':game}
    return render (request, 'games.html', context )

from .models import Game

def games_view(request):
    games = Game.objects.all()  # Fetch all games from the database
    context = {
        'games': games,  # Pass the games to the template context
    }
    return render(request, 'games.html', context)  # Render the template with the context
