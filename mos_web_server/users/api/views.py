from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response

from .filters import OrganizationFilter
from .serializers import UserSerializer, OrganizationSerializer, GroupSerializer
from ..models import Organization

User = get_user_model()


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all().order_by('id')
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = OrganizationFilter
    search_fields = ['name', ]
    pass


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    pass


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    pass
