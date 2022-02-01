# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from artist.models import Artist
from django.db import models

# Create your models here.

class TrackBaseClass(models.Model):
    anasheed_id = models.IntegerField(null=False, unique=True)
    artist_id = models.ForeignKey(Artist, db_column="artist_id", null=False, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, null=False, unique=True, db_index=True)
    listeners = models.IntegerField(default=0, null=True)
    downloads = models.IntegerField(default=0, null=True)
    filename = models.CharField(max_length=255, unique=True, null=False)


    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Track(TrackBaseClass):
    class Meta:
        ordering = ['name']
        db_table = "tracks"


class TrackView(TrackBaseClass):
    pop_score = models.IntegerField()
    stream_reference = models.CharField(max_length=255, unique=True, null=False)
    class Meta:
        db_table = "tracks_view"

class PopularTrackView(TrackBaseClass):
    pop_score = models.IntegerField()
    stream_reference = models.CharField(max_length=255, unique=True, null=False)
    class Meta:
        db_table = "popular_tracks_view"

class Stream(models.Model):
    reference = models.CharField(max_length=255, unique=True, null=False)
    track_id = models.ForeignKey(Track, db_column="track_id", null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "streams"
