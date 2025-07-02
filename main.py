import cv2
from detector_pose import detectar_pose
from classificacao import classificar_pose
from alerta import gerar_alerta, verificar_alerta_pose
from cama import detectar_cama
import os

# Modo de captura da camera atraves do IP/PORTA dela
    #url = "https://10.0.1.59:8080/video"
    #video = cv2.VideoCapture(url)

# Modo de captura da camera default do computador
video = cv2.VideoCapture(0) #pra pegar default camera pc

bed_coords = None
frame_count = 0
DETECT_INTERVAL = 30 #Imagino que essas cameras sejam 30fps, logo 1 atualizacao da cama por segundo serve

while True:
    ret, frame = video.read()
    if not ret:
        break

    frame_height, frame_width = frame.shape[:2]


    frame_count += 1
    if bed_coords is None or frame_count % DETECT_INTERVAL == 0:
        nova_cama = detectar_cama(frame)
        if nova_cama:
            bed_coords = nova_cama

    if bed_coords:
        x1, y1, x2, y2 = bed_coords
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
    else:
        bed_coords = (100, 100, 540, 380)  # fallback padrão

    keypoints = detectar_pose(frame)
    status = verificar_alerta_pose(keypoints, bed_coords, frame_height, frame_width)


    if status in ["1 PERNA FORA", "2 PERNAS FORA", "FORA DA CAMA"]:
        gerar_alerta(status)

    cv2.putText(frame, f"Status: {status}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Monitor UTI", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()