"""
author: Jiang Rivers

Draw stuffs with your mouse
"""
# Mouse event can be anything related to mouse like left-button down, left-button up, left-button double-click etc.
# It gives us the coordinates (x,y) for every mouse event. With this event and location, we can do whatever we like.
# To list all available events available, run the following code in Python terminal:
#import cv2 as cv
#events=[i for i in dir(cv) if 'EVENT' in i]
#print(events)


# Creating mouse callback function has a specific format which is same everywhere.
# It differs only in what the function does.
# So our mouse callback function does one thing, it draws a circle where we double-click.
# So see the code below. Code is self-explanatory from comments :
import numpy as np
import cv2
# mouse callback function
def draw_circle(event,x,y,flags,param):
    # MouseEventFlags ：
        #   cv.EVENT_FLAG_LBUTTON = 1, 左键拖拽
        #   cv.EVENT_FLAG_RBUTTON = 2, 右键拖拽
        #   cv.EVENT_FLAG_MBUTTON = 4, 中键不放
        #   cv.EVENT_FLAG_CTRLKEY = 8,按住ctrl不放
        #   cv.EVENT_FLAG_SHIFTKEY = 16, 按住shift不放
        #   cv.EVENT_FLAG_ALTKEY = 32 ,按住alt不放

    #  cv.MouseEventTypes ：
        #   cv.EVENT_MOUSEMOVE = 0, 鼠标移动
        #   cv.EVENT_LBUTTONDOWN = 1, 左键按下
        #   cv.EVENT_RBUTTONDOWN = 2, 右键按下
        #   cv.EVENT_MBUTTONDOWN = 3, 中键按下
        #   cv.EVENT_LBUTTONUP = 4, 左键释放
        #   cv.EVENT_RBUTTONUP = 5, 右键释放
        #   cv.EVENT_MBUTTONUP = 6, 中键释放
        #   cv.EVENT_LBUTTONDBLCLK = 7, 左键双击
        #   cv.EVENT_RBUTTONDBLCLK = 8, 右键双击
        #   cv.EVENT_MBUTTONDBLCLK = 9, 中健双击
        #   cv.EVENT_MOUSEWHEEL = 10, 滚轮滑动
        #   cv.EVENT_MOUSEHWHEEL = 11 横向滚轮滑动
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)

# Create a black iamge, a window and bind the function to window
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF ==ord('q'):
        break
cv2.destroyAllWindows()