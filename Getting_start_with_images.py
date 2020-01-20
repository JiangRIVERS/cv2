"""
@author: Rivers Jiang
"""

"""
读取图片并展示
"""
import cv2
image = cv2.imread('./thor.jpg',0)#可选参数-1，0，1表示读取不同的图像，例如0表示灰度图
cv2.namedWindow('image',cv2.WINDOW_NORMAL)#There is a special case where you can create an empty window and load an image to it later.
                                          # In that case, you can specify whether the window is resizable or not.
                                          # It is done with the function cv.namedWindow().
                                          # By default, the flag is cv.WINDOW_AUTOSIZE.
                                          # But if you specify the flag to be cv.WINDOW_NORMAL, you can resize window.
                                          # It will be helpful when an image is too large in dimension and when adding track bars to windows.
cv2.imshow('image',image)
cv2.waitKey(0) & 0xFF #按下任意键继续执行，括号内可指定image按特定键位继续执行
                      #If you are using a 64-bit machine, you will have to modify k = cv.waitKey(0) line as follows : k = cv.waitKey(0) & 0xFF
cv2.destroyAllWindows()#cv.destroyAllWindows() simply destroys all the windows we created.
                       # If you want to destroy any specific window, use the function cv.destroyWindow()
                       #where you pass the exact window name as the argument.

"""
写图片
"""
cv2.imwrite('imagename.png',saving_path)


"""
读取图片，按特定键位退出
"""
import cv2
img = cv2.imread('./thor.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF
if k==27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k==ord('s'): # wait for 's' key to save and exit
    cv2.destroyAllWindows()