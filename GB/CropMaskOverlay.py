import numpy as np
from cv2 import cv2
import os.path
        
 
def CROPMASK(img,pts,clr) : 
    
    ##clr ranges from 1-255 1 being black and 255 being white for gray scale values
    
    ## (1) Crop the bounding rect
    rect = cv2.boundingRect(pts)
    x,y,w,h = rect
    croped = img[y:y+h, x:x+w].copy()

    ## (2) make mask
    pts = pts - pts.min(axis=0)

    mask = np.zeros(croped.shape[:2], np.uint8)
    cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)

    ## (3) do bit-op
    dst = cv2.bitwise_and(croped, croped, mask=mask)

    ## (4) add the white background
    bg = np.ones_like(croped, np.uint8)*clr
    cv2.bitwise_not(bg,bg, mask=mask)
    dst2 = bg+ dst
    
    return  dst2