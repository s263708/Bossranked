from django.db import models
from django.db.models import ForeignKey
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


# Create your models here.
class Genre(models.Model):
    genre_ID = models.IntegerField(primary_key=True)
    genre_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.genre_name} ({self.genre_ID})"


class Game(models.Model):
    game_ID = models.IntegerField(primary_key=True)
    game_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField(max_length=1020)
    release_date = models.DateTimeField(auto_now_add=True)
    genre_ID = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True)
    game_picture = models.ImageField(upload_to='game_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.game_name} ({self.game_ID})"


class User(models.Model):
    user_ID = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.username} ({self.user_ID})"


class Review(models.Model):
    review_ID = models.IntegerField(primary_key=True)
    game_ID = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True)
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    review_text = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def __str__(self):
        return f"Review by {self.user_ID} for {self.game_ID} ({self.rating})"


class Admin(models.Model):
    admin_ID = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return f"Admin: {self.username} ({self.admin_ID})"


class ReviewAction(models.Model):
    action_ID = models.IntegerField(primary_key=True)
    admin_ID = models.ForeignKey(Admin, on_delete=models.CASCADE)
    review_ID = models.ForeignKey(Review, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=64)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Action by {self.admin_ID} on review {self.review_ID} ({self.action_type})"