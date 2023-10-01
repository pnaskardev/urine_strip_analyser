from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os 

from . models import ImageModel

@receiver(pre_delete, sender=ImageModel)
def delete_old_file(sender, instance, **kwargs):
   
   # This signal is triggered when an ImageModel instance is about to be deleted.
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
   