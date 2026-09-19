from django.db import models

from colorfield.fields import ColorField

COLOR_PALETTE = [
    ("#067bc2", "similar to blue"),
    ("#84bcda", "blue like gray"),
    ("#80e377", "light green"),
    ("#ecc30b", "yellow but no so much"),
    ("#f37748", "almost orange"),
    ("#d56062", "reddish"),
    ("#ffffff", "white"),
    ("#000000", "black"),
]


class Color(models.Model):
    color_default = ColorField(blank=True)
    # This field will be disabled in the admin section
    color_ro = ColorField(blank=True)

    color_null = ColorField(null=True)
    color_rgb = ColorField(format="rgb")
    color_rgba = ColorField(format="rgba")
    color_choices = ColorField(blank=True, choices=COLOR_PALETTE)
    color_samples = ColorField(blank=True, samples=COLOR_PALETTE)

    image = models.ImageField(blank=True, upload_to="temp")
    color_image_hex = ColorField(
        blank=True,
        editable=False,
        image_field="image",
        format="hex",
    )
    color_image_hexa = ColorField(
        blank=True,
        editable=False,
        image_field="image",
        format="hexa",
    )
    color_image_rgb = ColorField(
        blank=True,
        editable=False,
        image_field="image",
        format="rgb",
    )
    color_image_rgba = ColorField(
        blank=True,
        editable=False,
        image_field="image",
        format="rgba",
    )

    def save(self, *args, **kwargs):
        self.color_ro = self.color_default
        super().save(*args, **kwargs)


class Palette(models.Model):
    name = models.CharField(max_length=25)


class PaletteColor(models.Model):
    palette = models.ForeignKey(to="Palette", on_delete=models.CASCADE)
    color = ColorField()
    color_choices = ColorField(choices=COLOR_PALETTE)
    color_rgb = ColorField(format="rgb")
