from django.test import SimpleTestCase

from colorfield.fields import ColorField


class ColorFieldDeconstructionTests(SimpleTestCase):
    def test_clone_preserves_nondefault_format_and_validation(self):
        for color_format in ("hexa", "rgb", "rgba"):
            with self.subTest(color_format=color_format):
                field = ColorField(format=color_format)
                clone = field.clone()

                self.assertEqual(clone.format, color_format)
                self.assertEqual(
                    clone.clean(field.get_default(), None), field.get_default()
                )

    def test_default_format_does_not_add_a_migration_argument(self):
        field = ColorField()
        _, _, _, kwargs = field.deconstruct()

        self.assertNotIn("format", kwargs)
        self.assertEqual(field.clone().format, "hex")
