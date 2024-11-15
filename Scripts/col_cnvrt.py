import cv2
import numpy
img = cv2.imread("image/LOGO.png")
img1=img[:,:,2] #red color is removed
img2=img[:,:,1] #green color is removed
img3=img[:,:,0] #blue color is removed
cv2.imshow("window",img3)
cv2.waitKey(0)