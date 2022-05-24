from django.contrib import admin

from .models import Flat


class Admin(admin.ModelAdmin):
    search_fields = ['town', 'owner', 'address']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year']
    list_editable = ['new_building']
    list_filter = ['new_building', 'has_balcony', 'rooms_number']


admin.site.register(Flat, Admin)
