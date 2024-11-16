import cv2
import numpy
def draw(event,x,y,flags,params):
    if event==1:
        cv2.circle(img2,center=(x,y),radius=50,color=(55,85,99),thickness=-1)
        #print("mouse moved")
    elif event==1:
        #cv2.rectangle(img,pt1=())
        print("dowm pressed")
    elif event==4:
        print("mouse down dropped")

cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",draw)
    
img= numpy.zeros((512,512,3)) 
img2= cv2.imread("image/LOGO.png")
#cv2.waitKey(0)
while True:
    cv2.imshow("window",img2)
    if cv2.waitKey(1)& 0xFF==ord('x'):
        break
cv2.destroyAllWindows()