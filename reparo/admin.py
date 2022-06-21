from django import forms
from django.contrib import admin

from reparo.models import Device

from django.db.models import JSONField
from django.utils.translation import gettext_lazy as _
from django_json_widget.widgets import JSONEditorWidget


class BaseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget}
    }

    save_as = True

    def get_queryset(self, request):
        pass

    # if request.user.organization is None:
    #     queryset = super().get_queryset(request)
    # else:
    #     queryset = super().get_queryset(request).filter(organization=request.user.organization)
    # return queryset

    pass


# Register your models here.
class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)

    pass


@admin.register(Device)
class DeviceAdmin(BaseAdmin):
    ordering = ['id']
    list_display = ('id', 'name', 'model', 'sn', 'desc', 'activated', 'updated',)
    list_display_links = ['id', ]
    fields = [('name', 'activated',), ('model', 'sn'), 'description', ]
    form = DeviceForm
    search_fields = ('id', 'name', 'model', 'sn', 'description',)
    search_help_text = 'Search: id, name, model, sn, description'
    pass
