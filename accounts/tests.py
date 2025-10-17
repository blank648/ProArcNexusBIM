from django.test import TestCase
from django.urls import reverse
from .models import Utilizator

class AccountTests(TestCase):
    def setUp(self):
        self.user = Utilizator.objects.create_user(username='user1', password='pass1', role='user')

    def test_signup(self):
        response = self.client.post(reverse('accounts:signup'), {
            'username': 'newuser',
            'password1': 'newpass1',
            'password2': 'newpass2',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Utilizator.objects.filter(username='newuser').exists())

    def test_login_logout(self):
        response = self.client.post(reverse('accounts:login'), {
            'username': 'user1', 'password': 'pass1'
        })
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('accounts:logout'))
        self.assertEqual(response.status_code, 302)

    def test_profile_edit(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.post(reverse('accounts:profile'), {'username': 'user1'})
        self.assertEqual(response.status_code, 302)
