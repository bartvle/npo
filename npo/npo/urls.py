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
	path('over-ons/', views.over_ons),
	path('beleid/', views.beleid),
    path('natuurgebieden/', views.natuurgebieden),
    path('soortbescherming/', views.soortbescherming),
    path('activiteiten/', views.activiteiten),
    path('activiteiten/<int:year>-<int:month>-<int:day>-<slug:slug>/', views.activiteit),
    path('artikels/', views.artikels),
    path('artikels/<int:year>-<int:month>-<int:day>-<slug:slug>/', views.artikel),
    path('nieuwsbrief/', views.magazine),
    path('lid-worden/', views.lid_worden),
    path('steun-ons/', views.steun_ons),
    path('gluren-bij-de-buren/', views.gluren_bij_de_buren),
    path('rodeland/', views.rodeland),
    path('rodeland/app/', views.rodeland_app),
    path('beleid/memorandum/', views.memorandum),
    path('beleid/memorandum/n-va/', views.memorandum_nva),
    path('beleid/memorandum/groen/', views.memorandum_groen),


    ## Legacy
    path('overons/', views.over_ons), ## from 2018-07-04
    path('lidworden/', views.lid_worden), ## from 2018-07-04
    path('1Y3QgU7vcHqFNizeVjfFWg9U0V7Jb5eOXjjzBPldxXnhctUBdYRKvylsdioY85YU/', views.rodeland_app), ## from 2018-07-04
    path('memorandum/', views.memorandum), ## from 2018-11-21
    path('memorandum/n-va/', views.memorandum_nva), ## from 2018-11-21
    path('memorandum/groen/', views.memorandum_groen), ## from 2018-11-21
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
