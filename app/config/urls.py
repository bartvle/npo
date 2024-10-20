"""
"""


from django.conf import settings
from django.urls import path, re_path, include
from django.conf.urls.static import static

# from wagtail.admin import urls as wagtailadmin_urls
# from wagtail import urls as wagtail_urls
# from wagtail.documents import urls as wagtaildocs_urls

from frontend import views
from frontend.admin import admin_site


urlpatterns = [
    path('admin/', admin_site.urls),
    path('', views.start),
	path('over-ons/', views.over_ons),
	path('beleid/', views.beleid),
    path('natuurgebieden/', views.natuurgebieden),
    path('natuurgebieden/gondebeekvallei/toegankelijkheid', views.natuurgebieden_gondebeekvallei_toegankelijkheid),
    path('soortbescherming/', views.soortbescherming),
    path('activiteiten/', views.activiteiten),
    path('activiteiten/<int:year>-<int:month>-<int:day>-<slug:slug>/', views.activiteit),
    path('nieuws/', views.nieuws),
    path('nieuws/<int:year>-<int:month>-<int:day>-<slug:slug>/', views.artikel),
    path('lid-worden/', views.lid_worden),
    path('steun-ons/', views.steun_ons),
    path('doe-mee/', views.doe_mee),
    path('rodeland/', views.rodeland),
    path('rodeland/app/', views.rodeland_app),
    path('beleid/memorandum/', views.memorandum),
    path('beleid/memorandum/n-va/', views.memorandum_nva),
    path('beleid/memorandum/groen/', views.memorandum_groen),
    path('formulieren/nieuwsbrief/', views.form_nieuwsbrief),

    # path('cms/', include(wagtailadmin_urls)),
    # path('documents/', include(wagtaildocs_urls)),
    # path('pages/', include(wagtail_urls)),

    re_path('^.*/$', views.start),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
