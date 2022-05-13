from re import compile as re_compile

from django import VERSION as DJANGO_VERSION
from django.core.validators import RegexValidator

if DJANGO_VERSION >= (2, 0):
    from django.utils.translation import gettext_lazy as _
else:
    from django.utils.translation import ugettext_lazy as _


COLOR_HEX_RE = re_compile("^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$")
color_hex_validator = RegexValidator(
    COLOR_HEX_RE, _("Enter a valid hex color, eg. #000000"), "invalid"
)


COLOR_HEXA_RE = re_compile("#([A-Fa-f0-9]{8}|[A-Fa-f0-9]{4})$")
color_hexa_validator = RegexValidator(
    COLOR_HEXA_RE, _("Enter a valid hexa color, eg. #00000000"), "invalid"
)
