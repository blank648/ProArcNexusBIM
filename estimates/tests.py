from django.test import TestCase
from django.urls import reverse
from accounts.models import Utilizator
from clients.models import Client
from articles.models import Articol
from .models import Deviz

class EstimatesTests(TestCase):
    def setUp(self):
        self.user = Utilizator.objects.create_user('u', password='p', role='user')
        self.client.login(username='u', password='p')
        self.client_obj = Client.objects.create(denumire='C1')
        self.art = Articol.objects.create(cod='X1', denumire='D', um='buc', pret_standard=5)

    def test_create_deviz(self):
        def test_create_deviz(self):
            url = reverse('estimates:create')
            post_data = {
                'numar_deviz': 'D1', 'data_emitere': '2025-05-01', 'client': self.client_obj.pk,
                'status': 'Deschis',
                'liniedeviz-TOTAL_FORMS': '1', 'liniedeviz-INITIAL_FORMS': '0', 'liniedeviz-MIN_NUM_FORMS': '0',
                'liniedeviz-MAX_NUM_FORMS': '1000',
                'liniedeviz-0-articol': self.art.pk, 'liniedeviz-0-cantitate': '2', 'liniedeviz-0-pret_unitar': '',
            }
            response = self.client.post(url, post_data)
            self.assertEqual(response.status_code, 302)
            self.assertTrue(Deviz.objects.filter(numar_deviz='D1').exists())
            dev = Deviz.objects.get(numar_deviz='D1')
            self.assertEqual(dev.valoare_totala, 10)
