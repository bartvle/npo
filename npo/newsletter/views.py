"""
"""


import json

from django.http import HttpResponse

from .models import Subscription


def subscribe(request):
    """
    """
    email = json.loads(request.body.decode('utf-8'))['adress']
    try:
        s = Subscription.objects.get(email=email)
    except Subscription.DoesNotExist:
        s = Subscription(email=email)
        s.save()
        return HttpResponse('Bedankt, je bent ingeschreven!')
    else:
        return HttpResponse('Je bent reeds ingeschreven!')
