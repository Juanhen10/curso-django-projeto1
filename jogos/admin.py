from django.contrib import admin

from .models import Category, Jogos


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Jogos)
class JogosAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
