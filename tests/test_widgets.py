from django.test import TestCase

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
        self.assertIn(
            "data-coloris=\"{'format':'hex','alpha':false,'forceAlpha':false,'required':false,'clearButton':true}\"",
            text,
        )

    def test_init_attrs(self):
        widget = ColorWidget(attrs={"swatches": CHOICES})
        text = widget.render("color", None)
        self.assertIn('name="color"', text)
        self.assertIn('value=""', text)
        self.assertIn(
            "data-coloris=\"{'format':'hex','alpha':false,'forceAlpha':false,"
            "'required':false,'clearButton':true,"
            "'swatches':['#FFFFFF', '#000000'],'swatchesOnly':false}\"",
            text,
        )

    def test_render_attrs(self):
        widget = ColorWidget()
        text = widget.render(
            "color",
            None,
            attrs={"format": "rgb", "swatches_only": True},
        )
        # swatches_only is ignored if there are no swatches
        self.assertIn(
            "data-coloris=\"{'format':'rgb','alpha':false,'forceAlpha':false,"
            "'required':false,'clearButton':true}\"",
            text,
        )
