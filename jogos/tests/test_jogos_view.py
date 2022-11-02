from unicodedata import name
from unittest import skip
from urllib import response

from django.urls import resolve, reverse
from jogos import views
from this import s

from .test_jogos_base import GamesTestBase


class jogosViewsTest(GamesTestBase):
    def test_jogos_home_view_function_is_correct(self):
        view = resolve(reverse('jogos:home'))
        self.assertIs(view.func, views.home)



    def test_jogos_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('jogos:home'))
        self.assertEqual(response.status_code, 200)



    def test_jogos_home_view_loads_correct_template(self):
        response = self.client.get(reverse('jogos:home'))
        self.assertTemplateUsed(response, 'jogos/pages/home.html')


    
    def test_jogos_home_template_shows_no_jogoss_found_if_no_jogoss(self):
        response = self.client.get(reverse('jogos:home'))
        self.assertIn(
            ' <h1>NO GAMES FOUND HERE</h1>',
            response.content.decode('utf-8')
        )



    def test_jogos_home_template_loads_jogoss(self):
        # Need a jogos for this test
        self.make_game()

        response = self.client.get(reverse('jogos:home'))
        content = response.content.decode('utf-8')
        response_context_jogoss = response.context['jogos']

        # Check if one jogos exists
        self.assertIn('HOME ♦jogos', content)
        self.assertEqual(len(response_context_jogoss), 0)



    def test_jogos_category_template_dont_load_jogoss_not_published(self):
        """Test jogos is_published False dont show"""
        # Need a jogos for this test
        jogos = self.make_game(is_published=False)
        response = self.client.get(reverse('jogos:jogos', kwargs={'id': jogos.category.id}))

        # Check if one jogos exists
        self.assertEqual(response.status_code, 404)
        

    
    @skip
    def test_jogos_category_view_function_is_correct(self):
        view = resolve(
            reverse('jogos:category', kwargs={'category_id': 1000})
        )
        self.assertIs(view.func, views.category)



    def test_jogos_category_view_returns_404_if_no_jogoss_found(self):
        response = self.client.get(
            reverse('jogos:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)



    def test_jogos_category_template_loads_jogoss(self):
        needed_title = 'Not Found'
        # Need a jogos for this test
        self.make_game(title=needed_title)

        response = self.client.get(reverse('jogos:category', args=(1,)))
        content = response.content.decode('utf-8')

        # Check if one jogos exists
        self.assertIn(needed_title, content)



    def test_jogos_detail_view_function_is_correct(self):
        view = resolve(
            reverse('jogos:jogos', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.jogos)



    def test_jogos_detail_view_returns_404_if_no_jogoss_found(self):
        response = self.client.get(
            reverse('jogos:jogos', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)



    def test_jogos_detail_template_loads_the_correct_jogos(self):
        needed_title = 'Not Found'

        # Need a jogos for this test
        self.make_game(title=needed_title)

        response = self.client.get(
            reverse(
                'jogos:jogos',
                kwargs={
                    'id': 1
                }
            )
        )
        content = response.content.decode('utf-8')

        # Check if one jogos exists
        self.assertIn(needed_title, content)

    @skip
    def test_jogos_detail_template_dont_load_jogoss_not_published(self):
            """Test jogos is_published False dont show"""
            # Need a jogos for this test
            game = self.make_game(is_published=False)
            response = self.client.get(
                reverse(
                    'jogos:jogos',
                    kwargs={
                        'id': game.id
                    }
                )
        )
            # Check if one jogos exists
            self.assertEqual(response.status_code, 404)
            