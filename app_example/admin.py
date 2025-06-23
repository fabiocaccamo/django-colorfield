from django.contrib import admin

from colorfield.admin import ColorAdminMixin

from . import forms, models


@admin.register(models.Color)
class ColorAdmin(ColorAdminMixin, admin.ModelAdmin):
    list_display = [
        "id",
        "color_default_ro",
        "color_null",
        "color_rgb",
        "color_rgba",
        "color_choices",
        "color_samples",
        "color_image_hex",
        "color_image_hexa",
        "color_image_rgb",
        "color_image_rgba",
    ]

    # Make list editable to check how the list works along with RO fields
    list_editable = [
        "color_rgb",
        "color_rgba",
    ]

    # Add custom disabled field
    form = forms.ColorForm

    # These fields will display a box with the color in list and form
    readonly_fields = [
        "color_default_ro",
        "color_image_hex",
        "color_image_hexa",
        "color_image_rgb",
        "color_image_rgba",
    ]
    fieldsets = [
        (
            "HEX, null & blank",
            {
                "fields": [
                    ("color_default", "color_default_ro"),
                    "color_ro",
                    "color_null",
                ],
            },
        ),
        ("RGB", {"fields": ["color_rgb", "color_rgba"]}),
        ("Choices", {"fields": ["color_choices", "color_samples"]}),
        (
            "Image",
            {
                "fields": [
                    "image",
                    "color_image_hex",
                    "color_image_hexa",
                    "color_image_rgb",
                    "color_image_rgba",
                ]
            },
        ),
    ]

    def get_color_fields(self, request, object_id=None):
        fields = super().get_color_fields(request, object_id) or []
        # add custom field in list
        return fields + ["color_default_ro"]

    # Uncomment this method to display the change-form view as Read-Only.
    # def has_change_permission(self, request, obj=None):
    #     return False


class ColorInlineAdmin(admin.TabularInline):
    model = models.PaletteColor
    extra = 0


@admin.register(models.Palette)
class PaletteAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    inlines = [ColorInlineAdmin]
