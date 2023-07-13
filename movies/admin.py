from django.contrib import admin
from .models import Movie, MovieDirector, MovieRating, MovieActor


class MovieAdmin(admin.ModelAdmin):
    # filter_horizontal = ("tag", "genre")
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


class MovieDirectorAdmin(admin.ModelAdmin):
    # filter_horizontal = ("tag", "genre")
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


class MovieRatingAdmin(admin.ModelAdmin):
    pass


class MovieActorAdmin(admin.ModelAdmin):
    # filter_horizontal = ("tag", "genre")
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieDirector, MovieDirectorAdmin)
admin.site.register(MovieRating, MovieRatingAdmin)
admin.site.register(MovieActor, MovieActorAdmin)
