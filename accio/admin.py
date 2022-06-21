from admin_ordering.admin import OrderableAdmin
from django import forms
from django.contrib import admin
from django.db.models import JSONField
from django.utils.translation import gettext_lazy as _
from django_json_widget.widgets import JSONEditorWidget

from accio.form import CompoundForm, CartridgeForm
from accio.models import Cartridge, Compound, CompoundCodeCounter, CompoundTag, SpectrumTag, \
    Spectrum, QuantMethod, Experiment, QuantMethodCodeCounter, next_quant_method_code
from erecto.admin import TagLikeAdmin


# Register your models here.
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


@admin.register(Cartridge)
class CartridgeAdmin(BaseAdmin):
    ordering = ['id']
    list_display = ('id', 'code', 'source', 'polarity', 'analysis_type', 'activated', 'updated',)
    list_display_links = ['id', ]
    search_fields = ('id', 'code', 'analysis_type__name__icontains', 'description',)
    search_help_text = 'Search: id, code, analysis_type, description'

    form = CartridgeForm

    fieldsets = (
        (None, {
            'fields': (('code', 'source', 'polarity',), 'analysis_type',
                       ('pre_spary_time', 'spray_voltage_pos', 'spray_voltage_neg',), 'description', 'activated',)
        }),
        (_('targets'), {
            'classes': ('collapse',),
            'fields': ('compound',),
        }),
        (_('dda tags'), {
            'classes': ('collapse',),
            'fields': ('compound_tag',),
        }),
        (_('quant methods'), {
            'classes': ('collapse',),
            'fields': ('quant_method',),
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': (('code', 'source', 'polarity',), 'analysis_type',
                       ('pre_spary_time', 'spray_voltage_pos', 'spray_voltage_neg',), 'description', 'activated',)
        }),
    )

    targeted_fieldsets = (
        (None, {
            'fields': (('code', 'source', 'polarity',), 'analysis_type',
                       ('pre_spary_time', 'spray_voltage_pos', 'spray_voltage_neg',), 'description', 'activated',)
        }),
        (_('targets'), {
            # 'classes': ('collapse', ),
            'fields': ('compound',),
        }),
    )

    dda_fieldsets = (
        (None, {
            'fields': (('code', 'source', 'polarity',), 'analysis_type',
                       ('pre_spary_time', 'spray_voltage_pos', 'spray_voltage_neg',), 'description', 'activated',)
        }),
        (_('dda tags'), {
            # 'classes': ('collapse', ),
            'fields': ('compound_tag',),
        })
    )

    targeted_quant_fieldsets = (
        (None, {
            'fields': (('code', 'source', 'polarity',), 'analysis_type',
                       ('pre_spary_time', 'spray_voltage_pos', 'spray_voltage_neg',), 'description', 'activated',)
        }),
        (_('quant methods'), {
            # 'classes': ('collapse', ),
            'fields': ('quant_method',),
        }),
    )

    filter_horizontal = (
        'compound_tag',
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        else:
            if obj.analysis_type.name == 'Calibration':
                return self.add_fieldsets
            elif obj.analysis_type.name == 'Targeted' or obj.analysis_type.name == 'Targeted_pro':
                return self.targeted_fieldsets
            elif obj.analysis_type.name == 'DDA':
                return self.dda_fieldsets
            elif obj.analysis_type.name == 'Targeted_quant':
                return self.targeted_quant_fieldsets
            return super().get_fieldsets(request, obj)

    pass


class SpectrumInline(admin.TabularInline):
    model = Spectrum
    fields = ('id', 'precursor_mz', 'method_type', 'polarity', 'cid_q', 'cid_amp', 'activated', 'ordering',)
    readonly_fields = ('id', 'precursor_mz', 'method_type', 'polarity', 'cid_q', 'cid_amp', 'activated',)
    extra = 0
    pass


class SpectrumNoChangeInline(OrderableAdmin, SpectrumInline):

    def has_add_permission(self, request, obj=None):
        return False

    pass


class SpectrumReadOnlyInline(OrderableAdmin, SpectrumInline):
    pass


class ExperimentInline(admin.TabularInline):
    model = Experiment
    fields = (
        'id', 'source', 'device', 'activated',)
    extra = 0
    pass


@admin.register(CompoundTag)
class CompoundTagAdmin(TagLikeAdmin):
    pass


@admin.register(Compound)
class CompoundAdmin(BaseAdmin):
    ordering = ['id']
    list_display = ('id', 'code', 'name_cn', 'name_en', 'cas', 'mass', 'formula', 'activated', 'updated',)
    search_fields = ('id', 'code', 'name_cn', 'name_en', 'cas', 'mass', 'formula',)
    search_help_text = 'Search: id, code, name_cn, name_en, cas, mass, formula'

    form = CompoundForm

    fieldsets = (
        (None, {
            'fields': (('code', 'activated',), ('name_cn', 'name_en',), ('cas', 'mass', 'formula',),)
        }),
        (_('detail description'), {
            'classes': ('collapse',),
            'fields': (
                'description', ('chemical_prop', 'physical_prop',), ('structural_formula', 'safety_data_sheet',),
                'extra_data',),
        }),
    )

    inlines = [ExperimentInline, SpectrumNoChangeInline, ]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            CompoundCodeCounter.objects.create()

    pass


@admin.register(Experiment)
class ExperimentAdmin(BaseAdmin):
    ordering = ['id']
    fields = (
        ('compound', 'source',),
        ('device', 'location',),
        ('temperature', 'humidity',),
        'description',)
    list_display = ('id', 'compound', 'source', 'device', 'location', 'description',)
    autocomplete_fields = ('compound', 'source',)
    inlines = [SpectrumReadOnlyInline, ]
    pass


@admin.register(SpectrumTag)
class SpectrumTagAdmin(TagLikeAdmin):
    pass


@admin.register(Spectrum)
class SpectrumAdmin(BaseAdmin):
    ordering = ['id']
    list_display = ('id', 'compound', 'precursor_mz', 'method_type', 'polarity', 'peaks', 'average', 'activated',)
    fieldsets = (
        (None, {
            'fields': (
                ('compound', 'precursor_mz',),
                ('experiment', 'inj_lmco_mz',),
                ('method_type', 'polarity',),
                ('average', 'cid_q', 'cid_amp',),
                ('iso1_amp', 'iso2_amp',),
                ('scan_mass_start', 'scan_mass_end',),
                'peaks', 'spectrum_tag',)
        }),
        (_('detail description'), {
            'classes': ('collapse',),
            'fields': (
                'description',
                'extra_params',),
        }),
    )
    pass


class QuantMethodForm(forms.ModelForm):
    class Meta:
        model = QuantMethod
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(QuantMethodForm, self).__init__(*args, **kwargs)
        if self.initial.get('code') is None:
            self.initial['code'] = next_quant_method_code
        self.fields['code'].widget.attrs['readonly'] = True
        self.fields['code'].help_text = _('auto-generated non-editable')

    pass


@admin.register(QuantMethod)
class QuantMethodAdmin(BaseAdmin):
    ordering = ['id']
    fields = (
        ('code', 'quant_type',),
        ('target_spectrum', 'in_std_spectrum',),
        'description',)

    form = QuantMethodForm

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            QuantMethodCodeCounter.objects.create()

    pass
