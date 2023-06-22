from django.contrib import admin
from .models import Date, Period


class DateAdmin(admin.ModelAdmin):
    display_fields = "date"


class PeriodAdmin(admin.ModelAdmin):
    # filter_horizontal = ("tag", "genre")
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Date, DateAdmin)
admin.site.register(Period, PeriodAdmin)
