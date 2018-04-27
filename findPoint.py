#coding:utf-8
import cv2
import pylab as pl
img_rgb=cv2.imread("9.png",0)
img0=img_rgb
img_rgb = cv2.GaussianBlur(img_rgb, (3, 3), 0)
canny_img = cv2.Canny(img_rgb,100, 210)
img = canny_img
img_rgb=img

# gray_lap = cv2.Laplacian(img_rgb,cv2.CV_32F,ksize = 3)  
# img_rgb = cv2.convertScaleAbs(gray_lap)  
img_rgb = cv2.GaussianBlur(img_rgb, (5, 5), 0)
canny_img = cv2.Canny(img_rgb,100, 410)

_=pl.imshow(canny_img,cmap=pl.gray())
pl.show()


gray=img_rgb
ret, binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY)   
_,contours0, hierarchy = cv2.findContours(binary, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  
size_rectangle_max = 0; 
maxi=0
for i in range(len(contours0)):
    #aproximate countours to polygons
    approximation = cv2.approxPolyDP(contours0[i], 20, True)
        
    #has the polygon 4 sides?
    # if(not (len (approximation)==4)):
    #     continue;
    #is the polygon convex ?
    # if(not cv2.isContourConvex(approximation) ):
    #     continue; 
    #area of the polygon
    size_rectangle = cv2.contourArea(approximation)
    #store the biggest
    if size_rectangle> size_rectangle_max:
        size_rectangle_max = size_rectangle 
        big_rectangle = approximation
        maxi=i

cv2.drawContours(img0,contours0,maxi,(255,255,255),10)  
_=pl.imshow(img0,cmap=pl.gray())
pl.show()