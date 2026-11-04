from django.contrib import admin
from organizations.models import Organization

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)


admin.site.register(Organization, OrganizationAdmin)