from django.urls import path, re_path

from .views import ArtistsListView, ArtistDetailView, ArtistTracksListView, ArtistsSearchView, \
    ArtistSubscriptionsAddView, ArtistSubscriptionsListView


urlpatterns = [
    path("", ArtistsListView.as_view(), name='artists'),
    path("subscriptions/", ArtistSubscriptionsListView.as_view(), name="artist-subscriptions-list"),
    path("subscribe/", ArtistSubscriptionsAddView.as_view(), name="artist-subscriptions-add"),
    path("search/<str:query>", ArtistsSearchView.as_view(), name="artists-search"),
    re_path("^(?P<artist_id>\w+)/$", ArtistDetailView.as_view(), name="artist-detail"),
    re_path("^(?P<artist_id>\w+)/tracks/$", ArtistTracksListView.as_view(), name="artist-tracks"),
]
