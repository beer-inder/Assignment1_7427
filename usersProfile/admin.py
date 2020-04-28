from django.contrib import admin
from .models import extendeduser, child


class ExtenduserAdmin(admin.ModelAdmin):
    pass


class ChildAdmin(admin.ModelAdmin):
    list_display = ('child_name', 'parent')

    def parent(self, obj):
        return obj.user


admin.site.register(extendeduser, ExtenduserAdmin)
admin.site.register(child, ChildAdmin)
admin.site.site_header =   'Administration'
