from rest_framework import serializers
from .models import Track, Stream

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'
        #fields = ['id', 'name', 'listeners', 'downloads', 'filename', 'artist_id']

class StreamSerializer(serializers.ModelSerializer):
    track = TrackSerializer(required=True)
    class Meta:
        model = Stream
        fields = '__all__'
