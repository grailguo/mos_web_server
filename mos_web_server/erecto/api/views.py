from rest_framework import viewsets, permissions

from mos_web_server.erecto.api.serializers import MethodTypeSerializer, AnalysisTypeSerializer, \
    MatrixSerializer, SourceSerializer, EluentSerializer, UnitSerializer, ConcUnitSerializer
from mos_web_server.erecto.models import MethodType, AnalysisType, Matrix, Source, Eluent, Unit, ConcUnit


# Create your api views here.
class MethodTypeViewSet(viewsets.ModelViewSet):
    queryset = MethodType.objects.all().order_by('id')
    serializer_class = MethodTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    pass


class AnalysisTypeViewSet(viewsets.ModelViewSet):
    queryset = AnalysisType.objects.all().order_by('id')
    serializer_class = AnalysisTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    pass


class MatrixViewSet(viewsets.ModelViewSet):
    queryset = Matrix.objects.all().order_by('id')
    serializer_class = MatrixSerializer
    permission_classes = [permissions.IsAuthenticated]
    pass


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all().order_by('id')
    serializer_class = SourceSerializer
    permission_classes = [permissions.IsAuthenticated]
    pass


class EluentViewSet(viewsets.ModelViewSet):
    queryset = Eluent.objects.all().order_by('id')
    serializer_class = EluentSerializer
    permission_classes = [permissions.IsAuthenticated]
    pass


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all().order_by('id')
    serializer_class = UnitSerializer
    permission_classes = [permissions.IsAuthenticated]
    pass


class ConcUnitViewSet(viewsets.ModelViewSet):
    queryset = ConcUnit.objects.all().order_by('id')
    serializer_class = ConcUnitSerializer
    permission_classes = [permissions.IsAuthenticated]
    pass
