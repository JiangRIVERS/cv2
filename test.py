import cv2
cap=cv2.VideoCapture('/Users/jiangmingda/Desktop/【七代小丑-踩点-混剪-高燃】前方高能！欢乐与惊悚的踩点视觉盛宴！希斯莱杰诞辰40周年纪念。.flv')
fps = 23.975609756097562 #保存视频的帧率
size = (1920,1080) #保存视频的大小

videoWriter =cv2.VideoWriter('/Users/jiangmingda/Desktop/test1.mp4',cv2.VideoWriter_fourcc('X','V','I','D'),fps,size)

i=0
while True:
    success,frame = cap.read()
    if success:
        i += 1
        print('i = ',i)
        if(i<5030):
            videoWriter.write(frame)
        else:break
    else:
        print('end')
        break

