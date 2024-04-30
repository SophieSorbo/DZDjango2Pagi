from django_filters import rest_framework as filters

from advertisements.models import Advertisement
from django_filters import DateFromToRangeFilter, ChoiceFilter, ModelChoiceFilter
from rest_framework.authtoken.admin import User

from .models import AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    # TODO: задайте требуемые фильтры
    creator = filters.ModelChoiceFilter(field_name='creator', queryset=User.objects.all())
    status = ChoiceFilter(field_name='status', choices=AdvertisementStatusChoices.choices)
    date = DateFromToRangeFilter()
    class Meta:
        model = Advertisement
        fields = ['status', 'date', 'creator']
