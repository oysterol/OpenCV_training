import cv2
import numpy as np
import csv

def empty():
    pass


def select_colors():
    
    cap=cv2.VideoCapture(0)
    cap.set(3,640)

    cap.set(4,480)
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars",640,240)
    cv2.createTrackbar("Hue Min", "Trackbars", 0,179,empty)

    cv2.createTrackbar("Hue Max", "Trackbars", 179,179,empty)

    cv2.createTrackbar("Sat Min", "Trackbars", 0,255,empty)


    cv2.createTrackbar("Sat Max", "Trackbars", 255,255,empty)

    cv2.createTrackbar("Val Min", "Trackbars", 0,255,empty)

    cv2.createTrackbar("Val Max", "Trackbars", 255,255,empty)


    while True:
        success,img= cap.read()
        cv2.imshow("Video",img)
        ###add press q to break loop
        imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        h_min=cv2.getTrackbarPos("Hue Min", "Trackbars")
        h_max=cv2.getTrackbarPos("Hue Max", "Trackbars")
        s_min=cv2.getTrackbarPos("Sat Min", "Trackbars")
        s_max=cv2.getTrackbarPos("Sat Max", "Trackbars")
        v_min=cv2.getTrackbarPos("Val Min", "Trackbars")
        v_max=cv2.getTrackbarPos("Val Max", "Trackbars")
       # print(h_min, h_max,s_min,s_max,v_max,v_min)
        lower=np.array([h_min,s_min,v_min])
        upper=np.array([h_max,s_max,v_max])
        mask=cv2.inRange(imgHSV,lower,upper)

        imgResult=cv2.bitwise_and(img,img,mask=mask)
        #cv2.imshow("original",img)
        #cv2.imshow("hsv",imgHSV)
        cv2.imshow("mask",mask)
        #cv2.imshow("Result",imgResult)

        if cv2.waitKey(1) & 0xFF ==ord('q'):
            fields=['color','h_min','s_min','v_min','h_max','s_max','v_max']
            with open('colors.csv','a') as csvfile:
                color=input("Color if none press q: ")
                writer=csv.writer(csvfile)
                if color=='q':
                    break
                else:
                    writer.writerow([color,lower[0],lower[1],lower[2],upper[0],upper[1],upper[2]])

                break


def color_reader(colors):
    uppers=[]
    lowers=[]
    with open('colors.csv','r') as csvfile:
            values=csv.reader(csvfile, delimiter=',')
            for value in values:
                if len(value)>1:
                    if value[0] in colors:
                        for k in range(0,3):
                            uppers.append(int(value[4+k]))
                            lowers.append(int(value[1+k]))
    return lowers, uppers

#select_colors()