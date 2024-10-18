import django_filters
from .models import Gadget


class FishFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Gadget
        fields = ['price', 'name']