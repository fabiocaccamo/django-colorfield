import unittest

try:
    from unittest import mock  # Python 3
except ImportError:
    import mock  # Python 2

from colorfield.fields import ColorWidget


class ColorWidgetTestCase(unittest.TestCase):

    @mock.patch("colorfield.fields.render_to_string")
    def test_render_with_is_required_true(self, m):

        widget = mock.Mock(spec=ColorWidget)
        widget.is_required = True

        ColorWidget.render(widget, "alpha", "bravo", {"charlie": "delta"})

        self.assertEqual(m.call_count, 1)
        self.assertEqual(len(m.call_args[0]), 2)
        self.assertEqual(m.call_args[0][0], "colorfield/color.html")
        self.assertEqual(len(m.call_args[0][1]), 4)

        self.assertEqual(m.call_args[0][1]["name"], "alpha")
        self.assertEqual(m.call_args[0][1]["value"], "bravo")
        self.assertEqual(m.call_args[0][1]["attrs"], {"charlie": "delta"})
        self.assertEqual(m.call_args[0][1]["is_required"], True)

    @mock.patch("colorfield.fields.render_to_string")
    def test_render_with_is_required_false(self, m):

        widget = mock.Mock(spec=ColorWidget)
        widget.is_required = False

        ColorWidget.render(widget, "alpha", "bravo", {"charlie": "delta"})

        self.assertEqual(m.call_args[0][1]["is_required"], False)
