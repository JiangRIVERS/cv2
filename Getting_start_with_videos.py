"""
@author: Jiang Rivers
"""

"""
Playing Video from file
"""
import cv2
cap=cv2.VideoCapture('./irving.mov')

while cap.isOpened():
    # Sometimes, cap may not have initialized the capture.
    # In that case, this code shows error. You can check whether it is initialized
    # or not by the method cap.isOpened().
    # If it is True, OK. Otherwise open it using cap.open().
    ret,frame=cap.read()
    #cap.read()returns a bool(True / False).
    # ret用于检测是否读取到了这帧的视频，frame返回检测到的这帧视频的三维矩阵BGR形式。

    if not ret:
        # if frame is read correctly ret is True.
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


"""
Saving a video
"""
import cv2
cap=cv2.VideoCapture('./irving.mov')
#Define the codec and create VideoWriter object
#This time we create a VideoWriter object. We should specify the output file name (eg: output.avi).
# Then we should specify the FourCC code (details in next paragraph).
# Then number of frames per second (fps) and frame size should be passed.
# And last one is isColor flag.
# If it is True, encoder expect color frame, otherwise it works with grayscale frame.

#FourCC is a 4-byte code used to specify the video codec.
# The list of available codes can be found in fourcc.org. It is platform dependent.
# Following codecs works fine for me.

#In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2.
# (XVID is more preferable. MJPG results in high size video. X264 gives very small size video)
#In Windows: DIVX (More to be tested and added)
#In OSX: MJPG (.mp4), DIVX (.avi), X264 (.mkv).
fourcc=cv2.VideoWriter_fourcc(*'DIVX')
out=cv2.VideoWriter('flip_irving.avi',fourcc,20,(640,480),True)


while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame=cv2.flip(frame,1)#图像反转。 1：水平   0：垂直   -1：水平垂直
    #write the flipped frame
    out.write(frame)

    cv2.imshow('flip_irving',frame)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
#Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
