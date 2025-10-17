from django.db import models

#mapez tabela oracle
class Client(models.Model):
    client_id = models.BigAutoField(db_column='ClientID', primary_key=True)
    denumire = models.CharField(db_column='Denumire', max_length=255)
    cui = models.CharField(db_column='CUI', max_length=50, blank=True, null=True)
    adresa = models.CharField(db_column='Adresa', max_length=255, blank=True, null=True)
    telefon = models.CharField(db_column='Telefon', max_length=255, blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'Client'
        managed = False