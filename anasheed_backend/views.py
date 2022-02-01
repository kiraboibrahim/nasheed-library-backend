from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Artist
from track.models import Track
from track.serializers import TrackSerializer
from .serializers import ArtistSerializer

def suggest(request, text):
    # Search artists whose names contain the text, and also search the tracks whose names contain the DoesNotExist
    pass
