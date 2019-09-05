from django.contrib import admin
from .models import Member, Attend

class MemberAdmin(admin.ModelAdmin):
    search_fields = ('nid',)

class AttendAdmin(admin.ModelAdmin):
    search_fields = ('name', 'nid',)

admin.site.register(Member, MemberAdmin)
admin.site.register(Attend, AttendAdmin)
