import cv2
import numpy
img= cv2.imread("image/LOGO.png")
img_resize = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))
print(img_resize.shape)
cv2.imshow("window",img_resize)
cv2.waitKey(0)