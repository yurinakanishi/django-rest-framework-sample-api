from django.contrib import admin
from .models import LivingThings, Habitat, Species


class LivingThingsAdmin(admin.ModelAdmin):
    # filter_horizontal = ("tag", "genre")
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


class HabitatAdmin(admin.ModelAdmin):
    # filter_horizontal = ("tag", "genre")
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


class SpeciesAdmin(admin.ModelAdmin):
    # filter_horizontal = ("tag", "genre")
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(LivingThings, LivingThingsAdmin)
admin.site.register(Habitat, HabitatAdmin)
admin.site.register(Species, SpeciesAdmin)
