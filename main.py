import cv2
from detector_pose import detectar_pose
from classificacao import classificar_pose
from alerta import gerar_alerta, verificar_alerta_pose
from cama import detectar_cama
import os

# Modo de captura da camera atraves do IP/PORTA dela
#url = "rtsp://stream:123stream123@11.0.0.101:554/cam/realmonitor?channel=1&subtype=0"
#video = cv2.VideoCapture(url)

# Modo de captura da camera default do computador

#Melhores resultados
#video_path = "/home/leo/Documentos/LES/Videos_VisComp/PA43-4320_convertido.mp4"
#video_path = "/home/leo/Documentos/LES/Videos_VisComp/PA44-4411_convertido.mp4"
#video_path = "/home/leo/Documentos/LES/Videos_VisComp/PA_44_convertido.mp4"
#video_path = "/home/leo/Documentos/LES/Videos_VisComp/4210.1_convertido.mp4"
#video_path = "/home/leo/Documentos/LES/Videos_VisComp/4210.2_convertido.mp4"


#Outros videos
video_path = "/home/leo/Documentos/LES/Videos_VisComp/4321_convertido.mp4"

video = cv2.VideoCapture(video_path)

#Para utilizar a webcam do computador:
#video = cv2.VideoCapture(0)

if not video.isOpened():
    print("ERROR: Nao conseguiu abrir o video!\n")
    exit()


bed_coords = None
frame_count = 0
DETECT_INTERVAL = 30  # taxaCamera x qnts segundos de intervalo 

while True:
    ret, frame = video.read()
    if not ret:
        break

    frame_height, frame_width = frame.shape[:2]
    frame_count += 1

    
    if bed_coords is None or frame_count % DETECT_INTERVAL == 0:
        nova = detectar_cama(frame)
        if nova:
            bed_coords = nova

    # desenha deteccao da cama
    if bed_coords:
        cv2.rectangle(frame,
                      (bed_coords[0], bed_coords[1]),
                      (bed_coords[2], bed_coords[3]),
                      (0, 255, 0), 2)

    # deteccao de pose e alerta
    keypoints = detectar_pose(frame)
    # ATENCAO: ordem correta width, height **
    status = verificar_alerta_pose(keypoints, bed_coords, frame_width, frame_height)
    if status in ("1 PERNA FORA", "2 PERNAS FORA", "FORA DA CAMA", "SAINDO"):
        gerar_alerta(status)


    cv2.putText(frame, f"Status: {status}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    escala = 0.5 # ajuste escala da janela, cosmetico para testes
    frame_resized = cv2.resize(frame, (0, 0), fx=escala, fy=escala)
    cv2.imshow("Monitor UTI", frame_resized)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()