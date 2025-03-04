"""
"""


import datetime
import json
import os

from django.shortcuts import render, redirect
from django.db.models import Sum

from news.models import Article
from activities.models import Activity
from magazine.models import Volume
from amphi.models import Input

# from newsletter.models import Subscription
# from newsletter.forms import NewsletterForm


def start(request):
    """
    """
    # newsletter_message = None
    # if request.method == 'POST':
    #     form = NewsletterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         newsletter_message = 'Bedankt, je bent ingeschreven!'
    # else:
    #     form = NewsletterForm()

    activities = Activity.objects.all().filter(date__gte=datetime.date.today(), published=True)[:4]
    articles =  Article.objects.all().filter(published=True)[:3]
    # transfer = {}
    # transfer['toads'] = Input.objects.filter(date__year=2017).aggregate(Sum('toads'))['toads__sum']
    # transfer['frogs'] = Input.objects.filter(date__year=2017).aggregate(Sum('frogs'))['frogs__sum']
    # transfer['salamanders'] = Input.objects.filter(date__year=2017).aggregate(Sum('salamanders'))['salamanders__sum']

    news = [{
        'time': datetime.datetime(2023, 9, 8, 14, 45, 0),
        'text': 'Aanstaande zaterdag beheermoment in Ettingebos! Op de agenda: opruimen van het sluikstort dat we recent ontdekten en verder afzetten van de jonge populierenscheuten.',
        'image': '/static/images/news/373713734_691285133043237_3203966118604969872_n.jpg',
    }]

    context = {
        'activities': activities,
        'articles': articles,
        'news': news,
#        'transfer': transfer,
        # 'form': form,
        # 'newsletter_message': newsletter_message,
        }

    return render(request, 'start.htm', context=context)


def over_ons(request):
    """
    """
    return render(request, 'over_ons.htm')


def beleid(request):
    """
    """
    return render(request, 'beleid.htm')


def natuurgebieden(request):
    """
    """
    return render(request, 'natuurgebieden.htm')

def natuurgebieden_gondebeekvallei_toegankelijkheid(request):
    """
    """
    return render(request, 'natuurgebieden_gondebeekvallei_toegankelijkheid.htm')

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
    recent_activities = Activity.objects.all().filter(
        date__gte=datetime.date.today(), published=True).exclude(
        id=activity.id).order_by('date')[:3]

    context = {'activity': activity, 'recent_activities': recent_activities}

    return render(request, 'activiteit.htm', context=context)


def nieuws(request):
    """
    """
    articles = Article.objects.all().filter(published=True).order_by('-date')
    context = {'articles': articles}
    return render(request, 'nieuws.htm', context=context)


def artikel(request, year, month, day, slug):
    """
    """
    date = datetime.date(int(year), int(month), int(day))
    try:
        article = Article.objects.get(date=date, slug=slug)
    except Article.DoesNotExist:
        return redirect('/')
    return render(request, 'artikel.htm', context={'article': article})


def lid_worden(request):
    """
    """
    return render(request, 'lid_worden.htm')


def steun_ons(request):
    """
    """
    return render(request, 'steun_ons.htm')


def doe_mee(request):
    """
    """
    return render(request, 'doe_mee.htm')


def rodeland(request):
    """
    """
    return render(request, 'rodeland.htm')


def rodeland_app(request):
    """
    """
    context = {}
    for name in ['perimeter', 'natura_2000']:
        with open(os.path.join(os.path.dirname(__file__), '.', 'data', '{}.geojson'.format(name))) as f:
            data = json.load(f)

        context[name] = json.dumps(data)

    return render(request, 'rodeland_app.htm', context=context)


def memorandum(request):
    """
    """
    return render(request, 'memorandum.htm')


def memorandum_nva(request):
    """
    """
    return render(request, 'memorandum_nva.htm')


def memorandum_groen(request):
    """
    """
    return render(request, 'memorandum_groen.htm')


def improvisatie(request):
    """
    """
    return redirect('/activiteiten/2020-05-16-het-is-onze-tweede-natuur')


def form_nieuwsbrief(request):
    """
    """
    return redirect('https://docs.google.com/forms/d/e/1FAIpQLScdCuXkYngEpTKqoIHm7gl3-IW05ogich8lq7IHMI1UfBDqgw/viewform')
