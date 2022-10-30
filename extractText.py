import pytesseract
from PIL import Image

filename = 'test.png'
text = pytesseract.image_to_string(Image.open(filename))
print(text)