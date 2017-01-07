"""
"""


import datetime
import os

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.shortcuts import render

from npo.settings import BASE_DIR
from activities.models import Activity


@ensure_csrf_cookie
def start(request):
    """
    """
    activities = Activity.objects.all().filter(date__gte=datetime.date.today()).order_by('date')[:3]
    context = {'activities': activities}
    return render(request, 'start.htm', context=context)


@ensure_csrf_cookie
def overons(request):
    """
    """
    return render(request, 'overons.htm')


@ensure_csrf_cookie
def beleid(request):
    """
    """
    return render(request, 'beleid.htm')


@ensure_csrf_cookie
def natuurgebieden(request):
    """
    """
    return render(request, 'natuurgebieden.htm')


@ensure_csrf_cookie
def soortbescherming(request):
    """
    """
    return render(request, 'soortbescherming.htm')


@ensure_csrf_cookie
def activiteiten(request):
    """
    """
    activities = Activity.objects.all().filter(date__gte=datetime.date.today()).order_by('date')
    context = {'activities': activities}
    return render(request, 'activiteiten.htm', context=context)


@ensure_csrf_cookie
def activiteit(request, year, month, day, slug):
    """
    """
    date = datetime.date(int(year), int(month), int(day))
    activity = Activity.objects.get(date=date, slug=slug)
    return render(request, 'activiteit.htm', context={'activity': activity})


@ensure_csrf_cookie
def nieuwsbrief(request):
    """
    """
    folder = os.path.join(BASE_DIR, 'npo', 'static', 'magazine')
    data = []
    order = {'jan': 1, 'apr': 2, 'jul': 3, 'okt': 4}
    for year in os.listdir(folder)[::-1]:
        year_folder = os.path.join(folder, year)
        editions = []
        for edition in os.listdir(year_folder):
            editions.append(edition[:-8])
        editions.sort(key=lambda x: order[x[:3]])
        data.append({'year': year[:4], 'folder': year, 'editions': editions})
    data.sort(key=lambda x: x['year'])
    context = {'magazine': data[::-1]}
    return render(request, 'nieuwsbrief.htm', context=context)


@ensure_csrf_cookie
def lidworden(request):
    """
    """
    return render(request, 'lidworden.htm')
