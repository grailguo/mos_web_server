from django_filters import rest_framework as filters

from mos_web_server.flagrate.models import Data


class DataFilter(filters.FilterSet):
    class Meta:
        model = Data
        fields = ('case__id', 'device__sn', 'data_tags__name',)

    pass
