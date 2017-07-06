"""
"""


from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from . import views
from npo.admin import admin_site


urlpatterns = [
    url(r'^admin/', admin_site.urls),
    url(r'^$', views.start),
    url(r'^overons/$', views.over_ons),
    url(r'^beleid/$', views.beleid),
    url(r'^natuurgebieden/$', views.natuurgebieden),
    url(r'^soortbescherming/$', views.soortbescherming),
    url(r'^activiteiten/$', views.activiteiten),
    url(r'^activiteiten/(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})-(?P<slug>[\w-]+)/$', views.activiteit),
    url(r'^nieuws/$', views.nieuws),
    url(r'^nieuws/(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})-(?P<slug>[\w-]+)/$', views.artikel),
    url(r'^nieuwsbrief/$', views.magazine),
    url(r'^lidworden/$', views.lid_worden),
    url(r'^gluren-bij-de-buren/$', views.gluren_bij_de_buren),
    url(r'^1Y3QgU7vcHqFNizeVjfFWg9U0V7Jb5eOXjjzBPldxXnhctUBdYRKvylsdioY85YU/$', views.kaart_regionaal_bos),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
