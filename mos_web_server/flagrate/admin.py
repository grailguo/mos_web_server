from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Register your models here.
from mos_web_server.erecto.admin import TagLikeAdmin
from mos_web_server.flagrate.models import DataTag, Substance, Case, Data
from mos_web_server.users.admin import BaseAdmin


@admin.register(DataTag)
class DataTagAdmin(TagLikeAdmin):
    pass


class SubstanceInline(admin.TabularInline):
    model = Substance
    list_display = ('id', 'case', 'compound', 'concentration', 'conc_unit', 'organization',)
    fields = ('id', 'case', 'compound', 'concentration', 'conc_unit', 'organization', 'activated',)
    # classes = ['collapse']
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False

    pass


@admin.register(Case)
class CaseAdmin(BaseAdmin):
    ordering = ['id']
    list_display = ('id', 'case_code', 'matrix', 'cartridge', 'analysis_type', 'eluent',
                    'sample_amount', 'sample_unit', 'organization', 'desc', 'activated',)
    search_fields = ('id', 'matrix__name__icontains', 'cartridge__code__icontains',
                     'cartridge__analysis_type__name__icontains', 'eluent__name__icontains',)
    search_help_text = 'Search: id, matrix, cartridge, analysis_type, eluent'

    fieldsets = (
        (None, {
            'fields': (
                ('matrix', 'cartridge', 'activated',),
                ('eluent', 'sample_amount', 'sample_unit',),
                'organization', 'description',)
        }),
        (_('parameters settings'), {
            'classes': ('collapse',),
            'fields': ('algorithm_parameters', 'analysis_parameters', 'config_parameters',)
        }),
        (_('expected result settings'), {
            'classes': ('collapse',),
            'fields': ('expected_result',)
        }),
    )
    autocomplete_fields = ('matrix', 'eluent',)
    inlines = [SubstanceInline, ]
    pass


# Show Substances in inlines of the CaseAdmin
# @admin.register(Substance)
class SubstanceAdmin(BaseAdmin):
    ordering = ['id']
    list_display = ('id', 'case', 'compound', 'compound_name', 'concentration', 'conc_unit', 'activated',)
    fields = [('case', 'compound', 'activated'), ('concentration', 'conc_unit'), ]
    pass


@admin.register(Data)
class DataAdmin(BaseAdmin):
    ordering = ['id']
    list_display = ('id', 'case', 'device', 'status', 'data_tag_list', 'mrzfile',)
    list_display_links = ['id', ]
    search_fields = ('case__id__icontains', 'device__sn__icontains', 'data_tags__name__icontains',)
    search_help_text = 'Search: case, device_sn, data_tag_list'
    fieldsets = (
        (None, {
            'fields': (('case', 'device',), ('mrzfile', 'status',), 'activated', 'data_tags',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('data_info', 'result',),
        }),
    )
    autocomplete_fields = ('case', 'device',)
    filter_horizontal = ('data_tags',)

    pass
