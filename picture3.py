import cv2
import numpy as np
array=[]

def mouse_click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        array.append(x)
        array.append(y)
        text=str(x)+ "," +str(y)
        cv2.putText(img,text,(x,y),2,1,(255,255,0),1)
        cv2.imshow('img',img)
        

    if event==cv2.EVENT_RBUTTONDOWN:
        cv2.destroyAllWindows
        width, height =400,400
        pt1=np.float32([[array[0],array[1]],[array[2],array[3]],
        [array[4],array[5]],[array[6],array[7]]])
        
        pt2=np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix=cv2.getPerspectiveTransform(pt1,pt2)
        outimg=cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow('img2',outimg)



img=cv2.imread('book.png',1)
cv2.imshow('img',img)

cv2.setMouseCallback('img',mouse_click)

cv2.waitKey(0)
cv2.destroyAllWindows