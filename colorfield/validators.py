import re

from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

COLOR_HEX_RE = re.compile("^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$")
color_hex_validator = RegexValidator(
    COLOR_HEX_RE,
    _("Enter a valid hex color, eg. #000000"),
    "invalid",
)


COLOR_HEXA_RE = re.compile("#([A-Fa-f0-9]{8}|[A-Fa-f0-9]{4})$")
color_hexa_validator = RegexValidator(
    COLOR_HEXA_RE,
    _("Enter a valid hexa color, eg. #00000000"),
    "invalid",
)

COLOR_RGB_RE = re.compile(
    # prefix and opening parenthesis
    r"^rgb\("
    # first number: red channel
    r"(\d{1,3})"
    # comma and optional space
    r",\s?"
    # second number: green channel
    r"(\d{1,3})"
    # comma and optional space
    r",\s?"
    # third number: blue channel
    r"(\d{1,3})"
    # closing parenthesis
    r"\)$"
)
color_rgb_validator = RegexValidator(
    COLOR_RGB_RE,
    _("Enter a valid rgb color, eg. rgb(128, 128, 128)"),
    "invalid",
)
COLOR_RGBA_RE = re.compile(
    # prefix and opening parenthesis
    r"^rgba\("
    # first number: red channel
    r"(\d{1,3})"
    # comma and optional space
    r",\s?"
    # second number: green channel
    r"(\d{1,3})"
    # comma and optional space
    r",\s?"
    # third number: blue channel
    r"(\d{1,3})"
    # comma and optional space
    r",\s?"
    # alpha channel: decimal number between 0 and 1
    r"(0(\.\d{1,2})?|1(\.0)?)"
    # closing parenthesis
    r"\)$"
)
color_rgba_validator = RegexValidator(
    COLOR_RGBA_RE,
    _("Enter a valid rgba color, eg. rgba(128, 128, 128, 0.5)"),
    "invalid",
)

COLOR_HSL_RE = re.compile(
    # prefix and opening parenthesis
    r"^hsl\("
    # first number: hue channel
    r"(\d+\.?\d*)"
    # comma and optional space
    r",\s?"
    # second number: saturation channel, percentage
    r"(\d+\.?\d*)%"
    # comma and optional space
    r",\s?"
    # third number: lightness channel, percentage
    r"(\d+\.?\d*)%"
    # closing parenthesis
    r"\)$"
)
color_hsl_validator = RegexValidator(
    COLOR_HSL_RE,
    _("Enter a valid hsl color, eg. hsl(128, 28%, 12%)"),
    "invalid",
)
COLOR_HSLA_RE = re.compile(
    # prefix and opening parenthesis
    r"^hsla\("
    # first number: hue channel
    r"(\d+\.?\d*)"
    # comma and optional space
    r",\s?"
    # second number: saturation channel, percentage
    r"(\d+\.?\d*)%"
    # comma and optional space
    r",\s?"
    # third number: lightness channel, percentage
    r"(\d+\.?\d*)%"
    # comma and optional space
    r",\s?"
    # alpha channel: decimal number between 0 and 1
    r"(0(\.\d{1,2})?|1(\.0)?)"
    # closing parenthesis
    r"\)$"
)
color_hsla_validator = RegexValidator(
    COLOR_HSLA_RE,
    _("Enter a valid hsla color, eg. hsla(128, 28%, 12%, 0.5)"),
    "invalid",
)


VALIDATORS_PER_FORMAT = {
    "hex": color_hex_validator,
    "hexa": color_hexa_validator,
    "rgb": color_rgb_validator,
    "rgba": color_rgba_validator,
    "hsl": color_hsl_validator,
    "hsla": color_hsla_validator,
}
