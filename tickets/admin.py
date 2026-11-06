from django.contrib import admin
from tickets.models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'organization', 'assigned_to')
    list_filter = ('status', 'priority', 'organization')
    search_fields = ('title', 'description')
    list_select_related = ('organization', 'assigned_to')

admin.site.register(Ticket, TicketAdmin)
