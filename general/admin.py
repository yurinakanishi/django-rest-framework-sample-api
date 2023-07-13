from django.contrib import admin
from .models import Article, Tag, GenreForUrl, Language


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
admin.site.register(GenreForUrl, GenreAdmin)
admin.site.register(Language, LanguageAdmin)
