
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.forms import ValidationError
from parameterized import parameterized
from pytest import skip

from .test_jogos_base import GamesTestBase, Jogos


class GameModelTest(GamesTestBase):
    def setUp(self) -> None:
        self.game = self.make_game()
        return super().setUp()

    def make_game_no_defaults(self):
        game = Jogos(
            category=self.make_category(name='Test Default Category'),
            author=self.make_author(username='newuser'),
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time='time',
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation Steps',
        )
        game.full_clean()
        game.save()
        return game

    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 65),
        ('servings_unit', 65),
    ])
    def test_game_fields_max_length(self, field, max_length):
        setattr(self.game, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.game.full_clean()
    
 