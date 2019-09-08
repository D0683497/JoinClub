from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Attend

class AttendAdmin(ImportExportModelAdmin):
    search_fields = ('name', 'nid',)

admin.site.register(Attend, AttendAdmin)

