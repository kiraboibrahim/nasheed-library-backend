from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework_serializer_extensions.views import ExternalIdViewMixin

from tracks.serializers import TrackIdsSerializer

from .serializers import PlaylistSerializer
from .models import Playlist
from .permissions import IsPlaylistOwner


class PlaylistsListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlaylistSerializer

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user).prefetch_related("tracks")


class PlaylistDetailView(ExternalIdViewMixin, generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, IsPlaylistOwner)
    queryset = Playlist.objects.all().prefetch_related("tracks")
    serializer_class = PlaylistSerializer
    lookup_url_kwarg = "playlist_id"


class PlaylistDestroyView(ExternalIdViewMixin, generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, IsPlaylistOwner)
    queryset = Playlist.objects.all()
    lookup_url_kwarg = "playlist_id"


class PlaylistUpdateView(ExternalIdViewMixin, generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, IsPlaylistOwner)
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    lookup_url_kwarg = "playlist_id"


class PlaylistCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlaylistSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PlaylistTracksAddView(ExternalIdViewMixin, generics.GenericAPIView):
    permission_classes = (IsAuthenticated, IsPlaylistOwner)
    serializer_class = TrackIdsSerializer
    lookup_url_kwarg = "playlist_id"
    queryset = Playlist.objects.all()
    http_method_names = ["put"]

    def put(self, request, *args, **kwargs):
        self.check_permissions(request)
        playlist = self.get_object()
        self.check_object_permissions(request, playlist)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.add_tracks_to_playlist(serializer.get_tracks(), playlist)
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def add_tracks_to_playlist(tracks, playlist):
        playlist.tracks.add(*tracks)
        return playlist


class PlaylistTracksRemoveView(ExternalIdViewMixin, generics.GenericAPIView):
    permission_classes = (IsAuthenticated, IsPlaylistOwner)
    serializer_class = TrackIdsSerializer
    lookup_url_kwarg = "playlist_id"
    queryset = Playlist.objects.all()
    http_method_names = ["put"]

    def put(self, request, *args, **kwargs):
        self.check_permissions(request)
        playlist = self.get_object()
        self.check_object_permissions(request, playlist)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.remove_tracks_from_playlist(serializer.get_tracks(), playlist)
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def remove_tracks_from_playlist(tracks, playlist):
        playlist.tracks.remove(*tracks)
        return playlist
