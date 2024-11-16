import cv2 
import numpy
import time

cap= cv2.VideoCapture('first_video.avi')

while True:
    ret,frame= cap.read()
    time.sleep(1/10)
    cv2.imshow("webcam",frame)

    if cv2.waitKey(1)& 0xFF== ord('x'):
        break
cv2.destroyAllWindows()
