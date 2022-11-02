import pytesseract
from PIL import Image


def extract_text(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text
