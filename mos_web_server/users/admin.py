from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.db.models import JSONField
from django.utils.translation import gettext_lazy as _
from django_json_widget.widgets import JSONEditorWidget

from mos_web_server.users.forms import UserAdminChangeForm, UserAdminCreationForm
from mos_web_server.users.models import Organization

User = get_user_model()


class BaseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget}
    }

    save_as = True

    def get_queryset(self, request):
        if request.user.organization is None:
            queryset = super().get_queryset(request)
        else:
            queryset = super().get_queryset(request).filter(organization=request.user.organization)
        return queryset

    pass


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('id', 'name', 'desc', 'activated', 'updated', 'created',)
    fields = (('name', 'activated',), 'description',)
    search_fields = ('id', 'name', 'description',)
    search_help_text = 'Search: id, name, description'
    pass


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]
