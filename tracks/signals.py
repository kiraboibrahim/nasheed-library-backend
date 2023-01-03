from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Track
from .utils import get_track_duration


@receiver(pre_save, sender=Track)
def save_track_duration(sender, instance, **kwargs):
    if instance.duration is None:
        # It can already be defined when loading fixtures
        instance.duration = get_track_duration(instance.file.open("r"))
