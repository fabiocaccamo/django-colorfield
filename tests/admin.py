from django.contrib import admin

from colorfield.admin import ColorAdminMixin
from tests import models


@admin.register(models.Color)
class ColorAdmin(ColorAdminMixin, admin.ModelAdmin):
    list_display = ["id", "color"]


@admin.register(models.ColorChoices)
class ColorChoicesAdmin(ColorAdminMixin, admin.ModelAdmin):
    list_display = ["id", "color"]
