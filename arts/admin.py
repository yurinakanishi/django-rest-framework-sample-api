from django.contrib import admin
from .models import Art, Artist, ArtMethod, ArtStyle, Museum


class ArtAdmin(admin.ModelAdmin):
    pass


class ArtistAdmin(admin.ModelAdmin):
    pass


class ArtMethodAdmin(admin.ModelAdmin):
    pass


class ArtStyleAdmin(admin.ModelAdmin):
    pass


class MuseumAdmin(admin.ModelAdmin):
    pass


admin.site.register(Art, ArtAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(ArtMethod, ArtMethodAdmin)
admin.site.register(ArtStyle, ArtStyleAdmin)
admin.site.register(Museum, MuseumAdmin)
