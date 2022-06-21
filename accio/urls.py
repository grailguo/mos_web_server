from django.urls import path, include
from rest_framework import routers

from accio import views

router = routers.SimpleRouter()

router.register('compound_tags', views.CompoundTagViewSet)
router.register('compounds', views.CompoundViewSet)
router.register('experiments', views.ExperimentViewSet)
router.register('spectrum_tags', views.SpectrumTagViewSet)
router.register('spectra', views.SpectrumViewSet)
router.register('quant_methods', views.QuantMethodViewSet)
router.register('cartridges', views.CartridgeViewSet)

urlpatterns = [
    path('accio/', include(router.urls)),
]
