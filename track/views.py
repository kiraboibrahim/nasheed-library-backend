# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import F
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from anasheed_backend.utils import paginated_results
from .serializers import TrackSerializer, TrackViewSerializer
from .models import Track, TrackView, PopularTrackView
from artist.models import Artist
from django.http import JsonResponse

# Create your views here.

@api_view(['GET'])
def tracks(request):
    page = request.GET.get('page')
    tracks = paginated_results(page, TrackView.objects.all())
    return Response(TrackViewSerializer(tracks, many=True).data)

@api_view(['GET'])
def track_info(request, pk):
    try:
        track = TrackView.objects.get(id=pk)
    except TrackView.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(TrackViewSerializer(track).data)

@api_view(['GET'])
def top_tracks(request):
    # Popularity of an artist is based on his tracks, ie the popularity score(weighted average) of his tracks. popuarity score = 1/3 * listeners + 2/3 * downloads
    popular_tracks = PopularTrackView.objects.all();
    return Response(TrackViewSerializer(popular_tracks, many=True).data)

@api_view(['GET'])
def search_tracks(request):
    q = request.GET.get("q")
    page = request.GET.get("page")
    if q is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    search_results = paginated_results(page, TrackView.objects.filter(name__icontains=q))
    return Response(TrackViewSerializer(search_results, many=True).data)

@api_view(['POST'])
def register_listener(request, pk):
    try:
        pk = int(pk)
        track = list(Track.objects.filter(id=pk).values())[0]
    except IndexError:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Django suffixes the foreign key with 'id', which is not understood by the TrackSerializer

    artist_id = track['artist_id_id']
    del track['artist_id_id']
    # get the artist of the track
    artist = Artist.objects.get(id=artist_id)
    # Django requires the real model object instead of just an integer
    track['artist_id'] = artist
    track_instance = Track(**track)
    track['listeners'] = track['listeners'] + 1

    # Change the artist_id back to integer
    track['artist_id'] = artist_id

    serializer = TrackSerializer(track_instance, track)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def register_download(request, pk):
    try:
        pk = int(pk)
        track = list(Track.objects.filter(id=pk).values())[0]
    except IndexError:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Django suffixes the foreign key with 'id', which is not understood by the TrackSerializer

    artist_id = track['artist_id_id']
    del track['artist_id_id']
    # get the artist of the track
    artist = Artist.objects.get(id=artist_id)
    # Django requires the real model object instead of just an integer
    track['artist_id'] = artist
    track_instance = Track(**track)
    track['downloads'] = track['downloads'] + 1

    # Change the artist_id back to integer
    track['artist_id'] = artist_id

    serializer = TrackSerializer(track_instance, track)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(status=status.HTTP_200_OK)




@api_view(['GET'])
def stream_track(request, pk):
    # This will require byte serving
    pass
