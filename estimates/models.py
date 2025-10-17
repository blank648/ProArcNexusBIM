from django.db import models

#maparea tabelului
class Deviz(models.Model):
    deviz_id = models.BigAutoField(db_column='DevizID', primary_key=True)
    numar_deviz = models.CharField(db_column='NumarDeviz', max_length=100,unique=True)
    data_emitere = models.DateTimeField(db_column='DataEmitere')
    client = models.ForeignKey('clients.Client', db_column='ClientID', on_delete=models.CASCADE)
    valoare_totala = models.DecimalField(
        db_column='ValoareTotala', max_digits=15, decimal_places=2, default=0
    )
    status = models.CharField(
        db_column='Status', max_length=50, default='Deschis'
    )

    class Meta:
        db_table = 'DEVIZ'
        managed = False
        ordering = ['-data_emitere']

class LinieDeviz(models.Model):
    linie_id = models.BigAutoField(db_column='LinieID', primary_key=True)
    deviz = models.ForeignKey(
        Deviz, db_column='DevizID', on_delete=models.CASCADE, related_name='linii'
    )
    articol = models.ForeignKey(
        'articles.Articol', db_column='ArticolID', on_delete=models.CASCADE
    )
    cantitate = models.DecimalField(
        db_column='Cantitate', max_digits=15, decimal_places=4, default=0
    )
    pret_unitar = models.DecimalField(
        db_column='PretUnitar', max_digits=15, decimal_places=2, default=0
    )

    #pt html
    @property
    def valoare(self):
        return self.cantitate * self.pret_unitar

    class Meta:
        db_table = 'LinieDeviz'
        managed = False