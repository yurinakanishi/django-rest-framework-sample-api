from django.contrib import admin
from .models import Food, CookingMethod, Ingredient


class FoodAdmin(admin.ModelAdmin):
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


class CookingMethodAdmin(admin.ModelAdmin):
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


class IngredientAdmin(admin.ModelAdmin):
    pass
    display_fields = "name"
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Food, FoodAdmin)
admin.site.register(CookingMethod, CookingMethodAdmin)
admin.site.register(Ingredient, IngredientAdmin)
