import base64

import cv2
import numpy as np

from backend.models import Trap_Image_Data


def b64_2_img(b64):
    # NOTE: Converte imagem em base64 para imagem numpy
    if ', ' in b64:
        _, b64 = b64.split(', ')
    elif ',' in b64:
        _, b64 = b64.split(',')
    byte_img = base64.b64decode(b64)
    np_img = np.fromstring(byte_img, dtype=np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    return img


def crop_image(img, x, y, margin=None):
    # NOTE: Corta imagem numpy
    if margin == None:
        margin = 25
    y1, y2 = y - margin, y + margin
    x1, x2 = x - margin, x + margin
    return img[y1:y2, x1:x2]


def img_2_b64(img):
    # NOTE: Converte uma imagem numpy para base64
    _, data = cv2.imencode('.png', img)
    bytes = data.tobytes()
    b64 = "data:image/png;base64, " + base64.b64encode(bytes).decode("utf-8")
    return b64


def get_cropped_img(b64, x, y, margin=None):
    # NOTE: Corta imagens no formato base64
    img = b64_2_img(b64)
    img_crop = crop_image(img, x, y, margin)
    base64_string = img_2_b64(img_crop)
    return base64_string


def cut_petri(imagem):
    # NOTE: Corta a regiao exterior a placa de petri
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    cinza = cv2.medianBlur(cinza, 125)
    ret, thresh = cv2.threshold(cinza, 155, 255, cv2.THRESH_BINARY_INV)
    dilation = cv2.dilate(thresh, np.ones((5, 5), np.uint8), iterations=15)
    erosion = cv2.erode(dilation, np.ones((5, 5), np.uint8), iterations=15)

    rows = thresh.shape[0]
    circles = cv2.HoughCircles(erosion, cv2.HOUGH_GRADIENT, 18, rows, param2=22,
                               minRadius=int(rows / 4), maxRadius=int(rows / 2))

    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center, radius = (i[0], i[1]), i[2]

    cv2.circle(imagem, (center[0], center[1]), radius, (0, 255, 255), 4)

    h, w = imagem.shape[:2]
    Y, X = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((X - center[0]) ** 2 + (Y - center[1]) ** 2)
    mask = dist_from_center <= radius
    imagem[~mask] = 0

    y, y1 = int(center[1] - radius), int(center[1] + radius)
    x, x1 = int(center[0] - radius), int(center[0] + radius)
    imagem = imagem[y:y1, x:x1]

    y, x = imagem.shape[:2]
    y, x = int(y / 2), int(x / 2)
    return imagem, x, y, radius


def get_contours(imagem):
    # NOTE: Realiza as operações com a imagem
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(cinza, 110, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    thresh, contours, hierarchy = cv2.findContours(
        closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    return contours


def get_dist_ab(xC, xA, yC, yA):
    # NOTE: Retorna a distancia entre o afideo e o centro da placa de petri
    return np.sqrt(((xC - xA) ** 2) + ((yC - yA) ** 2))
