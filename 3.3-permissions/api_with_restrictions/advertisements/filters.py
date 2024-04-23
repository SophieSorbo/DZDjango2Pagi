from django_filters import rest_framework as filters

from advertisements.models import Advertisement
from django_filters import DateFromToRangeFilter, ChoiceFilter
from rest_framework.authtoken.admin import User

from .models import AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    # TODO: задайте требуемые фильтры
    creator = filters.ModelChoiceFilter(queryset=User.objects.all())
    status = ChoiceFilter(choices=AdvertisementStatusChoices.choices)
    date = DateFromToRangeFilter(field_name='created_at')
    class Meta:
        model = Advertisement
        fields = ['status', 'date', 'creator']
