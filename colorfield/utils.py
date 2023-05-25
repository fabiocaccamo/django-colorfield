import sys
try:
    from PIL import Image, UnidentifiedImageError
except ImportError:
    pass

def is_pil_installed() -> bool:
    """
        Check for pil / pillow package in system modules
    """
    return "PIL" in sys.modules

def get_image_background_color(img, alpha=False):
    img = img.convert("RGBA" if alpha else "RGB")
    pixel_color = img.getpixel((1, 1))
    color_format = "#" + "%02x" * len(pixel_color)
    color = color_format % pixel_color
    color = color.upper()
    return color


def get_image_file_background_color(img_file, alpha=False):
    color = ""
    try:
        if is_pil_installed():
            with Image.open(img_file) as image:
                color = get_image_background_color(image, alpha)
        else:
            color = "#000000"
    except UnidentifiedImageError:
        pass
    return color
