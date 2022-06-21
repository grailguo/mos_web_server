from django.urls import path, include
from rest_framework import routers

from reparo import views

router = routers.SimpleRouter()

router.register('devices', views.DeviceViewSet)

urlpatterns = [
    path('reparo/', include(router.urls)),
]
