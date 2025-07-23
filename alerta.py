from playsound import playsound
from classificacao import classificar_pose

def gerar_alerta(status="SAINDO"):
    print(f"ALERTA: {status}")
    # playsound("alerta.mp3")  # descomente para som

def verificar_alerta_pose(keypoints, bed_coords, frame_width, frame_height):
    """
    keypoints: dict {idx: (x_norm, y_norm)}
    bed_coords: (x1, y1, x2, y2) em pixels
    frame_width, frame_height: dimensões do frame em pixels
    """
    if not keypoints or not bed_coords:
        return "DESCONHECIDO"

    x1, y1, x2, y2 = bed_coords

    def fora_da_cama(idx):
        if idx in keypoints:
            x_px = keypoints[idx][0] * frame_width
            y_px = keypoints[idx][1] * frame_height
            return not (x1 <= x_px <= x2 and y1 <= y_px <= y2)
        return True

    pernas_fora = sum(fora_da_cama(i) for i in (27, 28))   # tornozelos
    quadris_fora = sum(fora_da_cama(i) for i in (23, 24))  # quadris

    # 1) se estiver saindo / erguendo (distância ombro-quadril grande)
    postura = classificar_pose(keypoints)
    if postura == "SAINDO":
        return "SAINDO"

    # 2) se os quadris já ultrapassaram a cama
    if quadris_fora == 2:
        return "FORA DA CAMA"
    # 3) perna(s) fora
    if pernas_fora == 2:
        return "2 PERNAS FORA"
    if pernas_fora == 1:
        return "1 PERNA FORA"
    if postura == "DEITADO":
        return "DEITADO"
    return "SENTADO"
