from django.contrib import admin
from .models import Movie, MovieDirector, MovieRating, MovieActor, MovieReview


class MovieAdmin(admin.ModelAdmin):
    pass


class MovieDirectorAdmin(admin.ModelAdmin):
    pass


class MovieRatingAdmin(admin.ModelAdmin):
    pass


class MovieActorAdmin(admin.ModelAdmin):
    pass


class MovieReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieDirector, MovieDirectorAdmin)
admin.site.register(MovieRating, MovieRatingAdmin)
admin.site.register(MovieActor, MovieActorAdmin)
admin.site.register(MovieReview, MovieReviewAdmin)
