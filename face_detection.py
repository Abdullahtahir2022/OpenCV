import cv2
import numpy as np

data = cv2.CascadeClassifier("data.xml")
img=cv2.imread('child.jpg',1)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face=data.detectMultiScale(gray,1.1,4)

for(x,y,w,h) in face:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('Random Pic',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows
