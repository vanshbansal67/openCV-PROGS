import cv2
import numpy
img = numpy.zeros((512,512,3))
cv2.rectangle(img,pt1=(100,100),pt2=(300,50),color =(255,0,0),thickness= 3)
cv2.imshow("window",img)
cv2.waitKey(0)