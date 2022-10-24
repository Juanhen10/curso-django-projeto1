from django.test import TestCase
from django.urls import reverse


class JogosURLsTEst(TestCase):
    def test_home_url_is_correct(self):
        url = reverse('jogos:home')
        self.assertEqual(url, '/')

    def test_jogos_category_url_is_correct(self):
        url = reverse('jogos:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/jogos/category/1/')


    def test_jogos_url_is_correct(self):
        url = reverse('jogos:jogos', kwargs={'id': 1})
        self.assertEqual(url, '/jogos/1/')
