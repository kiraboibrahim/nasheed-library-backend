from rest_framework import serializers
from .models import TrackView, Track

class TrackViewSerializer(serializers.ModelSerializer):
    stream_reference = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = TrackView
        exclude = ['anasheed_id', 'filename']

class TrackSerializer(serializers.ModelSerializer):

    def update(self, instance, validated):
        instance.listeners = validated.get('listeners', instance.listeners)
        instance.downloads = validated.get('downloads', instance.downloads)
        instance.save()
        return instance

    class Meta:
        model = Track
        exclude = ['anasheed_id', 'filename']
