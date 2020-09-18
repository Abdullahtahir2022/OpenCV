import cv2
import numpy as np

def gcontours(img):
    contours, hierarcy= cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        #area=cv2.contourArea(cnt)
        cv2.drawContours(imgc,cnt,-1,(255,0,0),1)
        cv2.imshow("cont",imgc)


#reading images
img=cv2.imread('shape.png',1)
imgc=img.copy()



imgB=cv2.GaussianBlur(img,(11,11),0)

imgcanny=cv2.Canny(imgB,50,50)

gcontours(imgcanny)






#cv2.imshow('CANNY',imgcanny)


# responsive keys to shut windows
key=cv2.waitKey(0)
if key==27:
    cv2.destroyAllWindows()
elif key==ord('s'):
    cv2.imwrite('copy.png',img)
    cv2.destroyAllWindows() 


