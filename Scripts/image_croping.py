import cv2
import numpy
img= cv2.imread("image/LOGO.png")
img_crop = img[30:500,200:500]
cv2.imshow("window",img_crop)
cv2.waitKey(0)