from django_filters import rest_framework as filters

from mos_web_server.users.models import Organization


class OrganizationFilter(filters.FilterSet):
    class Meta:
        model = Organization
        fields = ('name', )

    pass
