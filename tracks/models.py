from __future__ import unicode_literals

from django.db import models

from artists.models import Artist


class Track(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT, related_name='tracks')
    name = models.CharField(max_length=100, null=False, unique=True, db_index=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="tracks/")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-uploaded_at"]
