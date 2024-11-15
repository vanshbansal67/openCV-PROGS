import cv2
import numpy
img = numpy.zeros((512,512,3))
cv2.line(img,pt1=(0,0),pt2=(0,256),color =(23,54,37),thickness= 30)
cv2.imshow("window",img)
cv2.waitKey(0)