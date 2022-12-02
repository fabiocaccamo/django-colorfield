from django.core.exceptions import ValidationError as DjangoValidationError

try:
    from rest_framework.serializers import CharField
    from rest_framework.serializers import ValidationError as DRFValidationError
except ImportError:
    ModuleNotFoundError("Django REST Framework is not installed.")

from colorfield.validators import color_hex_validator, color_hexa_validator


class ColorField(CharField):

    default_error_messages = {
        "invalid": [
            color_hex_validator.message,
            color_hexa_validator.message,
        ]
    }

    def to_internal_value(self, data):
        has_hex_error = False
        has_hexa_error = False
        try:
            color_hex_validator(data)
        except DjangoValidationError:
            has_hex_error = True

        try:
            color_hexa_validator(data)
        except DjangoValidationError:
            has_hexa_error = True

        if has_hex_error and has_hexa_error:
            raise DRFValidationError(self.default_error_messages.get("invalid"))

        return data
