import cv2
import numpy
img = numpy.zeros((512,512,3))
cv2.circle(img,center=(256,256),radius =250,color=(0,0,255),thickness= 3)
cv2.imshow("window",img)
cv2.waitKey(0)