import cv2


def interpretSign(fingers, frame):
    font = cv2.FONT_HERSHEY_SIMPLEX

    origin = (20, 80)
    color = (0, 0, 0)
    if fingers == [1, 1, 0, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'A', origin, font, 3, color, 2, cv2.LINE_AA)

    if fingers == [0, 0, 0, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'E', origin, font, 3, color, 2, cv2.LINE_AA)

    if fingers == [0, 0, 1, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'I', origin, font, 3, color, 2, cv2.LINE_AA)

    if fingers == [1, 0, 1, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'O', origin, font, 3, color, 2, cv2.LINE_AA)

    if fingers == [0, 0, 1, 0, 0, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'U', origin, font, 3, color, 2, cv2.LINE_AA)

    if fingers == [0, 0, 1, 1, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'B', origin, font, 3, color, 2, cv2.LINE_AA)

    if fingers == [0, 0, 0, 0, 0, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'D', origin, font, 3, color, 2, cv2.LINE_AA)

    if fingers == [1, 1, 0, 0, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'K', origin, font, 3, color, 2, cv2.LINE_AA)

    if fingers == [1, 1, 0, 0, 0, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'L', origin, font, 3, color, 2, cv2.LINE_AA)

    if fingers == [0, 1, 0, 1, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'W', origin, font, 3, color, 2, cv2.LINE_AA)

    if fingers == [0, 1, 0, 0, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'N', origin, font, 3, color, 2, cv2.LINE_AA)

    if fingers == [1, 1, 1, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'Y', origin, font, 3, color, 2, cv2.LINE_AA)

    if fingers == [1, 1, 1, 1, 1, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'F', origin, font, 3, color, 2, cv2.LINE_AA)

    if fingers == [0, 1, 1, 1, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'P', origin, font, 3, color, 2, cv2.LINE_AA)

    if fingers == [0, 1, 0, 0, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'V', origin, font, 3, color, 2, cv2.LINE_AA)

    return fingers
