import mediapipe as mp
import cv2

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

def detectar_pose(frame):
    #entender as flags dessa funcao cvtColor()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(rgb)

    keypoints = {}
    if result.pose_landmarks:
        for idx, lm in enumerate(result.pose_landmarks.landmark):
            if lm.visibility > 0.5:  # confiabilidade minima, falta realizar testes para chegar em valor aceitável
                keypoints[idx] = (lm.x, lm.y)
        mp_drawing.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    return keypoints

