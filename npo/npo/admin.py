"""
"""


import csv
import json
import os

from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import path
from django.db.models import Sum
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models.functions import TruncYear

from register.models import Parcel, Ownership
from newsletter.models import Subscription
from amphi.models import Input


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Dashboard').exists())
def dashboard(request, key):
    """
    """
    context = {}

    return render(request, 'admin/dashboard.htm', context=context)


@login_required
@user_passes_test(lambda user: user.groups.filter(name='WG Aankopen').exists())
def perceel(request, key):
    """
    """
    try:
        parcel = Parcel.objects.get(key=key.replace('-', '/'))
    except Parcel.DoesNotExist:
        parcel = None

    context = {'parcel': parcel}

    return render(request, 'admin/perceel.htm', context=context)


@login_required
@user_passes_test(lambda user: user.groups.filter(name='WG Aankopen').exists())
def eigenaar(request, id):
    """
    """
    keys = [o.parcel.key for o in Ownership.objects.filter(owner__id=id)]

    return JsonResponse(keys, safe=False)


@login_required
@user_passes_test(lambda user: user.groups.filter(name='WG Aankopen').exists())
def kadaster_gondebeekvallei(request):
    """
    """
    context = {}

    with open(os.path.join(os.path.dirname(__file__), 'data', 'gondebeek_parcels.geojson')) as f:
        gondebeek_parcels = json.load(f)
    context['gondebeek_parcels'] = json.dumps(gondebeek_parcels)

    with open(os.path.join(os.path.dirname(__file__), 'data', 'gondebeek_perimeter.geojson')) as f:
        gondebeek_perimeter = json.load(f)
    context['gondebeek_perimeter'] = json.dumps(gondebeek_perimeter)

    return render(request, 'admin/kadaster_gondebeekvallei.htm', context=context)


@login_required
@user_passes_test(lambda user: user.groups.filter(name='WG Aankopen').exists())
def kadaster_ettingebos(request):
    """
    """
    context = {}

    with open(os.path.join(os.path.dirname(__file__), 'data', 'ettingebos_parcels.geojson')) as f:
        ettingebos_parcels = json.load(f)
    context['ettingebos_parcels'] = json.dumps(ettingebos_parcels)

    # with open(os.path.join(os.path.dirname(__file__), 'data', 'gondebeek_perimeter.geojson')) as f:
    #     gondebeek_perimeter = json.load(f)
    # context['gondebeek_perimeter'] = json.dumps(gondebeek_perimeter)

    return render(request, 'admin/kadaster_ettingebos.htm', context=context)


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Rodeland').exists())
def rodeland(request):
    """
    """
    context = {}

    with open(os.path.join(os.path.dirname(__file__), 'data', 'rodeland.geojson')) as f:
        parcels = json.load(f)
    context['parcels'] = json.dumps(parcels)

    return render(request, 'admin/rodeland.htm', context=context)


# def emails(request):
#     """
#     """
#     emails = [s.email for s in Subscription.objects.all()]
#     s = '\n'.join(emails)
#     return HttpResponse(s, content_type='text/plain')


def overzet(request):
    """
    """
    data = Input.objects.annotate(year=TruncYear('date')).order_by().values('year').annotate(toads=Sum('toads'), frogs=Sum('frogs'), salamanders=Sum('salamanders')).order_by('-year')
    locations = Input.objects.order_by().values('location').distinct()
    data_locations = {}
    for location in locations:
        qs = Input.objects.filter(location=location['location']).annotate(year=TruncYear('date')).order_by().values('year').annotate(toads=Sum('toads'), frogs=Sum('frogs'), salamanders=Sum('salamanders')).order_by('-year')
        data_locations[Input.LOCATIONS[location['location']-1]] = qs
    return render(request, 'admin/overzet.htm', context={'data': data, 'locations': data_locations})


def overzet_download(request, location, year):
    """
    """
    location_name = {'1': 'Lembergestraat', '2': 'Hoek ter Hulst'}[str(location)]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="overzet_%s_%s.csv"' % (location_name, year)
    writer = csv.writer(response)
    writer.writerow(['date', 'toads', 'frogs', 'salamanders', 'toads_death', 'frogs_death', 'salamanders_death'])

    items = Input.objects.filter(location=location, date__year=year).values_list('date', 'toads', 'frogs', 'salamanders', 'toads_death', 'frogs_death', 'salamanders_death')
    for item in items:
        writer.writerow(item)

    return response


class MyAdminSite(AdminSite):
    """
    """
    site_header = 'Natuurpunt Oosterzele Admin'
    site_title = 'NPO Admin'
    index_title = 'Sitebeheer'

    def get_urls(self):
        """
        """
        urls = [
            path('dashboard/', dashboard),
            path('overzet/download/<int:location>/<int:year>/', overzet_download),
            path('perceel/<str:key>/', perceel),
            path('eigenaar/<int:id>/', eigenaar),
            path('kadaster/', kadaster_gondebeekvallei),
            path('kadaster/gondebeekvallei', kadaster_gondebeekvallei),
            path('kadaster/ettingebos', kadaster_ettingebos),
            # path('emails/', emails),
            path('overzet/', overzet),
            path('rodeland/', rodeland),
            ]
        return super().get_urls() + urls


admin_site = MyAdminSite()

admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
