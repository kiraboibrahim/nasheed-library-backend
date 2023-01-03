from django.db import models
from django.contrib.auth import get_user_model

from thumbnails.fields import ImageField
from thumbnails import images, backends

User = get_user_model()


class Artist(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = ImageField(upload_to="images/artists", pregenerated_sizes=["small", "large"])

    @property
    def large_thumbnail_url(self):
        thumbnail_name = images.get_thumbnail_name(self.image.name, "large")
        thumbnail_storage_backend = backends.storage.get_backend()
        return thumbnail_storage_backend.url(thumbnail_name)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]


class ArtistSubscription(models.Model):
    artists = models.ManyToManyField(Artist, related_name="subscriptions")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="subscriptions")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
