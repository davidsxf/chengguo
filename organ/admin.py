from django.contrib import admin

# Register your models here.
from .models import Org, Participant, Department, Team
from import_export.admin import ImportExportModelAdmin

class OrgAdmin(ImportExportModelAdmin):

    class Meta:
        model = Org


class ParticipantAdmin(ImportExportModelAdmin):

    class Meta:
        model = Participant

class DepartmentAdmin(ImportExportModelAdmin):

    class Meta:
        model = Department

class TeamAdmin(ImportExportModelAdmin):

    class Meta:
        model = Team


admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Team, TeamAdmin)

admin.site.register(Org, OrgAdmin)
