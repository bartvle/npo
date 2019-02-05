"""
"""


import json
import os

from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.db.models import Sum
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.functions import TruncYear


from register.models import Parcel
from newsletter.models import Subscription
from amphi.models import Input


@login_required
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
def kadaster(request):
    """
    """
    with open(os.path.join(os.path.dirname(__file__), '.', 'data', 'gondebeek_parcels.geojson')) as f:
        gondebeek_parcels = json.load(f)

    context = {'gondebeek_parcels': json.dumps(gondebeek_parcels)}

    return render(request, 'admin/kadaster.htm', context=context)


@login_required
def emails(request):
    """
    """
    emails = [s.email for s in Subscription.objects.all()]
    s = '\n'.join(emails)
    return HttpResponse(s, content_type='text/plain')


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
            path('perceel/<int:oidn>/', perceel),
            path('kadaster/', kadaster),
            path('emails/', emails),
            path('overzet/', overzet),
            ]
        return super().get_urls() + urls


admin_site = MyAdminSite()

admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
