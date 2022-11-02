from unicodedata import category, name
from urllib import response
from venv import create

from django.test import TestCase
from jogos.models import Category, Jogos, User


class GamesTestBase(TestCase):
    def setUp(self) -> None:
        self.make_game()
        return super().setUp()

    def make_category(self, name='Category'):
        return Category.objects.create(name=name)

    def make_author(
        self,
        first_name = 'user',
        last_name ='name',
        username = 'username',
        password = '123456',
        email='username@gmail.com',
    ):
        return User(
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password,
            email= email,
        )


    def make_game(
        self, 
        category_data = None,
        author_data = None,
        title = 'Games Title',
        description = 'Games Description' ,
        slug = 'games-slug',
        game_mode = 'game_mode',
        preparation_time_unit =5 ,
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

        return Jogos(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            game_mode= game_mode,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,)
        
        
      
