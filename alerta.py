from playsound import playsound

def gerar_alerta(status="SAINDO"):
    print(f"⚠️ ALERTA: {status}")
    #playsound("alerta.mp3")  # Coloque um som aqui


def verificar_alerta_pose(keypoints, bed_coords, frame_width, frame_height):
    if not keypoints or not bed_coords:
        return "DESCONHECIDO"

    x1, y1, x2, y2 = bed_coords

    def fora_da_cama(idx):
        if idx in keypoints:
            x, y = keypoints[idx]
            return not (x1 <= x * frame_width <= x2 and y1 <= y * frame_height <= y2)
        return True

    pernas_fora = sum([fora_da_cama(27), fora_da_cama(28)])
    quadris_fora = sum([fora_da_cama(23), fora_da_cama(24)])

    if quadris_fora == 2:
        return "FORA DA CAMA"
    elif pernas_fora == 2:
        return "2 PERNAS FORA"
    elif pernas_fora == 1:
        return "1 PERNA FORA"
    else:
        return "SENTADO"
