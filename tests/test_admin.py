from django.contrib.auth import get_user_model
from django.contrib.admin.sites import AdminSite
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import TestCase, RequestFactory

from tests.admin import ColorAdmin, ColorChoicesAdmin
from tests.models import Color, ColorChoices


User = get_user_model()


class AdminTestCase(TestCase):
    @classmethod
    def get_request(cls):
        request = RequestFactory().get("/admin/")
        request.user = User.objects.create_superuser(username="admin")
        request.session = "session-admin"
        request._messages = FallbackStorage(request)
        return request


class ColorAdminTestCase(AdminTestCase):
    @classmethod
    def get_admin_app(cls):
        return ColorAdmin(Color, AdminSite())

    def test_admin_get_color_fields(self):
        app = self.get_admin_app()
        color_fields = app.get_color_fields(None)
        self.assertEqual(color_fields, [("color", None)])

    def test_admin_changelist_view(self):
        app = self.get_admin_app()
        request = self.get_request()

        response = app.changelist_view(request)
        self.assertContains(
            response,
            '<script id="colorfield-list-of-fields" type="application/json">'
            '[["color", null]]</script>',
        )

    def test_admin_changeform_view_add(self):
        app = self.get_admin_app()
        request = self.get_request()

        response = app.changeform_view(request)
        self.assertContains(
            response,
            '<script id="colorfield-list-of-fields" type="application/json">'
            '[["color", null]]</script>',
        )
        self.assertContains(response, "<h1>Add color</h1>")

    def test_admin_changeform_view_edit(self):
        app = self.get_admin_app()
        request = self.get_request()
        color = Color(color="#FFFFFF")
        color.save()

        response = app.changeform_view(request, object_id=str(color.pk))
        self.assertContains(
            response,
            '<script id="colorfield-list-of-fields" type="application/json">'
            '[["color", null]]</script>',
        )
        self.assertContains(response, f"<h2>Color object ({color.pk})</h2>")


class ColorChoicesAdminTestCase(AdminTestCase):
    @classmethod
    def get_admin_app(cls):
        return ColorChoicesAdmin(ColorChoices, AdminSite())

    def test_admin_get_color_fields(self):
        app = self.get_admin_app()
        color_fields = app.get_color_fields(None)
        self.assertEqual(
            color_fields,
            [("color", [("#ffffff", "white"), ("#000000", "black")])],
        )

    def test_admin_changelist_view(self):
        app = self.get_admin_app()
        request = self.get_request()

        response = app.changelist_view(request)
        self.assertEqual(response.template_name, "colorfield/admin/change_list.html")
        self.assertContains(
            response,
            '<script src="/static/colorfield/admin.js"></script>',
        )
        self.assertContains(
            response,
            '<script id="colorfield-list-of-fields" type="application/json">'
            '[["color", [["#ffffff", "white"], ["#000000", "black"]]]]</script>',
        )

    def test_admin_changeform_view(self):
        app = self.get_admin_app()
        request = self.get_request()

        response = app.changeform_view(request)
        self.assertEqual(response.template_name, "colorfield/admin/change_form.html")
        self.assertContains(
            response,
            '<script src="/static/colorfield/admin.js"></script>',
        )
        self.assertContains(
            response,
            '<script id="colorfield-list-of-fields" type="application/json">'
            '[["color", [["#ffffff", "white"], ["#000000", "black"]]]]</script>',
        )
