from rest_framework import serializers

from rest_framework_serializer_extensions.fields import HashIdField

from .models import Artist, ArtistSubscription
from .utils import internal_ids_from_model_and_external_ids


class ArtistSerializer(serializers.ModelSerializer):
    id = HashIdField(model=Artist)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["image"] = instance.large_thumbnail_url
        return ret

    class Meta:
        model = Artist
        fields = ("id", "name", "image")


class ArtistIdsSerializer(serializers.Serializer):
    artist_ids = serializers.ListField(child=serializers.CharField(), allow_empty=False, min_length=1)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        try:
            artist_ids = internal_ids_from_model_and_external_ids(Artist, data["artist_ids"])
        except Artist.DoesNotExist:
            raise serializers.ValidationError({"artist_ids": "All or some artist IDs are invalid"})
        validated_data = {
            "artist_ids": artist_ids
        }
        return validated_data

    def get_artists(self):
        return Artist.objects.filter(pk__in=self.validated_data.get("artist_ids"))

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError


class ArtistSubscriptionSerializer(serializers.ModelSerializer):
    id = HashIdField(model=ArtistSubscription)
    artists = ArtistSerializer(many=True)

    class Meta:
        model = ArtistSubscription
        fields = ["id", "artists"]
        depth = 1
