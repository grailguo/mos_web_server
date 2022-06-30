from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from mos_web_server.users.api.views import UserViewSet, GroupViewSet, OrganizationViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("organizations", OrganizationViewSet)
router.register("groups", GroupViewSet)
router.register("users", UserViewSet)

urlpatterns = router.urls
