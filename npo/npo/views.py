"""
"""


import datetime
import os

from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render
from django.db.models import Sum

from npo.settings import BASE_DIR
from news.models import Article
from activities.models import Activity, NeighboringActivity
from magazine.models import Volume
from amphi.models import Input

from newsletter.models import Subscription
from newsletter.forms import NewsletterForm


def start(request):
    """
    """
    newsletter_message = None
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            # newsletter_message = 'Je bent reeds ingeschreven!'
            form.save()
            newsletter_message = 'Bedankt, je bent ingeschreven!'
    else:
        form = NewsletterForm()

    activities = Activity.objects.all().filter(date__gte=datetime.date.today(), published=True).order_by('date')[:3]
    transfer = {}
    transfer['toads'] = Input.objects.filter(date__year=2017).aggregate(Sum('toads'))['toads__sum']
    transfer['frogs'] = Input.objects.filter(date__year=2017).aggregate(Sum('frogs'))['frogs__sum']
    transfer['salamanders'] = Input.objects.filter(date__year=2017).aggregate(Sum('salamanders'))['salamanders__sum']
    context = {'activities': activities, 'transfer': transfer}
    context['form'] = form
    context['newsletter_message'] = newsletter_message
    return render(request, 'start.htm', context=context)


def over_ons(request):
    """
    """
    return render(request, 'overons.htm')


def beleid(request):
    """
    """
    return render(request, 'beleid.htm')


def natuurgebieden(request):
    """
    """
    return render(request, 'natuurgebieden.htm')


def soortbescherming(request):
    """
    """
    return render(request, 'soortbescherming.htm')


def activiteiten(request):
    """
    """
    activities = Activity.objects.all().filter(date__gte=datetime.date.today(), published=True).order_by('date')
    context = {'activities': activities}
    return render(request, 'activiteiten.htm', context=context)


def activiteit(request, year, month, day, slug):
    """
    """
    date = datetime.date(int(year), int(month), int(day))
    activity = Activity.objects.get(date=date, slug=slug)
    recent_activities = Activity.objects.all().filter(date__gte=datetime.date.today()).exclude(id=activity.id).order_by('date')[:3]
    return render(request, 'activiteit.htm', context={'activity': activity, 'recent_activities': recent_activities})


def nieuws(request):
    """
    """
    articles = Article.objects.all().order_by('-date')
    context = {'articles': articles}
    return render(request, 'articles.htm', context=context)


def artikel(request, year, month, day, slug):
    """
    """
    date = datetime.date(int(year), int(month), int(day))
    article = Article.objects.get(date=date, slug=slug)
    return render(request, 'article.htm', context={'article': article})


def magazine(request):
    """
    """
    volumes = Volume.objects.all()
    context = {'volumes': volumes}
    return render(request, 'magazine.htm', context=context)


def lid_worden(request):
    """
    """
    return render(request, 'lidworden.htm')


def gluren_bij_de_buren(request):
    """
    """
    activities = NeighboringActivity.objects.all().filter(date__gte=datetime.date.today()).order_by('date')
    our_activities = Activity.objects.all().filter(date__gte=datetime.date.today()).order_by('date')[:3]
    return render(request, 'gluren_bij_de_buren.htm', context={'activities': activities, 'our_activities': our_activities})


def kaart_regionaal_bos(request):
    """
    """
    return render(request, 'kaart_regionaal_bos.htm')
