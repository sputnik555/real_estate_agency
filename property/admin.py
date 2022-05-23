from django.contrib import admin

from .models import Flat


class Admin(admin.ModelAdmin):
    search_fields = ['town', 'owner', 'address']
    readonly_fields = ['created_at']


admin.site.register(Flat, Admin)
