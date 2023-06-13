from django.contrib import admin
from .models import Country, Location


class CountryAdmin(admin.ModelAdmin):
    pass


class LocationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Country, CountryAdmin)
admin.site.register(Location, LocationAdmin)
