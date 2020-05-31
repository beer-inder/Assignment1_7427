from django.contrib import admin
from .models import extendeduser, child, activity, guardian, newsletter, notification


class ExtenduserAdmin(admin.ModelAdmin):
    pass


class ChildAdmin(admin.ModelAdmin):
    list_display = ('child_name', 'parent')

    list_select_related = (
        'user', 'guardian_name'
    )

    search_fields = ('nationality',)
    readonly_fields = ["child_age", ]

    def parent(self, obj):
        return obj.user


class Activity(admin.ModelAdmin):
    list_display = ('activity_name', 'activity_Date')
    search_fields = ('activity_name', 'activity_Date',)
    filter_horizontal = ('children_list',)


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added')


admin.site.register(extendeduser, ExtenduserAdmin)
admin.site.register(child, ChildAdmin)
admin.site.register(activity, Activity)
admin.site.register(guardian)
admin.site.register(newsletter, NewsletterAdmin)
admin.site.register(notification)
admin.site.site_header = 'Administration'
