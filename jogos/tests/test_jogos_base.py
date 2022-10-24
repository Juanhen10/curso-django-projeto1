from unicodedata import category, name
from urllib import response
from venv import create

from django.test import TestCase
from jogos.models import Category, Jogos, User


class GamesTestBase(TestCase):
    def setUp(self) -> None:
        self.make_games()
        return super().setUp()

    def make_category(self, name='Category'):
        return  Category.object.create(name=name)

    def make_author(
        self,
        first_name='lais',
        last_name='ferreira',
        username='laisF',
        password='12356',
        email='laisferreira@gmail.com',):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,)

    def make_games(
        Self, 
        category_data = None,
        author_data = None,
        title = 'Games Title',
        description = 'Games Description' ,
        slug = 'games-slug',
        game_mode = 10,
        preparation_time_unit ='Minutos' ,
        servings = 5,
        servings_unit = 'Porções',
        preparation_steps = 'games preparation Steps',
        preparation_steps_is_html = False,
        is_published = True ,
        ):

        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Jogos.objects.create(
            category =self.make_category(**category_data),
            author =self.make_author(**author_data),
            title = title,
            description = description ,
            slug = slug,
            game_mode = game_mode,
            preparation_time_unit =preparation_time_unit ,
            servings = servings,
            servings_unit = servings_unit,
            preparation_steps = preparation_steps,
            preparation_steps_is_html = preparation_steps_is_html,
            is_published = is_published ,
        )
        
