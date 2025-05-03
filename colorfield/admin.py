from colorfield.fields import ColorField


class ColorAdminMixin:
    add_form_template = "colorfield/admin/change_form.html"
    change_form_template = "colorfield/admin/change_form.html"
    change_list_template = "colorfield/admin/change_list.html"

    def get_color_fields(self, request, object_id=None):
        return [
            (f.name, f.choices)
            for f in self.model._meta.fields
            if isinstance(f, ColorField)
        ]

    def _get_extra_content(self, request, object_id=None, extra_context=None):
        fields = self.get_color_fields(request, object_id)
        extra_context = extra_context or {}
        extra_context.update({"colorfield_list_of_fields": fields})
        return extra_context

    def changelist_view(self, request, extra_context=None):
        extra_context = self._get_extra_content(request, extra_context=extra_context)
        return super().changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        extra_context = self._get_extra_content(
            request, object_id, extra_context=extra_context
        )
        return super().changeform_view(request, object_id, form_url, extra_context)
