from django.db import models

#mapeaza tabela articol
class Articol(models.Model):
    articol_id = models.BigAutoField(db_column='ArticolID',primary_key=True)
    cod = models.CharField(db_column='Cod',max_length=50,unique=True)
    denumire = models.CharField(db_column='Denumire',max_length=255)
    um = models.CharField(db_column='UM',max_length=20)
    pret_standard = models.DecimalField(db_column='Pret_Standard', max_digits=15, decimal_places=2, default=0)

    class Meta:
        db_table = 'Articol'
        managed = False
        ordering = ['cod']