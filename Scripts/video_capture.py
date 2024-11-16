import cv2
import numpy
cap = cv2.VideoCapture(0)
while True:
    ret,frame= cap.read()
    video_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("webcam",video_gray)


    if cv2.waitKey(1)& 0xFF== ord('x'):
        break
cv2.destroyAllWindows()