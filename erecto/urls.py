from django.urls import path, include
from rest_framework import routers

from erecto import views

router = routers.SimpleRouter()

router.register('method_types', views.MethodTypeViewSet)
router.register('analysis_types', views.AnalysisTypeViewSet)
router.register('matrixs', views.MatrixViewSet)
router.register('sources', views.SourceViewSet)
router.register('eluents', views.EluentViewSet)
router.register('units', views.UnitViewSet)
router.register('conc_units', views.ConcUnitViewSet)

urlpatterns = [
    path('erecto/', include(router.urls)),
]
