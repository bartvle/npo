"""
"""


from rest_framework import serializers, viewsets

from activities.models import Activity


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('date')
    serializer_class = ActivitySerializer
