from django.contrib import admin
from .models import LivingThings, Habitat, Species


class LivingThingsAdmin(admin.ModelAdmin):
    pass


class HabitatAdmin(admin.ModelAdmin):
    pass


class SpeciesAdmin(admin.ModelAdmin):
    pass


admin.site.register(LivingThings, LivingThingsAdmin)
admin.site.register(Habitat, HabitatAdmin)
admin.site.register(Species, SpeciesAdmin)
