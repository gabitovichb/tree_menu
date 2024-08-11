from django.contrib import admin

from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["name", "status"]
    list_display_links = ["name"]
    ordering = ["name"]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["menu", "parent", "name", "status"]
    list_display_links = ["name"]
    list_filter = ["menu", "status"]
    ordering = ["name"]
