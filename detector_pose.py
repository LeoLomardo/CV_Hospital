import mediapipe as mp
import cv2

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

pose = mp_pose.Pose(
    static_image_mode=False,         
    model_complexity=2,             # define precisao 0,1,2, qnt maior mais preciso
    smooth_landmarks=True,           
    enable_segmentation=False,       # Desativado por padrão
    min_detection_confidence=0.75,  # Rejeita detecções fracas
    min_tracking_confidence=0.75    # Rejeita rastreamentos fracos
)

drawing_spec = mp_drawing.DrawingSpec(color=(255,0,0), thickness=2, circle_radius=2)

def detectar_pose(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(rgb)

    keypoints = {}
    if result.pose_landmarks:
        for idx, lm in enumerate(result.pose_landmarks.landmark):
            if lm.visibility > 0.5:  # ajustável após testes
                keypoints[idx] = (lm.x, lm.y)
        
        mp_drawing.draw_landmarks(
            frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=drawing_spec,
            connection_drawing_spec=drawing_spec
        )
    return keypoints