from django.contrib import admin
from .models import Date, Period


class DateAdmin(admin.ModelAdmin):
    pass


class PeriodAdmin(admin.ModelAdmin):
    pass


admin.site.register(Date, DateAdmin)
admin.site.register(Period, PeriodAdmin)
