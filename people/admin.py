from django.contrib import admin
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    # filter_horizontal = ("tag", "genre")
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Person, PersonAdmin)
