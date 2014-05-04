from django.contrib import admin

from suit.admin import SortableModelAdmin
from mptt.admin import MPTTModelAdmin

from .models import Ad, CompanyStructure, Contest, News, Vacation, User


admin.site.register(Ad)
admin.site.register(Contest)
admin.site.register(News)
admin.site.register(Vacation)
admin.site.register(User)


class CompanyStructureAdmin(MPTTModelAdmin, SortableModelAdmin):
    mptt_level_indent = 20
    list_display = ('name',)
    sortable = 'order'
admin.site.register(CompanyStructure, CompanyStructureAdmin)