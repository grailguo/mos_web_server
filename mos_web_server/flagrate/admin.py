import json

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from mos_web_server.erecto.admin import TagLikeAdmin
from mos_web_server.flagrate.models import DataTag, Substance, Case, Data
from mos_web_server.users.admin import BaseAdmin


# Register your models here.
@admin.register(DataTag)
class DataTagAdmin(TagLikeAdmin):
    pass


class SubstanceInline(admin.TabularInline):
    model = Substance
    list_display = ('compound', 'concentration', 'conc_unit', 'organization',)
    fields = ('compound', 'concentration', 'conc_unit', 'organization', 'activated',)
    # classes = ['collapse']
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False

    pass


@admin.register(Case)
class CaseAdmin(BaseAdmin):
    ordering = ['id']
    list_display = ('case_code', 'matrix', 'cartridge', 'analysis_type', 'eluent',
                    'sample_amount', 'sample_unit', 'organization', 'desc', 'activated',)
    list_display_links = ['case_code', ]
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
            'fields': ('algorithm_data', 'algorithm_parameters', 'analysis_parameters',
                       'quant_methods', 'config_parameters',)
        }),
        (_('expected result settings'), {
            'classes': ('collapse',),
            'fields': ('expected_result',)
        }),
    )
    autocomplete_fields = ('matrix', 'eluent',)
    inlines = [SubstanceInline, ]

    def response_add(self, request, new_object, post_url_continue=None):
        obj = self.after_saving_model_and_related_inlines(new_object)
        return super(CaseAdmin, self).response_add(request, obj)

    def response_change(self, request, obj):
        obj = self.after_saving_model_and_related_inlines(obj)
        return super(CaseAdmin, self).response_change(request, obj)

    def after_saving_model_and_related_inlines(self, obj):
        substance_array = []
        for substance in self.inlines[0].model.objects.filter(case=obj):
            model_in_dict = model_to_dict(
                substance.compound, fields=["id", "code", "name_cn", "name_en", "mass", "cas", "formula"])
            substance_array.append(json.loads(json.dumps(model_in_dict, cls=DjangoJSONEncoder)))
        obj.expected_result = substance_array
        obj.save()
        return obj


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
    list_display = ('id', 'link_to_case', 'device', 'mrzfile', 'status', 'dbfile', 'db_version', 'data_tags',
                    'neg_compounds', 'pos_compounds',)
    list_display_links = ['id', ]
    search_fields = (
        'case__id__icontains', 'device__sn__icontains', 'datatag__name__icontains',
        'neg_compound__code__icontains', 'pos_compound__code__icontains',)
    search_help_text = 'Search: case, device_sn, data_tags, neg_compounds, pos_compounds'
    fieldsets = (
        (None, {
            'fields': (('case', 'device',), ('mrzfile', 'status',), ('dbfile', 'db_version',), 'activated',
                       'datatag', 'neg_compound', 'pos_compound',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('expected_result', 'analysis_result',),
        }),
    )
    autocomplete_fields = ('case', 'device',)
    filter_horizontal = ('datatag', 'neg_compound', 'pos_compound',)
    list_filter = ('case', 'device__sn', 'datatag',)

    def link_to_case(self, obj):
        link = reverse("admin:flagrate_case_change", args=[obj.case_id])
        return format_html('<a href="{}">CASE_#{}</a>', link, obj.case_id)

    link_to_case.short_description = _('case code')

    pass
