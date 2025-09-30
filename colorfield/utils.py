import colorsys
import contextlib
import string

from PIL import Image, UnidentifiedImageError

from django.utils.crypto import get_random_string as dj_get_random_string


def get_image_background_color(img, img_format: str):
    has_alpha = img_format in {"hexa", "rgba", "hsla"}
    img = img.convert("RGBA" if has_alpha else "RGB")
    pixel_color = img.getpixel((1, 1))

    if img_format in {"hex", "hexa"}:
        color_format = "#" + "%02x" * len(pixel_color)
        color = color_format % pixel_color
        color = color.upper()

    elif img_format in {"rgb", "rgba"}:
        if has_alpha:
            # Normalize alpha channel to be between 0 and 1
            pixel_color = (
                *pixel_color[:3],
                round(pixel_color[3] / 255, 2),
            )
        # Should look like `rgb(1, 2, 3) or rgba(1, 2, 3, 1.0)
        color = f"{img_format}{pixel_color}"

    elif img_format in {"hsl", "hsla"}:
        rgb = [x / 255.0 for x in pixel_color[:3]]
        hue, lightness, saturation = colorsys.rgb_to_hls(*rgb)
        hsl = (
            round(hue * 360.0),
            round(saturation * 100.0),
            round(lightness * 100.0),
        )

        color = f"{img_format}({hsl[0]}, {hsl[1]}%, {hsl[2]}%"
        if has_alpha:
            alpha = round(pixel_color[3] / 255, 2) if has_alpha else None
            color += f", {alpha}"
        color += ")"

    else:  # pragma: no cover
        raise NotImplementedError(f"Unsupported color format: {img_format}")

    return color


def get_image_file_background_color(img_file, img_format: str):
    color = ""
    with contextlib.suppress(UnidentifiedImageError):
        with Image.open(img_file) as image:
            color = get_image_background_color(image, img_format)
    return color


def get_random_string():
    return dj_get_random_string(
        length=32, allowed_chars=string.ascii_lowercase + string.digits
    )
