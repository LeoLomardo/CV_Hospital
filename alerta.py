from playsound import playsound
from classificacao import classificar_pose

def gerar_alerta(status="SAINDO"):
    print(f"ALERTA: {status}")


def verificar_alerta_pose(keypoints, bed_coords, frame_width, frame_height):
    """
    keypoints: dict {idx: (x_norm, y_norm)}
    bed_coords: (x1, y1, x2, y2) em pixels
    frame_width, frame_height: dimensoes do frame em pixels
    """
    if not keypoints or not bed_coords:
        return "DESCONHECIDO"

    x1, y1, x2, y2 = bed_coords

    def fora_da_cama(px, py):
        return not (x1 <= px <= x2 and y1 <= py <= y2) # se coordenada nao esta dentro dos limites de x E y ele ta fora da cama

    total_fora = 0
    total_dentro = 0
    for idx, (x_norm, y_norm) in keypoints.items():
        x_px = x_norm * frame_width
        y_px = y_norm * frame_height
        if fora_da_cama(x_px, y_px):
            total_fora += 1
        else:
            total_dentro += 1

    if total_fora == 0:
        return "DEITADO"
    elif total_fora <= 2:
        return "PARTES FORA"
    else:
        return "FORA DA CAMA"