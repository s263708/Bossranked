from django.db import models

# Create your models here.
class Game (models.Model):
    game_ID = models.IntegerField(max_length=5)
    game_name = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=255)
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name