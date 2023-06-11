from django.contrib import admin
from .models import Movie, MovieDirector, MovieRating


class MovieAdmin(admin.ModelAdmin):
    pass


class MovieDirectorAdmin(admin.ModelAdmin):
    pass


class MovieRatingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieDirector, MovieDirectorAdmin)
admin.site.register(MovieRating, MovieRatingAdmin)
