"""
@author: Rivers Jiang
"""

"""
Description

Goal:
Learn to draw different geometric shapes with OpenCV
You will learn these functions: 
cv.line(), 
cv.circle(), 
cv.rectangle(), 
cv.ellipse(), 
cv.putText() etc.

Code:
In all the above functions, you will see some common arguments as given below:
img: The image where you want to draw the shapes
color: Color of the shape. for BGR, pass it as a tuple, eg: (255,0,0) for blue. For grayscale, just pass the scalar value.
thickness: Thickness of the line or circle etc. 
            If **-1** is passed for closed figures like circles, it will fill the shape. default thickness = 1
lineType: Type of line, whether 8-connected, anti-aliased line etc. 
           By default, it is 8-connected. cv.LINE_AA gives anti-aliased line which looks great for curves.
"""

"""
Drawing Line
"""
import numpy as np
import cv2