# Create your views here.
from rest_framework import viewsets, permissions

from mos_web_server.flagrate.api.serializers import DataTagSerializer, SubstanceSerializer, CaseSerializer, \
    CaseWithSubstanceSerializer, DataSerializer, DataWithTagSerializer
from mos_web_server.flagrate.filters import DataFilter
from mos_web_server.flagrate.models import DataTag, Substance, Case, Data


class DataTagViewSet(viewsets.ModelViewSet):
    queryset = DataTag.objects.all().order_by('id')
    serializer_class = DataTagSerializer
    permission_classes = [permissions.IsAuthenticated]
    pass


class SubstanceViewSet(viewsets.ModelViewSet):
    queryset = Substance.objects.all().order_by('id')
    serializer_class = SubstanceSerializer
    permission_classes = [permissions.IsAuthenticated]
    pass


class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all().order_by('id')
    serializer_class = CaseSerializer
    search_fields = ['matrix__name__icontains', 'cartridge__code__icontains',
                     'cartridge__analysis_type__name__icontains', 'eluent__name__icontains', ]
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CaseWithSubstanceSerializer
        else:
            return self.serializer_class

    pass


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all().order_by('id')
    serializer_class = DataSerializer
    filterset_class = DataFilter
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return DataWithTagSerializer
        else:
            return self.serializer_class

    pass
