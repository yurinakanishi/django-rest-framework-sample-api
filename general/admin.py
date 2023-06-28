from django.contrib import admin
from .models import Article, Tag, GenreForURL, Language


class ArticleAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


class GenreAdmin(admin.ModelAdmin):
    display_fields = "name"

class LanguageAdmin(admin.ModelAdmin):
    display_fields = "name"

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(GenreForURL, GenreAdmin)
admin.site.register(Language, LanguageAdmin)
