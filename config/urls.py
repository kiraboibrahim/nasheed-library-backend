
from django.conf.urls import include, static
from django.urls import re_path
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^v2/accounts/', include('accounts.urls')),
    re_path(r'^v2/playlists/', include('playlists.urls')),
    re_path(r'^v2/artists/', include('artists.urls')),
    re_path(r'^v2/tracks/', include('tracks.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)