from django.template import Template, Context
from django.utils.html import format_html
from colorfield.fields import ColorField


class ColorAdminMixin:
    class Media:
        js = ("colorfield/colorfield-changelist-readonly.js",)

    def _get_color_fields(self):
        return tuple(
            (field.name, field.choices)
            for field in self.model._meta.fields
            if isinstance(field, ColorField)
        )

    def _get_color_fields_json_script(self):
        template = Template("{{ value|json_script:'colorfield-list-of-fields' }}")
        context = Context({"value": self._get_color_fields()})
        script = format_html(template.render(context))
        return script

    def _inject_color_fields_json_script(self, response):
        def inject_script():
            response.render()
            script_html = self._get_color_fields_json_script().encode("utf-8")
            response.content = response.content.replace(
                b"</head>", script_html + b"</head>"
            )

        if hasattr(response, "add_post_render_callback"):
            response.add_post_render_callback(lambda r: inject_script())
        else:
            inject_script()

        return response

    # # TODO: verify if it's needed
    # def add_view(self, request, form_url="", extra_context=None):
    #     response = super().add_view(request, form_url, extra_context)
    #     response = self._inject_color_fields_json_script(response)
    #     return response

    def change_view(self, request, object_id, form_url="", extra_context=None):
        response = super().change_view(request, object_id, form_url, extra_context)
        response = self._inject_color_fields_json_script(response)
        return response

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        response = self._inject_color_fields_json_script(response)
        return response
