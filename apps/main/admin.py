from django.contrib import admin
from apps.main.models import Page


@admin.register(Page)
class PAgeAdmin(admin.ModelAdmin):
    pass

