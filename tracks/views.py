from rest_framework import generics

from .serializers import TrackSerializer

from .models import Track


class TracksListView(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TracksSearchView(generics.ListAPIView):
    serializer_class = TrackSerializer
    lookup_url_kwarg = "query"

    def get_queryset(self):
        return Track.objects.filter(name__icontains=self.kwargs[self.lookup_url_kwarg])
