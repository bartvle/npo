"""
"""


import os

from django.http import JsonResponse
from django.shortcuts import render

from npo.settings import BASE_DIR


def index(request):
    """
    """
    return render(request, 'index.htm')


def api_magazine(request):
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
    return JsonResponse(data[::-1], safe=False)
