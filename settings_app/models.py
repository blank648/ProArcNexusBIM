from django.db import models

class SetareGenerala(models.Model):
    setare_id = models.BigAutoField(db_column='SetareID',primary_key=True)
    cheie = models.CharField(db_column='Cheie',max_length=100,unique=True)
    valoare = models.TextField(db_column='Valoare',blank=True,null=True)

    class Meta:
        db_table = 'SetariGenerale'
        managed = False
        ordering = ['cheie']

    def __str__(self):
        return f"{self.cheie} = {self.valoare}"