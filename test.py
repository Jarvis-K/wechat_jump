# import cv2
# import numpy as np

# img = cv2.imread('last.png')
# cv2.imshow("img",img)
# # gray=img
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# # edges = cv2.Canny(gray,50,150,apertureSize = 3)
# edges=gray
# minLineLength = 100000000
# maxLineGap = 0.001
# lines = cv2.HoughLinesP(edges,0.1,np.pi/1,50,minLineLength,maxLineGap)
# cnt=0
# for line in lines:
#     for x1,y1,x2,y2 in line:
#         cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
#         cnt+=1
# print(cnt)

# cv2.imwrite('houghlines5.jpg',img)
import cv2  
  
img = cv2.imread('canny.png')  
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)   
  
# _,contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
_,contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)  
cv2.drawContours(img,contours,0,(255,255,255),10)  
  



pentagram = contours[0] 
leftmost = tuple(pentagram[:,0][pentagram[:,:,0].argmin()])  
rightmost = tuple(pentagram[:,0][pentagram[:,:,0].argmax()]) 
upmost = tuple(pentagram[:,0][pentagram[:,:,1].argmax()])  
downmost = tuple(pentagram[:,0][pentagram[:,:,1].argmin()]) 


print(pentagram[:,0][:,0])

print(leftmost) 
print(rightmost)
print(downmost)
print(upmost)

  
cv2.circle(img, leftmost, 2, (0,255,0),5)   
cv2.circle(img, rightmost, 2, (0,255,0),5)  
cv2.circle(img, upmost, 2, (0,255,0),5)  
cv2.circle(img, downmost, 2, (0,255,0),5)  
print(contours[0].shape)  

cv2.imwrite("point.png",img)
# cv2.imshow("img", img)  
# cv2.waitKey(0)  