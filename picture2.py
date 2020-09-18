import cv2
import numpy as np



img=cv2.imread('abdullah.jpg',1)
#put line
img=cv2.line(img,(0,0),(650,650),(255,255,2),8)
#put rectangle
img=cv2.rectangle(img,(0,0),(650,650),(255,255,2),8)
#put circle
img=cv2.circle(img,(200,200),200,(255,2,2),4)
#put text
img=cv2.putText(img,"Hello",(300,300),2,2,(255,2,2),5)



cv2.imshow('img',img)
cv2.waitKey(0)
