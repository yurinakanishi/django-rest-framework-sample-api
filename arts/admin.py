from django.contrib import admin
from .models import Art, Artist, PaintingMethod, PaintingStyle, Museum, ArtsPeriod


class ArtAdmin(admin.ModelAdmin):
    # filter_horizontal = ("tag", "genre")
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


class ArtistAdmin(admin.ModelAdmin):
    # filter_horizontal = ("tag", "genre")
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


class ArtMethodAdmin(admin.ModelAdmin):
    # filter_horizontal = ("tag", "genre")
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


class ArtStyleAdmin(admin.ModelAdmin):
    # filter_horizontal = ("tag", "genre")
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


class MuseumAdmin(admin.ModelAdmin):
    # filter_horizontal = ("tag", "genre")
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


class ArtsPeriodAdmin(admin.ModelAdmin):
    # filter_horizontal = ("tag", "genre")
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Art, ArtAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(PaintingMethod, ArtMethodAdmin)
admin.site.register(PaintingStyle, ArtStyleAdmin)
admin.site.register(Museum, MuseumAdmin)
admin.site.register(ArtsPeriod, ArtsPeriodAdmin)
