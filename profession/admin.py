from django.contrib import admin
from .models import *


class ProfessionAdmin(admin.ModelAdmin):
    search_fields = ('name', 'slug')
    list_display = ('name', 'slug', 'active', 'updated')
    list_select_related = True
    list_per_page = 50
    list_filter = ('name',)
        
admin.site.register(Profession, ProfessionAdmin)
