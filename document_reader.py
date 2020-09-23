import cv2
import numpy as np

widthImg,heightImg=480,640
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
kernel=np.ones((5,5))

blankimg=img = np.zeros((widthImg,heightImg,3),np.uint8)

def preProcessing(img):
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur=cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny=cv2.Canny(imgBlur,150,150)
    imgDial=cv2.dilate(imgCanny,kernel=kernel,iterations=2)
    imgThres=cv2.erode(imgDial,kernel=kernel, iterations=1)
    return imgThres

def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    biggest=np.array([])
    maxArea=0
    for cnt in contours:
    
        area=cv2.contourArea(cnt)
        if area>5000:
            cv2.drawContours(imgCount,cnt,-1,(255,0,0),3)
            peri =cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            if area>maxArea and len(approx)==4:
                biggest =approx
                maxArea=area
    return biggest


def reorder(myPoints):
    myPoints=myPoints.reshape((4,2))
    myPointsNew=np.zeros((4,1,2),np.int32)
    add=myPoints.sum(1)
    myPointsNew[0]=myPoints[np.argmin(add)]
    myPointsNew[3]=myPoints[np.argmax(add)]
    diff=np.diff(myPoints, axis=1)
    myPointsNew[1]=myPoints[np.argmin(diff)]
    myPointsNew[2]=myPoints[np.argmax(diff)]
    return myPointsNew
    



def getWarp(img, biggest):
    biggest=reorder(biggest)
    pts1=np.float32(biggest)
    pts2=np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
    matrix=cv2.getPerspectiveTransform(pts1,pts2)
    imgOut=cv2.warpPerspective(img,matrix,(widthImg,heightImg))
    imgCropped=imgOut[20:imgOut.shape[0]-20,20:imgOut.shape[1]-20]
    imgCropped=cv2.resize(imgCropped,(widthImg,heightImg))
    return imgCropped



widthImg,heightImg=480,640
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
kernel=np.ones((5,5))

blankimg=img = np.zeros((widthImg,heightImg,3),np.uint8)

while True:
    success, img= cap.read()
    cv2.resize(img,(widthImg,heightImg))
    imgCount=img.copy()
    imgThres=preProcessing(img)
    biggest=getContours(imgThres)
    if len(biggest)>1:
        imgWarped=getWarp(img, biggest)
        cv2.imshow("WarpedImg",imgWarped)
        blankimg=imgWarped.copy()
    else:
        cv2.imshow("WarpedImg",blankimg)

    cv2.imshow("OGimage",img)
    cv2.imshow("thresh",imgThres)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break


   

""" 
img=cv2.imread("Resources\external-content.duckduckgo.com.jpg")

widthImg,heightImg=480,640

kernel=np.ones((5,5))
cv2.resize(img,(widthImg,heightImg))
imgCount=img.copy()
imgThres=preProcessing(img)
biggest=getContours(imgThres)
if len(biggest)>1:
    imgWarped=getWarp(img, biggest)
    cv2.imshow("WarpedImg",imgWarped)
    blankimg=imgWarped.copy()
else:
    cv2.imshow("WarpedImg",blankimg)

cv2.imshow("OGimage",imgCount)
cv2.imshow("thresh",imgThres)
cv2.waitKey(0) """