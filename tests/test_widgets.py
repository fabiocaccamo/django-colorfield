import json

from django.test import TestCase

from colorfield.widgets import ColorWidget
from tests.models import COLOR_PALETTE


CHOICES = [choice[0] for choice in COLOR_PALETTE]


class ColorWidgetTestCase(TestCase):
    def test_basic(self):
        widget = ColorWidget(attrs={"id": "id_color"})

        expected = {
            "format": "hex",
            "required": False,
            "clearButton": True,
            "alpha": False,
            "forceAlpha": False,
            "swatches": [],
            "swatchesOnly": False,
        }

        context = widget.get_context("color", "#FFFFFF")
        self.assertIn("data_coloris_id", context)
        self.assertIsNotNone(context["data_coloris_id"])
        self.assertIn("data_coloris_options", context)
        self.assertDictEqual(context["data_coloris_options"], expected)

        text = widget.render("color", "#FFFFFF")
        self.assertIn('<input type="text"', text)
        self.assertIn('id="id_color"', text)
        self.assertIn('class="colorfield_field coloris id_color form-control"', text)
        self.assertIn('name="color"', text)
        self.assertIn('value="#FFFFFF"', text)
        self.assertIn('placeholder="#FFFFFF"', text)
        self.assertIn('data-coloris=""', text)
        self.assertIn('data-coloris-options-json-script-id="coloris-id_color"', text)
        self.assertIn(json.dumps(expected), text)

    def test_init_attrs(self):
        widget = ColorWidget(attrs={"swatches": CHOICES})

        expected = {
            "format": "hex",
            "required": False,
            "clearButton": True,
            "alpha": False,
            "forceAlpha": False,
            "swatches": CHOICES,
            "swatchesOnly": False,
        }

        context = widget.get_context("color", None)
        self.assertIn("data_coloris_id", context)
        self.assertIsNotNone(context["data_coloris_id"])
        self.assertIn("data_coloris_options", context)
        self.assertDictEqual(context["data_coloris_options"], expected)

        text = widget.render("color", None)
        self.assertIn('name="color"', text)
        self.assertIn('value=""', text)
        self.assertIn('data-coloris=""', text)
        self.assertIn('data-coloris-options-json-script-id="coloris-', text)
        self.assertIn(json.dumps(expected), text)

    def test_render_attrs(self):
        widget = ColorWidget()

        expected = {
            "format": "rgb",
            "required": False,
            "clearButton": True,
            "alpha": False,
            "forceAlpha": False,
            "swatches": [],
            "swatchesOnly": False,
        }

        attrs = {"format": "rgb", "swatches_only": True}
        context = widget.get_context("color", None, attrs=attrs)
        self.assertIn("data_coloris_id", context)
        self.assertIsNotNone(context["data_coloris_id"])
        self.assertIn("data_coloris_options", context)
        self.assertDictEqual(context["data_coloris_options"], expected)

        text = widget.render("color", None, attrs=attrs)
        self.assertIn('data-coloris=""', text)
        self.assertIn('data-coloris-options-json-script-id="coloris-', text)
        self.assertIn(json.dumps(expected), text)


class ColorWidgetMediaTestCase(TestCase):
    def test_media_includes_the_alignment_stylesheet(self):
        # The widget's own rules must load after Coloris so they win on the
        # input itself, and they must be present in both debug and minified
        # modes.
        css = ColorWidget.Media.css["all"]
        self.assertIn("colorfield/css/colorfield.css", css)
        self.assertEqual(css[-1], "colorfield/css/colorfield.css")

    def test_alignment_stylesheet_ships_with_the_package(self):
        from pathlib import Path

        import colorfield

        path = Path(colorfield.__file__).parent / "static" / "colorfield" / "css" / "colorfield.css"
        self.assertTrue(path.is_file())
        text = path.read_text(encoding="utf-8")
        # The reported cause: vertical padding on the field, plus a text cursor.
        self.assertIn("padding-top: 0", text)
        self.assertIn("cursor: pointer", text)
