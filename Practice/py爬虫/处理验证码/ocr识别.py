import tesserocr
from PIL import Image
import Pillow


image = Image.open('captcha.png')
result = tesserocr.image_to_text(image)
print(result)