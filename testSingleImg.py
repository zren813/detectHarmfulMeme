from detoxify import Detoxify
import pytesseract
from PIL import Image

filename = '04125.png'
text = pytesseract.image_to_string(Image.open(filename))
print(text)

results = Detoxify('original').predict(text)['toxicity']
if results >= 0.2:
    print("toxic!")
else:
    print("not toxic.")
