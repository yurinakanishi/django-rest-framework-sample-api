from django.contrib import admin
from .models import Food, CookingMethod, Ingredient


class FoodAdmin(admin.ModelAdmin):
    pass


class CookingMethodAdmin(admin.ModelAdmin):
    pass


class IngredientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Food, FoodAdmin)
admin.site.register(CookingMethod, CookingMethodAdmin)
admin.site.register(Ingredient, IngredientAdmin)
