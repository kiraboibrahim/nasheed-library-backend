from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework_serializer_extensions.views import ExternalIdViewMixin
from rest_framework_serializer_extensions.utils import internal_id_from_model_and_external_id

from tracks.models import Track
from tracks.serializers import TrackSerializer

from .models import Artist, ArtistSubscription
from .serializers import ArtistSerializer, ArtistIdsSerializer, ArtistSubscriptionSerializer


class ArtistsListView(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDetailView(ExternalIdViewMixin, generics.RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_url_kwarg = 'artist_id'


class ArtistTracksListView(generics.ListAPIView):
    serializer_class = TrackSerializer
    lookup_url_kwarg = 'artist_id'

    def get_queryset(self):
        artist_id = internal_id_from_model_and_external_id(Artist, self.kwargs[self.lookup_url_kwarg])
        return Track.objects.filter(artist_id=artist_id)


class ArtistsSearchView(generics.ListAPIView):
    serializer_class = ArtistSerializer
    lookup_url_kwarg = "query"

    def get_queryset(self):
        return Artist.objects.filter(name__icontains=self.kwargs[self.lookup_url_kwarg])


class ArtistSubscriptionsAddView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    http_method_names = ["put"]
    serializer_class = ArtistIdsSerializer

    def put(self, request, *args, **kwargs):
        self.check_permissions(request)
        subscription, _ = ArtistSubscription.objects.get_or_create(user=request.user)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.add_artists_to_subscription(serializer.get_artists(), subscription)
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def add_artists_to_subscription(artists, subscription):
        subscription.artists.add(*artists)
        return subscription


class ArtistSubscriptionsListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ArtistSubscriptionSerializer

    def get_queryset(self):
        return ArtistSubscription.objects.filter(user=self.request.user).prefetch_related("artists")
