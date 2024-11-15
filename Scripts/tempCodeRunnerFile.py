import cv2
import numpy
img= cv2.imread("image/LOGO.png")
cv2.imshow("window",img)  #(288,466) is the original size of the image
# print(img.shape)
cv2.resize(img,(512,512))
cv2.waitKey(0)