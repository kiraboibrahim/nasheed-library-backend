
from django.conf.urls import include
from django.urls import re_path
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/v2/accounts/', include('accounts.urls')),
    re_path(r'^api/v2/playlists/', include('playlists.urls')),
    re_path(r'^api/v2/artists/', include('artists.urls')),
    re_path(r'^api/v2/tracks/', include('tracks.urls')),
]
