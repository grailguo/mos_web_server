from django.contrib import admin

# Register your models here.
from mos_web_server.reparo.forms import DeviceForm
from mos_web_server.reparo.models import Device
from mos_web_server.users.admin import BaseAdmin


# Register your models here.
@admin.register(Device)
class DeviceAdmin(BaseAdmin):
    ordering = ['id']
    list_display = ('id', 'name', 'model', 'sn', 'organization', 'desc', 'activated', 'updated',)
    list_display_links = ['id', ]
    fields = [('name', 'activated',), ('model', 'sn'), 'organization', 'description', ]
    form = DeviceForm
    search_fields = ('id', 'name', 'model', 'sn', 'description',)
    search_help_text = 'Search: id, name, model, sn, description'
    pass
