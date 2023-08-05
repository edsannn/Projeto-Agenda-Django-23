from django.contrib import admin
from contact import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',


def __str__(self) -> str:
    return self.name


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'email', 'show',
    ordering = 'id',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 1000
    list_editable = 'first_name', 'last_name', 'show'
    list_display_links = 'id', 'email',
