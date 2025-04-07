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
            'data-coloris="{'
            "&#x27;format&#x27;: &#x27;hex&#x27;, "
            "&#x27;required&#x27;: False, "
            "&#x27;clearButton&#x27;: True, "
            "&#x27;alpha&#x27;: False, "
            "&#x27;forceAlpha&#x27;: False, "
            "&#x27;swatches&#x27;: [], "
            "&#x27;swatchesOnly&#x27;: False"
            '}"',
            text,
        )

    def test_init_attrs(self):
        widget = ColorWidget(attrs={"swatches": CHOICES})
        text = widget.render("color", None)
        self.assertIn('name="color"', text)
        self.assertIn('value=""', text)
        self.assertIn(
            'data-coloris="{'
            "&#x27;format&#x27;: &#x27;hex&#x27;, "
            "&#x27;required&#x27;: False, "
            "&#x27;clearButton&#x27;: True, "
            "&#x27;alpha&#x27;: False, "
            "&#x27;forceAlpha&#x27;: False, "
            "&#x27;swatches&#x27;: [&#x27;#FFFFFF&#x27;, &#x27;#000000&#x27;], "
            "&#x27;swatchesOnly&#x27;: False"
            '}"',
            text,
        )

    def test_render_attrs(self):
        widget = ColorWidget()
        text = widget.render(
            "color",
            None,
            attrs={"format": "rgb", "swatches_only": True},
        )
        self.assertIn(
            'data-coloris="{'
            "&#x27;format&#x27;: &#x27;rgb&#x27;, "
            "&#x27;required&#x27;: False, "
            "&#x27;clearButton&#x27;: True, "
            "&#x27;alpha&#x27;: False, "
            "&#x27;forceAlpha&#x27;: False, "
            "&#x27;swatches&#x27;: [], "
            "&#x27;swatchesOnly&#x27;: False"
            '}"',
            text,
        )
