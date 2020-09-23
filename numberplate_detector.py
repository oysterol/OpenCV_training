import cv2
import numpy as np

#######################
frameWidth=640
frameHeight=480
minarea=200
color=[0,255,0]
nPlateCascade=cv2.CascadeClassifier("Resources/russian_lienceplate_cascade.xml")
##################3
cap=cv2.VideoCapture(0)
###3 =width
cap.set(3,640)
####4=height
cap.set(4,480)
####10=brightness
cap.set(10,100)
i=0
count=0
while True:
    success, img= cap.read()
    imgResize=cv2.resize(img,(640,480))
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    numberPlates=nPlateCascade.detectMultiScale(imgGray,1.71,4)
    for (x,y,w,h) in numberPlates:
        area=w*h
        if area>minarea:
            
            cv2.rectangle(imgResize,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,color,2)
            imgRoi=img[y:y+h,x:w+x]
            cv2.imshow("ROI",imgRoi)


    cv2.imshow("Result",img)
    cap.set(10,i)


    ###add press q to break loop
    if cv2.waitKey(1) & 0xFF ==ord('s'):
        cv2.imwrite("Resources/Scanned/Nr_plate_"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved", (150,265), cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count+=1

           
    elif cv2.waitKey(1) & 0xFF ==ord('q'):
        break
