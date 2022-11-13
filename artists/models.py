from django.db import models
from django.contrib.auth import get_user_model

from thumbnails.fields import ImageField


User = get_user_model()


class Artist(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = ImageField(upload_to="images/artists", pregenerated_sizes=["small", "large"])

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
