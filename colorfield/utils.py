# -*- coding: utf-8 -*-


def get_image_background_color(img, alpha=False):
    img = img.convert('RGBA' if alpha else 'RGB')
    pixel_color = img.getpixel((1, 1))
    color_format = '#' + '%02x' * len(pixel_color)
    color = color_format % pixel_color
    color = color.upper()
    return color
