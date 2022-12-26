from rest_framework import serializers
from rest_framework_serializer_extensions.fields import HashIdField, HashIdHyperlinkedRelatedField

from rest_framework_serializer_extensions.serializers import SerializerExtensionsMixin

from artists.models import Artist
from artists.serializers import ArtistSerializer
from artists.utils import internal_ids_from_model_and_external_ids

from .models import Track


class TrackSerializer(SerializerExtensionsMixin, serializers.ModelSerializer):
    id = HashIdField(model=Track)
    artist = ArtistSerializer()

    class Meta:
        model = Track
        exclude = ["uploaded_at"]
        read_only_fields = ["name", "artist", "file", "uploaded_at", "duration"]


class TrackIdsSerializer(serializers.Serializer):
    track_ids = serializers.ListField(child=serializers.CharField(), allow_empty=False, min_length=1)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        try:
            track_ids = internal_ids_from_model_and_external_ids(Track, data["track_ids"])
        except Track.DoesNotExist:
            raise serializers.ValidationError({"track_ids": "All or some track IDs are invalid"})
        validated_data = {
            "track_ids": track_ids
        }
        return validated_data

    def get_tracks(self):
        return Track.objects.filter(pk__in=self.validated_data["track_ids"])

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError

