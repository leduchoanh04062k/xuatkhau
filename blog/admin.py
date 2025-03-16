from django.contrib import admin
from .models import *


class CateAdmin(admin.ModelAdmin):
    search_fields = ('name', 'slug')
    list_display = ('name', 'slug', 'updated')
    list_per_page = 50
admin.site.register(Cate, CateAdmin)


class BlogAdmin(admin.ModelAdmin):
    search_fields = ('name', 'slug')
    list_display = ('name', 'slug', 'active', 'updated')
    list_per_page = 50
    list_filter = ('cate',)
admin.site.register(Blog, BlogAdmin)

