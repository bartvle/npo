"""
"""


from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

from . import views
from npo.admin import admin_site


urlpatterns = [
    path('admin/', admin_site.urls),
    path('', views.start),
	path('overons/', views.over_ons),
	path('beleid/', views.beleid),
    path('natuurgebieden/', views.natuurgebieden),
    path('soortbescherming/', views.soortbescherming),
    path('activiteiten/', views.activiteiten),
    path('activiteiten/<int:year>-<int:month>-<int:day>-<slug:slug>', views.activiteit),
    # path('nieuws/$', views.nieuws),
    # path('^nieuws/(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})-(?P<slug>[\w-]+)/$', views.artikel),
    path('nieuwsbrief/', views.magazine),
    path('lidworden/', views.lid_worden),
    path('gluren-bij-de-buren/', views.gluren_bij_de_buren),
    path('1Y3QgU7vcHqFNizeVjfFWg9U0V7Jb5eOXjjzBPldxXnhctUBdYRKvylsdioY85YU/', views.kaart_regionaal_bos),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
