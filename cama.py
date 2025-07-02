import cv2
import numpy as np

def detectar_cama(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    edges = cv2.Canny(blur, 30, 100)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cama_contorno = None
    area_max = 0
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        area = w * h
        aspect_ratio = w / h

        if area > area_max and 1.5 < aspect_ratio < 5:  # formato retangular horizontal
            area_max = area
            cama_contorno = (x, y, x + w, y + h)

    return cama_contorno