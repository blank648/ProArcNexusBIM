from django.test import TestCase
from accounts.models import Utilizator
from .models import ChangeLog
from clients.models import Client

class AuditTests(TestCase):
    def setUp(self):
        self.admin = Utilizator.objects.create_user('a', password='p', role='admin')
        self.client.login(username='a', password='p')

    def test_log_creation(self):
        c = Client.objects.create(denumire='C')
        self.assertTrue(ChangeLog.objects.filter(model_name='Client', action='create', object_pk=str(c.pk)).exists())
