import cv2

cap = cv2.VideoCapture(0)


from picamera import PiCamera
from time import sleep
camera = PiCamera()

camera.start_preview(fullscreen=False, window = (100, 20, 640, 480))

while(True):
    _, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
