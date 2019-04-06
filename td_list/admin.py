import csv

from django.contrib import admin
from django.http import HttpResponse

from td_list.models import TicketActivity


@admin.register(TicketActivity)
class TicketActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'is_delete',
                    'created_at', 'modified_at',)
    search_fields = ('title', 'description', 'status', 'is_delete',)

    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = (
            'attachment; filename={}.csv'.format(meta)
        )
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = 'Export Selected'
