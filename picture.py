import cv2
import numpy as np

#kernal required for dialation 
kernal=np.ones((5,5),np.uint8)

#reading images
img=cv2.imread('abdullah.jpg',1)

#conversion
imgG=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

imgB=cv2.GaussianBlur(imgG,(11,11),0)
imgcanny=cv2.Canny(imgG,50,50)
#part of canny used to thicken the curves
imgDialation=cv2.dilate(imgcanny,kernal,iterations=1)
#part of canny dialation used to thin the curves
imgerode=cv2.erode(imgDialation,kernal,iterations=1)



#cv2.imshow('GRAY',imgG)
#cv2.imshow('BLUR',imgB)
cv2.imshow('CANNY',imgcanny)
cv2.imshow('canny dialation',imgDialation)
cv2.imshow('CANNY erode',imgerode)

# responsive keys to shut windows
key=cv2.waitKey(0)
if key==27:
    cv2.destroyAllWindows()
elif key==ord('s'):
    cv2.imwrite('copy.png',img)
    cv2.destroyAllWindows() 


