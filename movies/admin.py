from django.contrib import admin
from .models import Movie, MovieDirector, MovieRating, MovieActor, MovieReview


class MovieAdmin(admin.ModelAdmin):
    # filter_horizontal = ("tag", "genre")
    display_fields = "title"
    prepopulated_fields = {"title": ("title",)}


class MovieDirectorAdmin(admin.ModelAdmin):
    # filter_horizontal = ("tag", "genre")
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


class MovieRatingAdmin(admin.ModelAdmin):
    display_fields = "movie_name"
    prepopulated_fields = {"slug": ("movie_name",)}


class MovieActorAdmin(admin.ModelAdmin):
    # filter_horizontal = ("tag", "genre")
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


class MovieReviewAdmin(admin.ModelAdmin):
    # filter_horizontal = ("tag", "genre")
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieDirector, MovieDirectorAdmin)
admin.site.register(MovieRating, MovieRatingAdmin)
admin.site.register(MovieActor, MovieActorAdmin)
admin.site.register(MovieReview, MovieReviewAdmin)
