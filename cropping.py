import glob
import cv2
import numpy as np
cv_img = []

ix=729
iy=108
iw=126
ih=69

#give folder name of phots and format
for filename in glob.glob("40d8Dd/*.png"):
    print filename
    img = cv2.imread(filename)
    [y,x,a]=img.shape
    cropped = img[y-iy-ih:y-iy , ix:ix+iw]
    #cv2.imshow("cropped", cropped)
    filename ='o'+filename[0:]
    print filename
    cv2.imwrite(filename,cropped)
    print img.shape
    print cropped.shape
print "finish"
