from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("game_search/", views.gamesearch, name="game_search"),
    path("login/", views.loginview, name="login"),
    path('register/', views.registerview, name='register'),
    path('game_details/<int:game_id>/', views.gameview, name='game_details'),
    path('logout/', views.logoutview, name='logout'),
    path('delete_account/', views.deleteaccountview, name='delete_account'),
    path('update_account/', views.updateaccountview, name='update_account'),
    ]

