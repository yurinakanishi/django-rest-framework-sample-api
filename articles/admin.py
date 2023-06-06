from django.contrib import admin

# Register your models here.
from .models import Article, Tag, Genre


class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ("tags", "genres")
    display_fields = ("name", "title", "author", "date_published")
    prepopulated_fields = {"name": ("title",)}


class TagAdmin(admin.ModelAdmin):
    pass


class GenreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Genre, GenreAdmin)
