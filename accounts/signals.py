from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from playlists.models import Playlist


User = get_user_model()


@receiver(post_save, sender=User)
def create_favorite_playlist(sender, instance, created, **kwargs):
    if created:
        Playlist.objects.create(name="Favorites", user=instance, is_favorite=True)
