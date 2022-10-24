from unicodedata import name
from unittest import skip
from urllib import response

from django.urls import resolve, reverse
from jogos import views
from jogos.models import Category, Jogos, User

from .test_jogos_base import GamesTestBase


class JogosViewsTest(GamesTestBase):
        def test_jogos_home_view_function_is_correct(self):
            view = resolve('/')
            self.assertIs(view.func, views.home)

        def test_jogo_home_view_returns_status_code_200_ok(self):
            response = self.client.get(reverse("jogos:home"))
            self.assertEqual(response.status_code, 200)

        def test_jogo_home_view_loads_correct_template(self):
            response = self.client.get(reverse("jogos:home"))
            self.assertTemplateUsed(response,'jogos/pages/home.html')

        def test_jogos_home_no_games_found_if_no_games(self):
            response = self.client.get(reverse('jogos:home'))
            self.assertIn(
                'NO GAMES FOUND HERE',
                response.content.decode('utf-8'))

        
            

        def test_jogos_home_template_loads_games(self):
            self.make_games()
            response = self.client.get(reverse('jogos:home'))
            content = response.content.decode('utf-8'),
            
            self.assertIn('Games Title', content)
            self.assertEqual(len(response_context_games), 1)

        def test_jogos_category_template_loads_games(self):
            needed_title= "this is  a category test"
            self.make_games(title= needed_title)
            response = self.client.get(reverse('jogos:category', args=(1,)))
            content = response.content.decode('utf-8'),
            
            self.assertIn(needed_title,content)

        def test_jogos_category_view_function_is_correct(self):
            view = resolve(reverse('jogos:category', kwargs={'category_id': 1}))
            self.assertIs(view.func, views.category)

        def test_jogo_category_view_returns_404_if_no_games_found(self):
            response = self.client.get(reverse('jogos:category', kwargs={'category_id': 1}))
            self.assertEqual(response.status_code, 404)

        def test_jogos_detail_view_function_is_correct(self):
            view = resolve(reverse('jogos:jogos', kwargs={'id': 1}))
            self.assertIs(view.func, views.jogos)

        def test_jogos_detail_view_returns_404_if_no_games_found(self):
            response = self.client.get(reverse('jogos:jogos', kwargs={'id': 2}))
            self.assertEqual(response.status_code, 404)

