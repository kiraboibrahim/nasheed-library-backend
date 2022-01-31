# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Artist(models.Model):
    anasheed_id = models.IntegerField(null=False, unique=True)
    name = models.CharField(max_length=50, null=False, unique=True, db_index=True)
    image = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "artists"
        ordering = ["name"]
