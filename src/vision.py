import cv2
import easyocr

image_path = "../input/terms.jpg"
image = cv2.imread(image_path)
reader = easyocr.Reader(['en'])
text = reader.readtext(image)
for i in text:
    print(i)
