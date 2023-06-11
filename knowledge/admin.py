from django.contrib import admin
from .models import Knowledge


class KnowledgeAdmin(admin.ModelAdmin):
    # filter_horizontal = ("tag", "genre")
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Knowledge, KnowledgeAdmin)
