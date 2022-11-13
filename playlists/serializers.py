from rest_framework import serializers

from rest_framework_serializer_extensions.fields import HashIdField

from tracks.serializers import TrackSerializer

from .models import Playlist


class PlaylistSerializer(serializers.ModelSerializer):
    id = HashIdField(model=Playlist, read_only=True)
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Playlist
        fields = ["id", "name", "tracks"]
        read_only_fields = ["user"]
