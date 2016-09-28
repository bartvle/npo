"""
"""


from rest_framework import serializers, viewsets

from activities.models import Activity


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity


class ActivityViewSet(viewsets.ModelViewSet):
    #queryset = Activity.objects.all().order_by('date')
    serializer_class = ActivitySerializer

    def get_queryset(self):
        queryset = Activity.objects.all().order_by('date')
        date = self.request.query_params.get('date', None)
        slug = self.request.query_params.get('slug', None)
        if date is not None:
            queryset = queryset.filter(date=date)
        if slug is not None:
            queryset = queryset.filter(slug=slug)
        return queryset
