# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Count, Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Artist, ArtistView, PopularArtistView
from track.models import Track
from track.serializers import TrackSerializer
from .serializers import ArtistSerializer
from anasheed_backend.utils import paginated_results


# Create your views here.

@api_view(['GET'])
def artists(request):
    page = request.GET.get('page')
    artists = paginated_results(page, ArtistView.objects.all())
    return Response(ArtistSerializer(artists, many=True).data)

@api_view(['GET'])
def artist_info(request, pk):
    try:
        artist = ArtistView.objects.get(id=pk)
    except ArtistView.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(ArtistSerializer(artist).data)

@api_view(['GET'])
def artist_tracks(request, pk):
    page = request.GET.get("page")
    tracks = paginated_results(page, Track.objects.filter(artist_id=pk))
    return Response(TrackSerializer(tracks, many=True).data)

@api_view(['GET'])
def popular_artists(request):
    # Popularity of an artist is based on his tracks, ie the popularity score(weighted average) of his tracks. popuarity score = 1/3 * listeners + 2/3 * downloads
    popular_artists = PopularArtistView.objects.all();
    return Response(ArtistSerializer(popular_artists, many=True).data)

@api_view(['GET'])
def search_artists(request):
    q = request.GET.get("q")
    page = request.GET.get("page")
    if q is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    search_results = paginated_results(page, ArtistView.objects.filter(name__icontains=q))
    return Response(ArtistSerializer(search_results, many=True).data)
