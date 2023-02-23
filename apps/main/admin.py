from django.contrib import admin
from apps.main.models import Page, Contact


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class PageAdmin(admin.ModelAdmin):
    pass

