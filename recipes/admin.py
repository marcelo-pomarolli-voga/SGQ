from django.contrib import admin

from .models import Category, Recipe
class CategoryAdmin(admin.ModelAdmin):
    ...    
admin.site.register(Category, CategoryAdmin)

@admin.register(Recipe) # Outra forma de registrar 
class RecipeAdmin(admin.ModelAdmin):
    ...
