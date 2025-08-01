from ultralytics import YOLO
import cv2


model_path = "/home/leo/Documentos/LES/CV_Hospital/runs/detect/train2/weights/best.pt"
modelo_cama = YOLO(model_path)


#Funcoes relacionadas a detectar cama estao funcionando corretamente, basta apenas aumentar o dataset para melhorar a acuracia
def detectar_cama(frame):
    #results = modelo_cama(frame, verbose=False)[0]
    results = modelo_cama.predict(source= frame, verbose = False)[0]
    if not results.boxes:
        print("Nenhuma cama detectada neste frame.")
        return None

    for box in results.boxes:
        classe = int(box.cls[0])
        if classe == 0:  # 'Bed', talvez no futuro treinar um modelo detectando 'bed_arm', 'mattress', etc... mas por enquanto ele identifica tudo como 'Bed'
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            print(f"Cama detectada: ({x1}, {y1}, {x2}, {y2})")
            return (x1, y1, x2, y2)

    print("Cama nao identificada.")
    return None