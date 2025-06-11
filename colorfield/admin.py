from colorfield.fields import ColorField


class ColorAdminMixin:
    # add_form_template = "colorfield/admin/change_form.html"
    # change_form_template = "colorfield/admin/change_form.html"
    change_list_template = "colorfield/admin/change_list.html"

    def _get_color_fields(self):
        return [
            (field.name, field.choices)
            for field in self.model._meta.fields
            if isinstance(field, ColorField)
        ]

    def _get_extra_context(self, extra_context):
        fields = self._get_color_fields()
        extra_context = extra_context or {}
        extra_context.update({"colorfield_list_of_fields": fields})
        return extra_context

    def changelist_view(self, request, extra_context=None):
        extra_context = self._get_extra_context(extra_context)
        return super().changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        extra_context = self._get_extra_context(extra_context)
        return super().changeform_view(request, object_id, form_url, extra_context)
