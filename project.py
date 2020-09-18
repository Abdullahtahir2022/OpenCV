import cv2
##########################################
numberCascade= cv2.CascadeClassifier("number.xml")
###########################################
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    number = numberCascade.detectMultiScale(imgGray,1.1,4)
    for (x,y,w,h) in number:
        area=w*h
        if area>500:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,'number plate',(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,0),2)
            imgroi=img[y:y+h,x:x+w]
            cv2.imshow('Number Plate',imgroi)

        



    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('scanned.jpg',imgroi)
        break