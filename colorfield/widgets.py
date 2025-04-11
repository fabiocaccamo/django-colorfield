from django.conf import settings
from django.forms import TextInput
from django.template.loader import render_to_string


_minimize = "" if settings.DEBUG else ".min"


class ColorWidget(TextInput):
    template_name = "colorfield/color.html"

    class Media:
        css = {"all": [f"colorfield/coloris/coloris{_minimize}.css"]}
        js = [
            f"colorfield/coloris/coloris{_minimize}.js",
            "colorfield/colorfield.js",
        ]

    def get_context(self, name, value, attrs=None):
        context = {}
        context.update(self.attrs.copy() or {})
        context.update(attrs or {})
        context.update(
            {
                "widget": self,
                "name": name,
                "value": value,
            }
        )
        if "format" not in context:
            context.update({"format": "hex"})

        context.update(
            {
                "alpha": str(bool(context.get("alpha"))).lower(),
                "clear_button": str(not bool(context.get("required"))).lower(),
                "swatches_only": str(bool(context.get("swatches_only"))).lower(),
            }
        )

        return context

    def render(self, name, value, attrs=None, renderer=None):
        return render_to_string(
            self.template_name, self.get_context(name, value, attrs)
        )
