import cv2
import numpy as np


""" 
#####How to import images and display them

###Import image
img=cv2.imread("path")
###Show image and add delay 0=infinite, 1000 = 1 second etc...
cv2.imshow("output", img)
cv2.waitKey(0)

######How to import video

###Import video
cap=cv2.VideoCapture("/path")

####Go through each frame of the video
while True:
    success, img= cap.read()
    ##show img
    cv2.imshow("Video",img)
    ###add press q to break loop
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

###
###Import webcam picture ad set certain dimensions 0 ==local webcam
cap=cv2.VideoCapture(0)
###3 =width
cap.set(3,640)
####4=height
cap.set(4,480)
####10=brightness
cap.set(10,100)
i=0
while True:
    success, img= cap.read()
    ##show img
    i+=0.1
    cv2.imshow("Video",img)
    cap.set(10,i)
    ###add press q to break loop
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
 """

""" 
###testing different functions
kernel= np.ones((5,5),np.uint8)
img=cv2.imread("Resources/Gruppebilde_1.jpg")

###Make greyscale
imgGray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
###blur image
imgBlur=cv2.GaussianBlur(imgGray, (7,7),0)
### Canny image i.e find edges
imgCanny=cv2.Canny(imgGray, 100,100)
###make edges thicker
imgDialation=cv2.dilate(imgCanny, kernel,iterations=1)
###make edges smaller
imgEroded=cv2.erode(imgDialation, kernel, iterations=1)
cv2.imshow("imgcanny", imgCanny)
cv2.imshow("imgdial",imgDialation)
cv2.imshow("imgerod", imgEroded)
cv2.waitKey(0) """


""" 
###Cropping and resizing
img=cv2.imread("Resources/Gruppebilde_1.jpg")
print(img.shape)
imgResize=cv2.resize(img,(300,200))
imgCropped=img[0:300,0:500]
cv2.imshow("test", imgCropped)
cv2.waitKey(0) """

""" 
####coloring different (rectangels) parts of a picture
img = np.zeros((512,512,3),np.uint8)
img[200:300,100:300]=255,0,0
img[:]=0,255,0
cv2.imshow("img",img)
 """

"""
###different functions to add shapes onto image
img = np.zeros((512,512,3),np.uint8)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),3)
cv2.rectangle(img,(0,0),(250,350),(0,255,0),cv2.FILLED)
cv2.circle(img, (400,50),30,(255,0,255),5)
cv2.putText(img, "Open CV text",(300,200),cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255))
cv2.imshow("img",img)
cv2.waitKey(0)
"""

""" 
###Warping images points (on screen px), and points 2 (location of points)
img=cv2.imread("Resources/stocky_thingy.jpg")
width,height=250,350
pts1=np.float32([[856,229],[1095,389],[844,713],[617,522]])
pts2=np.float32([[0,0],[width,0],[width,height],[0,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOut=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("img",img)
cv2.imshow("imgw",imgOut)
cv2.waitKey(0) """




""" 
####Color detection
def empty():
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)
cv2.createTrackbar("Hue Min", "Trackbars", 92,179,empty)

cv2.createTrackbar("Hue Max", "Trackbars", 113,179,empty)

cv2.createTrackbar("Sat Min", "Trackbars", 101,255,empty)


cv2.createTrackbar("Sat Max", "Trackbars", 255,255,empty)

cv2.createTrackbar("Val Min", "Trackbars", 6,255,empty)

cv2.createTrackbar("Val Max", "Trackbars", 255,255,empty)

while True:
    img=cv2.imread("Resources/stocky_thingy.jpg")
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max=cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min=cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max=cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min=cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max=cv2.getTrackbarPos("Val Max", "Trackbars")
    print(h_min, h_max,s_min,s_max,v_max,v_min)
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)

    imgResult=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("original",img)
    cv2.imshow("hsv",imgHSV)
    cv2.imshow("Result",imgResult)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break """


""" 
###Edge detection uses shapes and finds contours and such
img=cv2.imread("Resources/shapes.jpg")

#angels=["dot","line","Tri","Square","5","Hex","7","8","9","10","11","12","13","14","15","16"]


def getContours(img):

    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
    
        # cv2.drawContours(imgContor,cnt,-1,(255,0,0),3)
        peri =cv2.arcLength(cnt,True)
        approx=cv2.approxPolyDP(cnt,0.02*peri,True)
        print(len(approx))
        objcor=len(approx)
        x,y,w,h=cv2.boundingRect(approx)
        ObjectType="None"
       # for i in range(len(angels)):
        if objcor==3:ObjectType="Tri"
        elif objcor==4:
            aspRatio=w/float(h)
            if aspRatio>0.95 and aspRatio<1.05:ObjectType="Square"
            else:ObjectType="Rectangle"
        elif objcor>4:ObjectType="Circle"
    
        cv2.rectangle(imgContor,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.putText(imgContor,ObjectType,(x+(int(w/2))-10,y+(int(h/2))-10), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
        #cv2.drawContours(imgContor,cnt,-1,(255,0,0),3)


imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgContor=img.copy()
imgBlur=cv2.GaussianBlur(imgGray, (7,7),1.2)
imgCanny=cv2.Canny(imgBlur, 50,50,2)
getContours(imgCanny)
cv2.imshow("test",imgContor)
cv2.waitKey(0)

 """

""" 
 ###Facial recognition
import os
path=os.getcwd()
faceCascade=cv2.CascadeClassifier("Resources\haarcascade_frontalface_default.xml")
img=cv2.imread('Resources/Gruppebilde_1.jpg')

imgResize=cv2.resize(img,(300,200))
imgGray=cv2.cvtColor(imgResize,cv2.COLOR_BGR2GRAY)
faces=faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(imgResize,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("test",imgResize)
cv2.waitKey(0)
 """


""" 
###own facial recognition
faceCascade=cv2.CascadeClassifier("Resources\haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
###3 =width
cap.set(3,640)
####4=height
cap.set(4,480)
####10=brightness
cap.set(10,100)
i=0
while True:
    success, img= cap.read()
    ##show img
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(imgGray,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)



    cv2.imshow("Video",img)
    ###add press q to break loop
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break


 """
