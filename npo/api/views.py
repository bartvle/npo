"""
"""


import datetime

from rest_framework import serializers, viewsets

from activities.models import Activity


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity


class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        """
        """
        ## All activities
        queryset = Activity.objects.all().order_by('date')

        date = self.request.query_params.get('date', None)
        slug = self.request.query_params.get('slug', None)

        ## One activity (should be placed in a get function)
        if date is not None and slug is not None:
            queryset = queryset.filter(date=date)
            queryset = queryset.filter(slug=slug)
            return queryset

        ## All future activities
        if date == 'future':
            queryset = queryset.filter(date__gte=datetime.date.today())

        ## Limit number
        limit = self.request.query_params.get('limit', None)
        if limit is not None:
            queryset = queryset[:int(limit)]

        return queryset
