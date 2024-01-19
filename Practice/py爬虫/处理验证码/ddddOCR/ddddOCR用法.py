from ddddocr import DdddOcr

ocr= DdddOcr(show_ad=False)
with open('../img/yzm.jpg', mode='rb') as f:
    image = f.read()
res = ocr.classification(image)
print(res)