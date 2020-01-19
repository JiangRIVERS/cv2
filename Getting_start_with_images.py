import cv2

image = cv2.imread('/Users/jiangmingda/Desktop/thor.jpg',0)#可选参数-1，0，1表示读取不同的图像，例如0表示灰度图
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',image)
cv2.waitKey(0)#按下任意键继续执行，括号内可指定image显示秒数以及按特定键位继续执行
cv2.destroyAllWindows()