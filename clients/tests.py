from django.test import TestCase
from django.urls import reverse
from accounts.models import Utilizator
from .models import Client

class ClientTests(TestCase):
    def setUp(self):
        self.admin = Utilizator.objects.create_user('admin', password='a', role='admin')
        self.client.login(username='admin', password='a')

    def test_create_client(self):
        response = self.client.post(reverse('clients:create'), {'denumire': 'C1', 'cui': 'RO1'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Client.objects.filter(denumire='C1').exists())


