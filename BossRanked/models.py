from django.db import models

# Create your models here.
class Game (models.Model):
    game_ID = models.IntegerField(max_length=5, primary_key=True)
    game_name = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1020)
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.game_ID}, {self.game_name}, {self.genres}, {self.price}, {self.description}, {self.release_date}"

class User (models.Model):
    user_ID = models.IntegerField(max_length=5, primary_key=True)
    game_ID = models.ForeignKey(Game,on_delete=models.CASCADE, related_name="game_id")
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

class Reviews (models.Model):
    review_ID = models.IntegerField(max_length=5, primary_key=True)
    game_ID = models.ForeignKey(Game,on_delete=models.CASCADE, related_name="game_id")
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id")
    reviews = models.CharField(max_length=1020)
