from django.contrib import admin
from django.utils.html import format_html
from .models import Team


class TeamAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width= "40" style="border-radius: 50px;"/>'.format(obj.photo.url))

    image_tag.short_description = 'Image'

    list_display = ('id','image_tag', 'first_name','last_name', 'designation', 'created_date')
    list_display_links = ('id','image_tag','first_name', 'designation')
    list_filter = ('designation',)
    search_fields = ('first_name', 'last_name')
    #list_editable = ('last_name',)

admin.site.register(Team,TeamAdmin)
