from django.contrib import admin

from .models import Category, Juan, Recipe


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ...
admin.site.register(Category, CategoryAdmin)    


class RecipesAdmin(admin.ModelAdmin):
    ...
admin.site.register(Recipe,RecipesAdmin)



