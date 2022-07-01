from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

from mos_web_server.users.models import Organization

User = get_user_model()


# Create your api serializers here.
# Serializers define the API representation.
class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    activated = serializers.BooleanField(default=True, initial=True)

    class Meta:
        model = Organization
        fields = '__all__'

    pass


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name', ]

    pass


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name',
                  'email', 'groups', 'is_staff', 'is_active',
                  'last_login', 'date_joined', 'organization_id', ]

    pass
