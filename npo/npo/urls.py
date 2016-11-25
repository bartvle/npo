"""npo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from npo.views import index, api_magazine
from newsletter.views import subscribe as api_newsletter_subscribe
from api.urls import api_router
from npo.admin import admin_site


urlpatterns = [
    url(r'^admin/', admin_site.urls),
    url(r'^api/magazine/', api_magazine),
    url(r'^api/newsletter/subscribe', api_newsletter_subscribe),
    url(r'^api/', include(api_router.urls)),
    url(r'^$', index),
    url(r'^overons', index),
    url(r'^beleid', index),
    url(r'^natuurgebieden', index),
    url(r'^soortbescherming', index),
    url(r'^nieuwsbrief', index),
    url(r'^lidworden', index),
    url(r'^activiteiten', index),
]
