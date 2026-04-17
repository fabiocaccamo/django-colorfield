from django.core.exceptions import ValidationError as DjangoValidationError

try:
    from rest_framework.serializers import CharField
    from rest_framework.serializers import ValidationError as DRFValidationError
except ImportError:
    ModuleNotFoundError("Django REST Framework is not installed.")

from colorfield.validators import VALIDATORS_PER_FORMAT


class ColorField(CharField):
    default_error_messages = {
        "invalid": [fn.message for fn in VALIDATORS_PER_FORMAT.values()]
    }

    def to_internal_value(self, data):
        errors = {}

        for key, validator_fn in VALIDATORS_PER_FORMAT.items():
            try:
                validator_fn(data)
                errors[key] = False
            except DjangoValidationError:
                errors[key] = True

        if all(errors.values()):
            raise DRFValidationError(self.default_error_messages.get("invalid"))

        return data
