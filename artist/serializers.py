
from rest_framework import serializers
from .models import ArtistView

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistView
        fields = ['id', 'name', 'image', 'num_songs']
