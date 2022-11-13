from django.urls import path

from .views import TracksListView, TracksSearchView


urlpatterns = [
    path("", TracksListView.as_view(), name="tracks-list"),
    path("search/<str:query>", TracksSearchView.as_view(), name="tracks-search")
]
