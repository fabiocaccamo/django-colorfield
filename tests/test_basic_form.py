from django.test import TestCase
from tests.forms import BasicForm


class BasicFormTest(TestCase):
    def test_color_field_initial_value(self):
        """
        Test that the color field has the correct initial value.
        """
        form = BasicForm()
        self.assertEqual(form.fields["color"].initial, "#FF0000")

    def test_color_field_valid_data(self):
        """
        Test that the form is valid with correct HEX color data.
        """
        data = {"color": "#00FF00"}
        form = BasicForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["color"], "#00FF00")

    def test_color_field_invalid_data(self):
        """
        Test that the form is invalid with incorrect HEX color data.
        """
        # Test invalid HEX color (missing #)
        data = {"color": "00FF00"}
        form = BasicForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("color", form.errors)

        # Test invalid HEX color (invalid characters)
        data = {"color": "#ZZZZZZ"}
        form = BasicForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("color", form.errors)

    def test_color_field_empty_data(self):
        """
        Test that the form is invalid when the color field is empty.
        """
        data = {"color": ""}
        form = BasicForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("color", form.errors)

    def test_color_field_widget_rendering(self):
        """
        Test that the color field widget renders correctly.
        """
        form = BasicForm()
        rendered_form = form.as_p()
        self.assertIn('type="text"', rendered_form)
        self.assertIn('value="#FF0000"', rendered_form)
