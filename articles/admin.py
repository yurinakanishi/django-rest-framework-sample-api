from django.contrib import admin
from .models import Article, Tag, Genre


class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ("tags", "genres")
    display_fields = "title"
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    pass


class GenreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Genre, GenreAdmin)
