from admin_ordering.admin import OrderableAdmin
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Register your models here.
from mos_web_server.accio.forms import CartridgeForm, QuantMethodForm, CompoundForm
from mos_web_server.accio.models import Cartridge, Spectrum, Experiment, CompoundTag, Compound, CompoundCodeCounter, \
    QuantMethod, QuantMethodCodeCounter, SpectrumTag
from mos_web_server.erecto.admin import TagLikeAdmin
from mos_web_server.users.admin import BaseAdmin


@admin.register(Cartridge)
class CartridgeAdmin(BaseAdmin):
    ordering = ['id']
    list_display = (
        'code', 'udi_di', 'source', 'polarity', 'analysis_type', 'organization', 'activated', 'updated',)
    list_display_links = ['code', ]
    search_fields = ('id', 'code', 'udi_di', 'analysis_type__name__icontains', 'description',)
    search_help_text = 'Search: id, code, udi_di, analysis_type, description'

    form = CartridgeForm

    fieldsets = (
        (None, {
            'fields': (('code', 'udi_di', 'source', 'polarity'), ('analysis_type', 'organization'),
                       ('pre_spary_time', 'spray_voltage_pos', 'spray_voltage_neg'), 'description', 'activated',)
        }),
        (_('targets'), {
            'classes': ('collapse',),
            'fields': ('compound',),
        }),
        (_('dda tags'), {
            'classes': ('collapse',),
            'fields': ('compoundtag',),
        }),
        (_('quant methods'), {
            'classes': ('collapse',),
            'fields': ('quantmethod',),
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': (('code', 'udi_di', 'source', 'polarity'), ('analysis_type', 'organization'),
                       ('pre_spary_time', 'spray_voltage_pos', 'spray_voltage_neg'), 'description', 'activated',)
        }),
    )

    targeted_fieldsets = (
        (None, {
            'fields': (('code', 'udi_di', 'source', 'polarity'), ('analysis_type', 'organization'),
                       ('pre_spary_time', 'spray_voltage_pos', 'spray_voltage_neg'), 'description', 'activated',)
        }),
        (_('targets'), {
            # 'classes': ('collapse',),
            'fields': ('compound',),
        }),
    )

    dda_fieldsets = (
        (None, {
            'fields': (('code', 'udi_di', 'source', 'polarity'), ('analysis_type', 'organization'),
                       ('pre_spary_time', 'spray_voltage_pos', 'spray_voltage_neg'), 'description', 'activated',)
        }),
        (_('dda tags'), {
            # 'classes': ('collapse',),
            'fields': ('compoundtag',),
        })
    )

    targeted_quant_fieldsets = (
        (None, {
            'fields': (('code', 'udi_di', 'source', 'polarity'), ('analysis_type', 'organization'),
                       ('pre_spary_time', 'spray_voltage_pos', 'spray_voltage_neg'), 'description', 'activated',)
        }),
        (_('quant methods'), {
            # 'classes': ('collapse',),
            'fields': ('quantmethod',),
        }),
    )

    filter_horizontal = (
        'compoundtag',
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
        print(self.model)
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
    list_display = ('code', 'name_cn', 'name_en', 'cas', 'mass', 'formula', 'activated', 'updated')
    list_display_links = ['code', ]
    search_fields = ('id', 'code', 'name_cn', 'name_en', 'cas', 'mass', 'formula')
    search_help_text = 'Search: id, code, name_cn, name_en, cas, mass, formula'

    form = CompoundForm

    fieldsets = (
        (None, {
            'fields': (('code', 'activated'), ('name_cn', 'name_en'), ('cas', 'mass', 'formula'), 'organization',)
        }),
        (_('detail description'), {
            'classes': ('collapse',),
            'fields': (
                'description', ('chemical_prop', 'physical_prop'), ('structural_formula', 'safety_data_sheet'),
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
    list_display = ('id', 'compound', 'precursor_mz', 'method_type', 'polarity', 'peaks', 'average', 'spectrum_tags', 'activated',)
    fieldsets = (
        (None, {
            'fields': (
                ('compound', 'precursor_mz',),
                ('experiment', 'inj_lmco_mz',),
                ('method_type', 'polarity',),
                ('average', 'cid_q', 'cid_amp',),
                ('iso1_amp', 'iso2_amp',),
                ('scan_mass_start', 'scan_mass_end',),
                'peaks', 'spectrumtag',)
        }),
        (_('detail description'), {
            'classes': ('collapse',),
            'fields': (
                'description',
                'extra_params',),
        }),
    )
    # list_filter = ('method_type', 'polarity', 'spectrumtag',)

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
