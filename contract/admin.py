from django.contrib import admin
from .models import Project, Participantion, FundState, Performance
# Register your models here.
from import_export.admin import ImportExportModelAdmin


class ProjectAdmin(ImportExportModelAdmin):

    class Meta:
        model = Project


admin.site.register(Project, ProjectAdmin)
# admin.site.register(ProjectDoc)
admin.site.register(Participantion)
admin.site.register(FundState)
# admin.site.register(TongChou)
admin.site.register(Performance)
