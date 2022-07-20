from django.conf import settings
from rest_framework.routers import DefaultRouter

from mos_web_server.accio.api.views import CompoundTagViewSet, CompoundViewSet, ExperimentViewSet, SpectrumTagViewSet, \
    SpectrumViewSet, QuantMethodViewSet, CartridgeViewSet
from mos_web_server.erecto.api.views import MethodTypeViewSet, AnalysisTypeViewSet, MatrixViewSet, SourceViewSet, \
    EluentViewSet, UnitViewSet, ConcUnitViewSet
from mos_web_server.flagrate.views import DataTagViewSet, CaseViewSet, SubstanceViewSet, DataViewSet
from mos_web_server.reparo.api.views import DeviceViewSet
from mos_web_server.users.api.views import UserViewSet, GroupViewSet, OrganizationViewSet

# Current only use DefaultRouter in dev and prod by guo liang at 2022-07-20
if settings.DEBUG:
    router = DefaultRouter()
else:
    # router = SimpleRouter()
    router = DefaultRouter()

router.register("organizations", OrganizationViewSet)
router.register("groups", GroupViewSet)
router.register("users", UserViewSet)

router.register('method_types', MethodTypeViewSet)
router.register('analysis_types', AnalysisTypeViewSet)
router.register('matrixs', MatrixViewSet)
router.register('sources', SourceViewSet)
router.register('eluents', EluentViewSet)
router.register('units', UnitViewSet)
router.register('conc_units', ConcUnitViewSet)

router.register('devices', DeviceViewSet)

router.register('compound_tags', CompoundTagViewSet)
router.register('compounds', CompoundViewSet)
router.register('experiments', ExperimentViewSet)
router.register('spectrum_tags', SpectrumTagViewSet)
router.register('spectra', SpectrumViewSet)
router.register('quant_methods', QuantMethodViewSet)
router.register('cartridges', CartridgeViewSet)

router.register('cases', CaseViewSet)
router.register('substances', SubstanceViewSet)
router.register('data_tags', DataTagViewSet)
router.register('data', DataViewSet)

urlpatterns = router.urls
