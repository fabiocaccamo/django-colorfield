from django.test import TestCase
from rest_framework.serializers import Serializer
from rest_framework.serializers import ValidationError as DRFValidationError

from colorfield.serializers import ColorField


class SerializerWithColor(Serializer):
    color = ColorField()


class ColorFieldTestCase(TestCase):
    def setUp(self):
        self.valid_hex_full_color = "#123456"
        self.invalid_hex_full_color1 = "#1234567"
        self.invalid_hex_full_color2 = "#12345R"

        self.valid_hex_short_color = "#123"
        self.invalid_hex_short_color1 = "#12"
        self.invalid_hex_short_color2 = "#12R"

        self.valid_hexa_full_color = "#12345678"
        self.invalid_hexa_full_color1 = "#123456789"
        self.invalid_hexa_full_color2 = "#1234567R"

        self.valid_hexa_short_color = "#1234"
        self.invalid_hexa_short_color1 = "#12345"
        self.invalid_hexa_short_color2 = "#123R"

        self.valid_rgb_colors = [
            "rgb(5, 3, 6)",
            "rgb(5,3,6)",
            "rgb(50, 30, 128)",
            "rgb(45,10, 99)",
            "rgb(128, 128, 128)",
            "rgb(156,200,250)",
        ]
        self.invalid_rgb_colors = [
            "rgb(5)",
            "rgb(5, 6)",
            "rgb(128,255)",
            "rgb(128,A)",
            "rgb(128, 128, A)",
            "rgb(128,255,12,30)",
            "rgb(128, 255, 12, A)",
        ]

        self.valid_rgba_colors = [
            "rgba(5, 3, 6, 1)",
            "rgba(5,3,6,1)",
            "rgba(50, 30, 128, 0.5)",
            "rgba(45,10, 99, 0.6)",
            "rgba(128, 128, 128, 0.3)",
            "rgba(128, 128, 128, 0.34)",
            "rgba(128, 128, 128, 1.0)",
            "rgba(156,200,250,0)",
        ]
        self.invalid_rgba_colors = [
            "rgba(10)",
            "rgba(50, 100)",
            "rgba(120,199)",
            "rgba(1, 2, 3)",
            "rgba(128,255,127)",
            "rgba(128,255,127,A)",
            "rgba(128, 255, 127, A)",
            "rgba(128, 255, 127, 1.5)",
            "rgba(128, 255, 127, 0.6777777)",
            "rgba(128, 12, 35, 1, 1)",
            "rgba(128, 12, 35, 1, 1, 2)",
        ]

    def test_valid_serializer(self):
        data = {"color": self.valid_hex_full_color}
        serializer = SerializerWithColor(data=data)
        self.assertTrue(serializer.is_valid())

        data = {"color": self.valid_hex_short_color}
        serializer = SerializerWithColor(data=data)
        self.assertTrue(serializer.is_valid())

        data = {"color": self.valid_hexa_full_color}
        serializer = SerializerWithColor(data=data)
        self.assertTrue(serializer.is_valid())

        data = {"color": self.valid_hexa_short_color}
        serializer = SerializerWithColor(data=data)
        self.assertTrue(serializer.is_valid())

        for value in self.valid_rgb_colors:
            with self.subTest(f"RGB={value}"):
                data = {"color": value}
                serializer = SerializerWithColor(data=data)
                self.assertTrue(serializer.is_valid())

        for value in self.valid_rgba_colors:
            with self.subTest(f"RGBA={value}"):
                data = {"color": value}
                serializer = SerializerWithColor(data=data)
                self.assertTrue(serializer.is_valid())

    def test_invalid_serializer(self):
        data = {"color": self.invalid_hex_full_color1}
        serializer = SerializerWithColor(data=data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(DRFValidationError):
            serializer.is_valid(raise_exception=True)

        data = {"color": self.invalid_hex_full_color2}
        serializer = SerializerWithColor(data=data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(DRFValidationError):
            serializer.is_valid(raise_exception=True)

        data = {"color": self.invalid_hex_short_color1}
        serializer = SerializerWithColor(data=data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(DRFValidationError):
            serializer.is_valid(raise_exception=True)

        data = {"color": self.invalid_hex_short_color2}
        serializer = SerializerWithColor(data=data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(DRFValidationError):
            serializer.is_valid(raise_exception=True)

        data = {"color": self.invalid_hexa_full_color1}
        serializer = SerializerWithColor(data=data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(DRFValidationError):
            serializer.is_valid(raise_exception=True)

        data = {"color": self.invalid_hexa_full_color2}
        serializer = SerializerWithColor(data=data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(DRFValidationError):
            serializer.is_valid(raise_exception=True)

        data = {"color": self.invalid_hexa_short_color1}
        serializer = SerializerWithColor(data=data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(DRFValidationError):
            serializer.is_valid(raise_exception=True)

        data = {"color": self.invalid_hexa_short_color2}
        serializer = SerializerWithColor(data=data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(DRFValidationError):
            serializer.is_valid(raise_exception=True)

        for value in self.invalid_rgb_colors:
            with self.subTest(f"RGB={value}"):
                data = {"color": value}
                serializer = SerializerWithColor(data=data)
                self.assertFalse(serializer.is_valid())
                with self.assertRaises(DRFValidationError):
                    serializer.is_valid(raise_exception=True)

        for value in self.invalid_rgba_colors:
            with self.subTest(f"RGBA={value}"):
                data = {"color": value}
                serializer = SerializerWithColor(data=data)
                self.assertFalse(serializer.is_valid())
                with self.assertRaises(DRFValidationError):
                    serializer.is_valid(raise_exception=True)
