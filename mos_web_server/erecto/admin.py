from django.contrib import admin

from mos_web_server.erecto.models import MethodType, AnalysisType, Source, Matrix, Eluent, Unit, ConcUnit


# Register your models here.
class TagLikeAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('id', 'name', 'desc', 'activated', 'updated', 'created',)
    list_display_links = ['id', ]
    fields = [('name', 'activated'), 'description', ]
    search_fields = ('id', 'name', 'description',)
    search_help_text = 'Search: id, name, description'
    pass


@admin.register(MethodType)
class MethodTypeAdmin(TagLikeAdmin):
    pass


@admin.register(AnalysisType)
class AnalysisTypeAdmin(TagLikeAdmin):
    pass


@admin.register(Matrix)
class MatrixAdmin(TagLikeAdmin):
    pass


@admin.register(Source)
class SourceAdmin(TagLikeAdmin):
    pass


@admin.register(Eluent)
class EluentAdmin(TagLikeAdmin):
    pass


@admin.register(Unit)
class UnitAdmin(TagLikeAdmin):
    pass


@admin.register(ConcUnit)
class ConcUnitAdmin(TagLikeAdmin):
    pass
