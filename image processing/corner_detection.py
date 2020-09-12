import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while 1:
    ret,img=cap.read()
    cv2.imshow('live',img)

# to downgrade the image
scale_percent1 = 60
scale_percent2 = 40
weidth = int(img.shape[1]*scale_percent1/100)
height= int(img.shape[0]*scale_percent2/100)
dim = (weidth,height)
img = cv2.resize(img , dim , interpolation = cv2.INTER_AREA)  #resizing the image

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray= np.float32(gray)
dst=cv2.cornerHarris(gray,4,5,0.04)
dst = cv2.dilate(dst,None)
img[dst>0.01*dst.max()] = [0,0,0]

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
