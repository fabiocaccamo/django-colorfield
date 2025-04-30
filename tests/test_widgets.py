import json

from django.test import TestCase
from django.utils.html import escape

from colorfield.widgets import ColorWidget
from tests.models import COLOR_PALETTE


CHOICES = [choice[0] for choice in COLOR_PALETTE]


class ColorWidgetTestCase(TestCase):
    def test_basic(self):
        widget = ColorWidget(attrs={"id": "id_color"})
        text = widget.render("color", "#FFFFFF")
        self.assertIn('<input type="text"', text)
        self.assertIn('id="id_color"', text)
        self.assertIn('class="colorfield_field coloris id_color form-control"', text)
        self.assertIn('name="color"', text)
        self.assertIn('value="#FFFFFF"', text)
        self.assertIn('placeholder="#FFFFFF"', text)

        data_coloris = {
            "format": "hex",
            "required": False,
            "clearButton": True,
            "alpha": False,
            "forceAlpha": False,
            "swatches": [],
            "swatchesOnly": False,
        }
        self.assertIn(f'data-coloris="{escape(json.dumps(data_coloris))}"', text)

    def test_init_attrs(self):
        widget = ColorWidget(attrs={"swatches": CHOICES})
        text = widget.render("color", None)
        self.assertIn('name="color"', text)
        self.assertIn('value=""', text)

        data_coloris = {
            "format": "hex",
            "required": False,
            "clearButton": True,
            "alpha": False,
            "forceAlpha": False,
            "swatches": ["#FFFFFF", "#000000"],
            "swatchesOnly": False,
        }
        self.assertIn(f'data-coloris="{escape(json.dumps(data_coloris))}"', text)

    def test_render_attrs(self):
        widget = ColorWidget()
        text = widget.render(
            "color",
            None,
            attrs={"format": "rgb", "swatches_only": True},
        )

        data_coloris = {
            "format": "rgb",
            "required": False,
            "clearButton": True,
            "alpha": False,
            "forceAlpha": False,
            "swatches": [],
            "swatchesOnly": False,
        }
        self.assertIn(f'data-coloris="{escape(json.dumps(data_coloris))}"', text)
