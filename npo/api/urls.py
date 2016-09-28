"""
"""


from rest_framework import routers

from . import views


api_router = routers.DefaultRouter()
api_router.register(r'activities', views.ActivityViewSet, base_name='activities')
