import io
import cv2
import base64
import numpy as np
from PIL import Image
from io import BytesIO

def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    print(imgdata)
    image = Image.open(io.BytesIO(imgdata))
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)

def cropImage(img, x, y, margin=None):
    if margin == None:
        margin = 25

    y1, y2 = int(y) - int(margin), int(y) + int(margin)
    x1, x2 = int(x) - int(margin), int(x) + int(margin)
    return img[y1:y2, x1:x2]

def imgTo64(img):
    pil_img = Image.fromarray(img)
    buff = BytesIO()
    pil_img.save(buff, format="JPEG")
    new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")
    return "data:image/png;base64, " + str(new_image_string)

# imagem = cv2.imread("img.jpg")
# imagem = cropImage(imagem, 25, 25)
# cv2.imshow('teste', imagem)
# cv2.waitKey()
#
# print(imgTo64(imagem))
