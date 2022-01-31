
from rest_framework import serializers
from .models import Artist

class ArtistSerializer(serializers.ModelSerializer):
    num_songs = serializers.IntegerField(read_only=True)
    class Meta:
        model = Artist
        fields = ['id', 'name', 'image', 'num_songs']

class PopularArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'image']
