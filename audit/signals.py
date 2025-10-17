from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.forms.models import model_to_dict

from .models import ChangeLog
from estimates.models import Deviz, LinieDeviz
from articles.models import Articol
from clients.models import Client

TRACKED_MODELS = [Deviz, LinieDeviz, Articol, Client]

#Daca sender e urmaribil (Deviz, LinieDeviz, Articol, Client), creeaza ChangeLog cu action='create' sau 'update', new_data=model_to_dict(instance).
@receiver(post_save)
def log_save(sender, instance, created, **kwargs):
    if sender in TRACKED_MODELS:
        action = 'create' if created else 'update'
        old = None
        #la primul update pot face query inainte de salvare pt old_data, dar vom lasa old_data null
        ChangeLog.objects.create(
            user=getattr(instance, 'user', None),
            model_name=sender.__name__,
            object_pk=str(instance.pk),
            action=action,
            new_data=model_to_dict(instance),
            old_data=old
        )
#pentru delete, salveaza old_data=model_to_dict(instance)
@receiver(post_delete)
def log_delete(sender, instance, **kwargs):
    if sender in TRACKED_MODELS:
        ChangeLog.objects.create(
            user=getattr(instance, '_current_user', None),
            model_name=sender.__name__,
            object_pk=str(instance.pk),
            action='delete',
            old_data=model_to_dict(instance),
            new_data=None
        )
