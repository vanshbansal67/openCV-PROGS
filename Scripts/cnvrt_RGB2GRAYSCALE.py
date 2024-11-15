import cv2
import numpy
img = cv2.imread("image/LOGO.png")
img_gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("window",cv2.resize(img_gray,(750,750)))
cv2.waitKey(0)

# print(img_gray)