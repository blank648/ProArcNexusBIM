from django.test import TestCase
from django.urls import reverse
from accounts.models import Utilizator
from .models import SetareGenerala

class SettingsAppTests(TestCase):
    def setUp(self):
        self.admin = Utilizator.objects.create_user('a', password='p', role='admin')
        self.client.login(username='a', password='p')

    def test_create_setting(self):
        response = self.client.post(reverse('settings_app:create'), {'cheie': 'k', 'valoare': 'v'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(SetareGenerala.objects.filter(cheie='k').exists())
