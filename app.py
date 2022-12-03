import cv2
import mediapipe as mp

from Utils.interpreter import interpretSign
from Utils.normalizeCords import getAngles

current_read = 0

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
mp_drawing_styles = mp.solutions.drawing_styles

cap = cv2.VideoCapture(0)

wCam, hCam = 1280, 720
cap.set(3, wCam)
cap.set(4, hCam)

with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.75) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        height, width, _ = frame.shape
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks is not None:
            angleId = getAngles(results, width, height)[0]

            fingers = []

            if angleId[5] > 125:
                fingers.append(1)
            else:
                fingers.append(0)

            if angleId[4] > 150:
                fingers.append(1)
            else:
                fingers.append(0)

            for index in range(0, 4):
                if angleId[index] > 90:
                    fingers.append(1)
                else:
                    fingers.append(0)

            totalFingers = fingers.count(1)
            interpretSign(fingers, frame)

            pinky = getAngles(results, width, height)[1]
            pinkY = pinky[1] + pinky[0]
            resta = pinkY - current_read
            current_read = pinkY
            print(abs(resta), pinkY, current_read)

            if fingers == [0, 0, 1, 0, 0, 0]:
                if abs(resta) > 30:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
                    cv2.putText(frame, 'J', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
