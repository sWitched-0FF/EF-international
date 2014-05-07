#coding:  utf-8
from django.contrib import admin

from suit.admin import SortableModelAdmin
from mptt.admin import MPTTModelAdmin

from .models import Ad, Calendar, CompanyStructure, Contest, News, Vacation


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('title',),}),
        (None, {
            'classes': ('full-width',),
            'fields': ('content',)
        }),
        (None, {'fields': ('is_active', 'is_publish'),}),
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(PageAdmin, self).save_model(request, obj, form, change)


class CalendarPageAdmin(PageAdmin):
    fieldsets = [
        (None, {'fields': ('title',),}),
        (None, {
            'classes': ('full-width',),
            'fields': ('content',)
        }),
        (None, {'fields': ( 'start_date',
                            'end_date',
                            'is_active',
                            'is_publish'),
        }),
    ]

admin.site.register(Ad, PageAdmin)
admin.site.register(Calendar, CalendarPageAdmin)
admin.site.register(Contest, PageAdmin)
admin.site.register(News, PageAdmin)
admin.site.register(Vacation)


class CompanyStructureAdmin(MPTTModelAdmin, SortableModelAdmin):
    mptt_level_indent = 20
    list_display = ('name',)
    sortable = 'order'
admin.site.register(CompanyStructure, CompanyStructureAdmin)