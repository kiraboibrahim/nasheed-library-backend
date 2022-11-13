from django.contrib import admin
from image_cropping import ImageCroppingMixin

from .models import Artist


class ArtistAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


admin.site.register(Artist, ArtistAdmin)
