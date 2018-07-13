import cv2
import base64
import numpy as np

def stringToImage(base64_string):
    ''' Base64 to Numpy Array'''
    if ', ' in base64_string:
        _, base64_string = base64_string.split(', ')
    elif ',' in base64_string:
        _, base64_string = base64_string.split(',')
    img = base64.b64decode(base64_string)
    np_img = np.fromstring(img, dtype=np.uint8)
    image = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    return image

def cropImage(image, x, y, margin=None):
    ''' Crop image '''
    if margin == None: margin = 25
    y1, y2 = y - margin, y + margin
    x1, x2 = x - margin, x + margin
    return image[y1:y2, x1:x2]

def imageTo64(img):
    ''' Numpy Array to Base64 '''
    _, data = cv2.imencode('.png', img)
    bytes = data.tobytes()
    b64 = "data:image/png;base64, " + base64.b64encode(bytes).decode("utf-8")
    return b64

def getCropImg(b64, x, y, margin=None):
    ''' Crop Base64 Images'''
    img = stringToImage(b64)
    img_crop = cropImage(img, x, y, margin)
    base64_string = imageTo64(img_crop)
    return base64_string
