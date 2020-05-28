from django.utils import timezone
import django_filters
from django_filters import DateFilter

from .models import *


class OrderFilter(django_filters.FilterSet):
    hours = django_filters

    def get_past_n_hours(self, queryset, field_name, value):
        time_threshold = timezone.now() - timedelta(hours=int(value))
        return queryset.filter(time_stamp__gte=time_threshold)

    class Meta:
        model = Order
        fields = ['product', 'status']
