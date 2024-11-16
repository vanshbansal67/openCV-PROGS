import cv2
import numpy
flag=False
ix=-1
iy=-1
def draw(event,x,y,flags,params):
    global ix,iy,flag
    if event==1:
        flag= True
        ix=x
        iy=y
    elif event==0:
        flag= True
        
          #  cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,255,0),thickness=-1)
        
    elif event==4:
        flag=False
        cv2.rectangle(img,pt1 =(ix,iy),pt2=(x,y),color=(55,85,99),thickness=-1)
        

cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",draw)
    
img= numpy.zeros((512,512,3)) 
#img2= cv2.imread("image/LOGO.png")
#cv2.waitKey(0)
while True:
    cv2.imshow("window",img)
    if cv2.waitKey(1)& 0xFF==ord('x'):
        break
cv2.destroyAllWindows()