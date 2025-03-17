from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Game
# Create your views here.
def home(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def gamesearch(request):
    items = Game.objects.all()
    return render(request, "game_search.html", {"games": items})

@login_required
def gameview(request, id):
    game = get_object_or_404(Game, id=id)  # get the game or return an error
    return render(request, 'game_details.html', {'game': game})

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def loginview(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("game_search")  # redirect to the games page after login
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "login.html")

def registerview(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)  # auto-login after registration
            return redirect("game_search")  # redirect after successful registration

    return render(request, "register.html")


def deleteaccountview(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # user exists and credentials are correct, delete the user
            user.delete()
            messages.success(request, "Your account has been deleted.")
            return redirect("login")  # redirect to login page after deletion
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, "delete_account.html")

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import update_session_auth_hash

def updateaccountview(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate the user with the provided username and password
        user = authenticate(username=request.user.username, password=password)

        if user is not None:  # if the password is correct, update the db
            user.username = username
            user.save()  # save the changes to the database
            messages.success(request, "Your account has been updated successfully.")
            return redirect('update_account')  # redirect to the update account page
        else:
            messages.error(request, "Incorrect password. Please try again.")

    return render(request, 'update_account.html', {'user': request.user})

from django.contrib.auth import logout

def logoutview(request):
    logout(request)
    return redirect("login")  # redirect to login page
