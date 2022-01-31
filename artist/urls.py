from django.conf.urls import url
from .views import artists, artist_info, artist_tracks, popular_artists, search_artists

urlpatterns = [
    url(r'^$', artists, name="all-artists"),
    url(r'^(?P<pk>\d+)$', artist_info, name="artist-info"),
    url(r'^(?P<pk>\d+)/tracks$', artist_tracks, name="artist-tracks"),
    url(r'^popular$', popular_artists, name="popular-artists"),
    url(r'^search$', search_artists, name="search-artists"),

]
