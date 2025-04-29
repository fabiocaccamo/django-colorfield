from django.contrib import admin

from . import models


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "color_default",
        "color_null",
        "color_rgb",
        "color_rgba",
        "color_choices",
        "color_samples",
        "color_image",
        "color_image_default",
        "color_image_hexa",
        "color_image_rgb",
        "color_image_rgba",
    ]


class ColorInlineAdmin(admin.TabularInline):
    model = models.PaletteColor
    extra = 0


@admin.register(models.Palette)
class PaletteAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    inlines = [ColorInlineAdmin]
