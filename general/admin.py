from django.contrib import admin
from .models import Article, Tag, Genre


class ArticleAdmin(admin.ModelAdmin):
    pass
    # filter_horizontal = ("tags", "genres")
    # display_fields = "name"
    # prepopulated_fields = {"slug": ("name",)}


class TagAdmin(admin.ModelAdmin):
    pass


class GenreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Genre, GenreAdmin)
