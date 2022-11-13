from django.urls import path, re_path

from .views import PlaylistDetailView, PlaylistDestroyView, PlaylistCreateView, PlaylistUpdateView, \
    PlaylistTracksAddView, PlaylistTracksRemoveView, PlaylistsListView

urlpatterns = [
    path("", PlaylistsListView.as_view(), name="playlists-list"),
    path("create/", PlaylistCreateView.as_view(), name="playlist-create"),
    re_path("^(?P<playlist_id>\w+)/$", PlaylistDetailView.as_view(), name="playlist-detail"),
    re_path("^(?P<playlist_id>\w+)/update/$", PlaylistUpdateView.as_view(), name="playlist-update"),
    re_path("^(?P<playlist_id>\w+)/delete/$", PlaylistDestroyView.as_view(), name="playlist-destroy"),
    re_path("^(?P<playlist_id>\w+)/add-tracks/$", PlaylistTracksAddView.as_view(), name="playlist-tracks-add"),
    re_path("^(?P<playlist_id>\w+)/remove-tracks/$", PlaylistTracksRemoveView.as_view(), name="playlist-tracks-remove")
]
