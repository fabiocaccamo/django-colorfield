# -*- coding: utf-8 -*-

from django.test import TestCase
from rest_framework.serializers import Serializer
from rest_framework.serializers import ValidationError as DRFValidationError

from colorfield.serializers import ColorField


class SerializerWithHexColor(Serializer):
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

    def test_valid_serializer(self):
        data = {"color": self.valid_hex_full_color}
        serializer = SerializerWithHexColor(data=data)
        self.assertTrue(serializer.is_valid())

        data = {"color": self.valid_hex_short_color}
        serializer = SerializerWithHexColor(data=data)
        self.assertTrue(serializer.is_valid())

        data = {"color": self.valid_hexa_full_color}
        serializer = SerializerWithHexColor(data=data)
        self.assertTrue(serializer.is_valid())

        data = {"color": self.valid_hexa_short_color}
        serializer = SerializerWithHexColor(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_serializer(self):
        data = {"color": self.invalid_hex_full_color1}
        serializer = SerializerWithHexColor(data=data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(DRFValidationError):
            serializer.is_valid(raise_exception=True)

        data = {"color": self.invalid_hex_full_color2}
        serializer = SerializerWithHexColor(data=data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(DRFValidationError):
            serializer.is_valid(raise_exception=True)

        data = {"color": self.invalid_hex_short_color1}
        serializer = SerializerWithHexColor(data=data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(DRFValidationError):
            serializer.is_valid(raise_exception=True)

        data = {"color": self.invalid_hex_short_color2}
        serializer = SerializerWithHexColor(data=data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(DRFValidationError):
            serializer.is_valid(raise_exception=True)

        data = {"color": self.invalid_hexa_full_color1}
        serializer = SerializerWithHexColor(data=data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(DRFValidationError):
            serializer.is_valid(raise_exception=True)

        data = {"color": self.invalid_hexa_full_color2}
        serializer = SerializerWithHexColor(data=data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(DRFValidationError):
            serializer.is_valid(raise_exception=True)

        data = {"color": self.invalid_hexa_short_color1}
        serializer = SerializerWithHexColor(data=data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(DRFValidationError):
            serializer.is_valid(raise_exception=True)

        data = {"color": self.invalid_hexa_short_color2}
        serializer = SerializerWithHexColor(data=data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(DRFValidationError):
            serializer.is_valid(raise_exception=True)
