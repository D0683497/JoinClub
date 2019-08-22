from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    search_fields = ('nid',)

admin.site.register(Member, MemberAdmin)
