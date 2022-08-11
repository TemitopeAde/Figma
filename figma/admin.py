from django.contrib import admin
from .models import Hashes, Stories, SourceModel

# Register your models here.


class StoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ['status']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ['title']}


class SourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ['title']


class HashAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    prepopulated_fields = {'slug': ['title']}


admin.site.register(Stories, StoriesAdmin)
admin.site.register(SourceModel, SourceAdmin)
admin.site.register(Hashes, HashAdmin)
