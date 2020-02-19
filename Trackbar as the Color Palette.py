"""
author: Jiang Rivers

Create trackbar to control certain parameters
"""
'''
For cv.getTrackbarPos() function, first argument is the trackbar name, 
second one is the window name to which it is attached, 
third argument is the default value, 
fourth one is the maximum value and fifth one is the callback function which is executed everytime trackbar value changes. 
The callback function always has a default argument which is the trackbar position.
In our case, function does nothing, so we simply pass.
'''
import numpy as np
import cv2

def nothing(x):
    # function does nothing
    pass

# Create a black image, a window
img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')

# Create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# Create switch for ON/OFF functionality
switch='0:OFF \n 1: ON'
cv2.createTrackbar(switch,'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1) & 0xFF
    if k==ord('q'):
        break

    # get current positions of four trackbars
    r=cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s==0:
        img[:]=0
    else:
        img[:]=[b,g,r]
cv2.destroyAllWindows()