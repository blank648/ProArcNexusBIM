from django.db import models
from django.conf import settings

class ChangeLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    model_name = models.CharField(max_length=100)
    object_pk = models.CharField(max_length=100)
    action = models.CharField(
        max_length=10,
        choices=[('create','create'),('update','update'),('delete','delete')]
    )
    old_data = models.JSONField(null=True, blank=True)
    new_data = models.JSONField(null=True, blank=True)

    class Meta:
        ordering = ['-timestamp',]
