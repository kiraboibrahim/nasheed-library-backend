from django.db import models
from django.contrib.auth import get_user_model

from tracks.models import Track

User = get_user_model()


class Playlist(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="playlists")
    tracks = models.ManyToManyField(Track, related_name="playlist")
    is_favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-is_favorite", "-created_at"]
