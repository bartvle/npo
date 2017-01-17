"""
"""


from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from . import views
from newsletter.views import subscribe as api_newsletter_subscribe
from npo.admin import admin_site


urlpatterns = [
    url(r'^admin/', admin_site.urls),
    url(r'^api/newsletter/subscribe', api_newsletter_subscribe),
    url(r'^$', views.start),
    url(r'^overons/$', views.overons),
    url(r'^beleid/$', views.beleid),
    url(r'^natuurgebieden/$', views.natuurgebieden),
    url(r'^soortbescherming/$', views.soortbescherming),
    url(r'^activiteiten/$', views.activiteiten),
    url(r'^activiteiten/(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})-(?P<slug>[\w-]+)/$', views.activiteit),
    url(r'^nieuwsbrief/$', views.nieuwsbrief),
    url(r'^lidworden/$', views.lidworden),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
