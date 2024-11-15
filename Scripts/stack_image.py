import cv2
import numpy
img = cv2.imread("image/LOGO.png")
imgred=img[:,:,2]
imggreen=img[:,:,1]
imgblue=img[:,:,0]
new_img= numpy.hstack((imgred,imggreen,imgblue))
cv2.imshow("window",new_img)
cv2.waitKey(0)