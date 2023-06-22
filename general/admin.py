from django.contrib import admin
from .models import Article, Tag, Genre


class ArticleAdmin(admin.ModelAdmin):
    display_fields = "title"
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


class GenreAdmin(admin.ModelAdmin):
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Genre, GenreAdmin)
