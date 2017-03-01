"""
"""


import datetime
import os

from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render
from django.db.models import Sum

from npo.settings import BASE_DIR
from news.models import Article
from activities.models import Activity
from magazine.models import Volume
from amphi.models import Input


@ensure_csrf_cookie
def start(request):
    """
    """
    activities = Activity.objects.all().filter(date__gte=datetime.date.today()).order_by('date')[:3]
    transfer = {}
    transfer['toads'] = Input.objects.filter(date__year=2017).aggregate(Sum('toads'))['toads__sum']
    transfer['frogs'] = Input.objects.filter(date__year=2017).aggregate(Sum('frogs'))['frogs__sum']
    transfer['salamanders'] = Input.objects.filter(date__year=2017).aggregate(Sum('salamanders'))['salamanders__sum']
    context = {'activities': activities, 'transfer': transfer}
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
    recent_activities = Activity.objects.all().filter(date__gte=datetime.date.today()).exclude(id=activity.id).order_by('date')[:3]
    return render(request, 'activiteit.htm', context={'activity': activity, 'recent_activities': recent_activities})


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
    volumes = Volume.objects.all()
    context = {'volumes': volumes}
    return render(request, 'e_nieuwsbrief.htm', context=context)


@ensure_csrf_cookie
def lid_worden(request):
    """
    """
    return render(request, 'lidworden.htm')
