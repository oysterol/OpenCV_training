import cv2
import numpy as np
from color_selector import color_reader

def empty():
        pass    


myPoints=[]

def findColor(img,color_val,color):
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower,upper=np.asfarray(color_val[0]),np.asfarray(color_val[1])
   # lower=np.array([lower])
   # upper=np.array([upper])
    newPoints=[]
    mask=cv2.inRange(imgHSV,lower,upper)
    x,y=getContours(mask)
    cv2.circle(imgResult,(x,y),10,color,cv2.FILLED)
    newPoints.append([x,y,color])
    cv2.imshow("img_{}".format(color),mask)
    return newPoints

def drawOnCanvas(myPoints):
    for point in myPoints:
       # print(point[2])
        cv2.circle(imgResult,(point[0],point[1]),10,point[2],cv2.FILLED)


def getContours(img):

    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>300:
            #cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            peri =cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h=cv2.boundingRect(approx)
    return x+int(w/2),y

    
cap=cv2.VideoCapture(0)
###3 =width
cap.set(3,640)
####4=height
cap.set(4,480)
####10=brightness
cap.set(10,150)
colors=['red','blue']
myColors=[]
MyColorValues=[[0,0,255],
        [255,0,0]]
for color in colors:
    myColors.append(color_reader(color))
while True:
    success, img= cap.read()
    imgResult=img.copy()
    for i in range(len(colors)):
            new_points=findColor(img,myColors[i],MyColorValues[i])
            if len(new_points)!=0:
                for point in new_points:
                    myPoints.append(point)
    if len(myPoints)>0:
        drawOnCanvas(myPoints)
    cv2.imshow("Video",imgResult)
    ###add press q to break loop
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
