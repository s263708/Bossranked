from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Game
from decimal import Decimal

class BossRankedTestCase(TestCase):
    def setUp(self):
        """create test user and sample game data"""
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.game = Game.objects.create(
            game_name="Elden Ring",
            price=Decimal("49.99"),  # ensure price is stored as decimal rather than float
        )

    def test_game_creation(self):
        """test for saved game"""
        game = Game.objects.get(game_name="Elden Ring")
        self.assertEqual(game.price, Decimal("49.99"))

    def test_game_list_view(self):
        """ensure game list page loads"""
        response = self.client.get(reverse("game_search"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Elden Ring")

    def test_login_user(self):
        """ensure a user can log in to their account"""
        login = self.client.login(username="testuser", password="password123")
        self.assertTrue(login)