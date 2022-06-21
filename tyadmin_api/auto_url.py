from tyadmin_api import auto_views
from django.urls import re_path, include, path
from rest_framework.routers import DefaultRouter
    
router = DefaultRouter(trailing_slash=False)
    
router.register('permission', auto_views.PermissionViewSet)
    
router.register('group', auto_views.GroupViewSet)
    
router.register('content_type', auto_views.ContentTypeViewSet)
    
router.register('method_type', auto_views.MethodTypeViewSet)
    
router.register('analysis_type', auto_views.AnalysisTypeViewSet)
    
router.register('matrix', auto_views.MatrixViewSet)
    
router.register('source', auto_views.SourceViewSet)
    
router.register('eluent', auto_views.EluentViewSet)
    
router.register('unit', auto_views.UnitViewSet)
    
router.register('conc_unit', auto_views.ConcUnitViewSet)
    
router.register('device', auto_views.DeviceViewSet)
    
router.register('compound_code_counter', auto_views.CompoundCodeCounterViewSet)
    
router.register('compound_tag', auto_views.CompoundTagViewSet)
    
router.register('compound', auto_views.CompoundViewSet)
    
router.register('experiment', auto_views.ExperimentViewSet)
    
router.register('spectrum_tag', auto_views.SpectrumTagViewSet)
    
router.register('spectrum', auto_views.SpectrumViewSet)
    
router.register('quant_method_code_counter', auto_views.QuantMethodCodeCounterViewSet)
    
router.register('quant_method', auto_views.QuantMethodViewSet)
    
router.register('cartridge', auto_views.CartridgeViewSet)
    
urlpatterns = [
        re_path('^', include(router.urls)),
    ]
    