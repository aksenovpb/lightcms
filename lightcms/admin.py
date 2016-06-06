from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from lightcms.admin_forms import PageAdminForm
from lightcms.models import Page, Module, Block, ModuleRelation


class PageAdmin(DjangoMpttAdmin):
    form = PageAdminForm


class BlockAdmin(admin.ModelAdmin):
    pass


class ModuleAdmin(admin.ModelAdmin):
    pass


class ModuleRelationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Page, PageAdmin)
admin.site.register(Block, BlockAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(ModuleRelation, ModuleRelationAdmin)
