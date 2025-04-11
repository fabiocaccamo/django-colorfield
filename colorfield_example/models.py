from django.db import models

from colorfield.fields import ColorField

COLOR_PALETTE = [
    ("#067bc2", "dark blue"),
    ("#84bcda", "light blue"),
    ("#80e377", "green"),
    ("#ecc30b", "yellow"),
    ("#f37748", "orange"),
    ("#d56062", "red"),
    ("#FFFFFF", "white"),
    ("#000000", "black"),
]


class Color(models.Model):
    image = models.ImageField(blank=True, upload_to="temp")

    color_default = ColorField(blank=True)
    color_null = ColorField(null=True)
    color_rgb = ColorField(format="rgb")
    color_rgba = ColorField(format="rgba")
    color_choices = ColorField(blank=True, choices=COLOR_PALETTE)
    color_samples = ColorField(blank=True, samples=COLOR_PALETTE)

    color_image = ColorField(image_field="image")
    color_image_default = ColorField(image_field="image", default="#FF0000")
    color_image_hexa = ColorField(image_field="image", format="hexa")
    color_image_rgb = ColorField(image_field="image", format="rgb")
    color_image_rgba = ColorField(image_field="image", format="rgba")

    class Meta:
        app_label = "colorfield_example"
