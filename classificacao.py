def classificar_pose(keypoints):
    if not keypoints:
        return "DESCONHECIDO"

    ombros = []
    quadris = []

    for ombro_idx, quadril_idx in [(11, 23), (12, 24)]:
        ombro = keypoints.get(ombro_idx)
        quadril = keypoints.get(quadril_idx)
        if ombro and quadril:
            dy = abs(ombro[1] - quadril[1])
            ombros.append(dy)

    if not ombros:
        return "DESCONHECIDO"

    dy_medio = sum(ombros) / len(ombros)

    if dy_medio < 0.05:
        return "DEITADO"
    elif dy_medio < 0.15:
        return "SENTADO"
    else:
        return "SAINDO"