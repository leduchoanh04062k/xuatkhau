from django.contrib import admin
from .models import *
from django.forms import CheckboxSelectMultiple


class ProvinceInline(admin.StackedInline):
    model = Province
    extra = 0

class CountryAdmin(admin.ModelAdmin):
    search_fields = ('name', 'slug')
    list_display = ('name', 'slug', 'show_home', 'is_japan')
    list_select_related = True
    list_per_page = 50
    list_filter = ('name',)
    list_editable = ['show_home', 'is_japan']
    inlines = (ProvinceInline, )  
        
admin.site.register(Country, CountryAdmin)

class ProvinceAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', 'active', 'updated')
    list_select_related = True
    list_per_page = 50
    list_filter = ('country',)
admin.site.register(Province, ProvinceAdmin)

class CityAdmin(admin.ModelAdmin):
    search_fields = ('name', 'slug')
    list_display = ('name', 'slug', 'active', 'updated')
    list_select_related = True
    list_per_page = 50
    list_filter = ('name',)
admin.site.register(City, CityAdmin)