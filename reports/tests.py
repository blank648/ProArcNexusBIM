from django.test import TestCase
from django.urls import reverse
from accounts.models import Utilizator
from clients.models import Client
from estimates.models import Deviz

class ReportsTestCase(TestCase):
    def setUp(self):
        self.mgr = Utilizator.objects.create_user('m', password='p', role='manager')
        self.client.login(username='m', password='p')
        self.cli = Client.objects.create(denumire='C')
        Deviz.objects.create(numar_deviz='R1', data_emitere='2025-05-01', client=self.cli, valoare_totala=100)

    def test_summary_view(self):
        response = self.client.get(reverse('reports:summary'), {'start_date': '2025-05-01', 'end_date': '2025-05-31'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'C')