from django.test import TestCase
from django.urls import reverse
from accounts.models import Utilizator
from .models import Articol

class ArticlesTest(TestCase):
    def setUp(self):
        self.manager = Utilizator.objects.create_user('mgr', password='p', role='manager')
        self.client.login(username='mgr', password='p')

    def test_create_articol(self):
        data = {'cod': 'A1', 'denumire': 'Art1', 'um': 'buc', 'pret_standard': 10}
        response = self.client.post(reverse('articles:create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Articol.objects.filter(cod='A1').exists())

