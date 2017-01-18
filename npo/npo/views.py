"""
"""


import datetime
import os

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.shortcuts import render

from npo.settings import BASE_DIR
from news.models import Article
from activities.models import Activity


@ensure_csrf_cookie
def start(request):
    """
    """
    activities = Activity.objects.all().filter(date__gte=datetime.date.today()).order_by('date')[:3]
    context = {'activities': activities}
    return render(request, 'start.htm', context=context)


@ensure_csrf_cookie
def over_ons(request):
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
def nieuws(request):
    """
    """
    articles = Article.objects.all().order_by('-date')
    context = {'articles': articles}
    return render(request, 'articles.htm', context=context)


@ensure_csrf_cookie
def artikel(request, year, month, day, slug):
    """
    """
    date = datetime.date(int(year), int(month), int(day))
    article = Article.objects.get(date=date, slug=slug)
    return render(request, 'article.htm', context={'article': article})


@ensure_csrf_cookie
def e_nieuwsbrief(request):
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
def lid_worden(request):
    """
    """
    return render(request, 'lidworden.htm')
