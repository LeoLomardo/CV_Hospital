import math

def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def classificar_pose(keypoints):
    if not keypoints:
        return "DESCONHECIDO"

    # Indices mediapipe, catei na internet, ainda nao olhei com calma
    OMBROS = [11, 12]
    QUADRIS = [23, 24]
    TORNOZELOS = [27, 28]
    JOELHOS = [25, 26]

    dy_ombro_quadril = []
    comprimento_corpo = []

    for o, q, t in zip(OMBROS, QUADRIS, TORNOZELOS):
        ombro = keypoints.get(o)
        quadril = keypoints.get(q)
        tornozelo = keypoints.get(t)

        if ombro and quadril:
            dy = abs(ombro[1] - quadril[1])
            dy_ombro_quadril.append(dy)

        if ombro and tornozelo:
            corpo = distancia(ombro, tornozelo)
            comprimento_corpo.append(corpo)

    if not dy_ombro_quadril or not comprimento_corpo:
        return "DESCONHECIDO"

    # normaliza
    media_dy = sum(dy_ombro_quadril) / len(dy_ombro_quadril)
    media_corpo = sum(comprimento_corpo) / len(comprimento_corpo)
    proporcao = media_dy / media_corpo  # Quanto o tronco está "dobrado"

    # Logica de decisao porca, falta calcular direito e definir condicoes de maneira mais precisa, esse else "SAINDO" ta uma m***a
    if proporcao < 0.15:
        return "DEITADO"
    elif proporcao < 0.35:
        return "SENTADO"
    else:
        return "SAINDO"
