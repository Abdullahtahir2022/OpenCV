import cv2
from datetime import datetime

cam=cv2.VideoCapture(0);



while(cam.isOpened):
    ret, frame = cam.read()
 
    
    frame=cv2.putText(frame,str(datetime.now()),(10,50), 4, 1, (0,255,0), 1,cv2.LINE_AA)  

    cv2.imshow('img',frame)
    key=cv2.waitKey(1)
    if(key==27 or key==ord('q')):
        break

    
cam.release() 
cv2.destroyAllWindows() 







