from django.conf.urls import url
from .views import tracks, track_info, top_tracks, search_tracks, register_listener, register_download

urlpatterns = [
    url(r'^$', tracks, name="tracks"),
    url(r'^(?P<pk>\d+)$', track_info, name="track-info"),
    url(r'^popular$', top_tracks, name="top-tracks"),
    url(r'^search$', search_tracks, name="search-tracks"),
    url(r'^(?P<pk>\d+)/listener$', register_listener, name="register-listener"),
    url(r'^(?P<pk>\d+)/download$', register_download, name="register-download"),
]
