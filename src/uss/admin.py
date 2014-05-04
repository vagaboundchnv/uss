from django.contrib import admin
from uss.models import Tag, UrlDesc

class TagAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')

class UrlDescAdmin(admin.ModelAdmin):
    list_display = ('user', 'link', 'desc', 'title')
    
admin.site.register(Tag, TagAdmin)
admin.site.register(UrlDesc, UrlDescAdmin)