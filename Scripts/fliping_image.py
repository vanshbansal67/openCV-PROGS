import cv2
import numpy
img= cv2.imread("image/LOGO.png")
img_flip1=cv2.flip(img,0) #flip the image in vertical direction
img_flip2=cv2.flip(img,1) #flip the image in horizontal direction
img_flip3=cv2.flip(img,-1) #flip the image in both direction
cv2.imshow("window",img_flip1)
cv2.waitKey(0)