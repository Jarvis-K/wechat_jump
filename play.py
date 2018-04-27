#coding:utf-8
import os
import cv2
import numpy as np
import time
import pylab as pl
import random


# 使用的Python库及对应版本：
# python 3.6
# opencv-python 3.3.0
# numpy 1.13.3
# 用到了opencv库中的模板匹配和边缘检测功能


# def get_screenshot(id):
#     os.system('adb shell screencap -p /sdcard/%s.png' % str(id))
#     os.system('adb pull /sdcard/%s.png .' % str(id))


def jump(distance):
    # 这个参数还需要针对屏幕分辨率进行优化
    press_time = int(distance * 1.35)

    # 生成随机手机屏幕模拟触摸点
    # 模拟触摸点如果每次都是同一位置，成绩上传可能无法通过验证
    rand = random.randint(0, 9) * 10
    cmd = ('adb shell input swipe %i %i %i %i ' + str(press_time)) \
          % (320 + rand, 410 + rand, 320 + rand, 410 + rand)
    os.system(cmd)
    print(cmd)
    # os.remove("last.png")

def findPoint(pointSet):
    leftx = 100000
    rightx = 0
    topy = 100000
    bottomy = 0
    lefty = 100000
    righty = 0
    bottomx = 100000
    topx = 0
    for point in pointSet:
        if point[0] < leftx:
            leftx = point[0]
        elif point[0] > rightx:
            rightx = point[0]
        if point[1] < topy:
            topy = point[1]
        elif point[1] > bottomy:
            bottomy = point[1]
    for point in pointSet:
        if point[0] == leftx and point[1] < lefty:
            lefty = point[1]
        if point[0] == rightx and point[1] > righty:
            righty = point[1]
        if point[1] == bottomy and point[0] < bottomx:
            bottomx = point[0]
        if point[1] == topy and point[0] > topx:
            topx = point[0]
    # 返回左，右，上，下的坐标
    return (leftx, lefty), (rightx, righty), (bottomx, bottomy), (topx, topy)
    # print(left, lefty, right, righty, bottom, bottomx, top, topx)


def get_center(img_canny, ):
    # 利用边缘检测的结果寻找物块的上沿和下沿
    # 进而计算物块的中心点
    y_top = np.nonzero([max(row) for row in img_canny[400:]])[0][0] + 400
    print("y_top is ",y_top)
    x_top = int(np.mean(np.nonzero(canny_img[y_top])))

    y_bottom = y_top + 50
    for row in range(y_bottom, H):
        if canny_img[row, x_top] != 0:
            y_bottom = row
            break

    x_center, y_center = x_top, (y_top + y_bottom) // 2
    return img_canny, x_center, y_center

def find4point(points):
    lt = None
    rt = None
    lb= None
    rb = None

    # points = points[np.argsort(points[:][0])]
    points = points[points[:, 0].argsort()]

    print(points)
    if points[0][1] > points[1][1]:
        lt = points[1]
        lb = points[0]
    else:
        lt = points[0]
        lb = points[1]
    if points[2][1] > points[3][1]:
        rt = points[3]
        rb = points[2]
    else:
        rt = points[2]
        rb = points[3]
    return ((lt[0], lt[1]), (lb[0], lb[1]), (rt[0], rt[1]), (rb[0], rb[1]))

def getScreen(img_rgb):
    img0=img_rgb
    img_rgb = cv2.GaussianBlur(img_rgb, (3, 3), 0)
    canny_img = cv2.Canny(img_rgb,100, 210)
    img_rgb=canny_img
    # gray_lap = cv2.Laplacian(img_rgb,cv2.CV_32F,ksize = 3)  
    # img_rgb = cv2.convertScaleAbs(gray_lap)  
    img_rgb = cv2.GaussianBlur(img_rgb, (5, 5), 0)
    gray=img_rgb
    # img=gray
    ret, binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY)   
    _,contours0, hierarchy = cv2.findContours(binary, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  
    size_rectangle_max = 0; 
    maxi=0
    for i in range(len(contours0)):
        #aproximate countours to polygons
        approximation = cv2.approxPolyDP(contours0[i], 20, True)
        size_rectangle = cv2.contourArea(approximation)
        #store the biggest
        if size_rectangle> size_rectangle_max:
            size_rectangle_max = size_rectangle 
            big_rectangle = approximation
            maxi=i
    cv2.drawContours(canny_img,contours0,maxi,(0,0,0),20)  
    # for con in contours0[maxi][:,0]:
    #     cv2.circle(img0,tuple(con),10,255,-1)
    # _=pl.imshow(img0)
    # pl.show()

    pentagram = contours0[maxi]
    cnt=pentagram
    rect = cv2.minAreaRect(cnt)  # 最小外接矩形
    box = np.int0(cv2.boxPoints(rect))  # 矩形的四个角点取整
    print(box)
    cv2.drawContours((img0), [box], 0, (255, 0, 0), 2)
    _=pl.imshow(img0)
    pl.show()

    # print(type(pentagram[:,0]) 
    # print(type(big_rectangle))
    lu,ld,ru,rd=find4point(box)
    # lu=(box[0][0],box[0][1])
    # ld=(box[1][0],box[1][1])
    # rd=(box[2][0],box[2][1])
    # ru=(box[3][0],box[3][1])
    # lu,rd,ld,ru=findPoint(pentagram[:,0])
    print(lu,ru,ld,rd)
    #warp
    # 原图中卡片的四个角点
    pts1 = np.float32([lu,ru, ld, rd])
    # 变换后分别在左上、右上、左下、右下四个点
    pts2 = np.float32([[0, 0], [750, 0], [0, 1334], [750, 1334]])
    # 生成透视变换矩阵
    M = cv2.getPerspectiveTransform(pts1, pts2)
    # 进行透视变换
    dst = cv2.warpPerspective(canny_img, M, (750, 1334))
    dst0 = cv2.warpPerspective(img0, M, (750,1334))
    # plt.subplot(121), plt.imshow(img[:, :, ::-1]), plt.title('input')
    # plt.subplot(122), plt.imshow(dst[:, :, ::-1]), plt.title('output')
    # plt.show()
    return dst0,dst





# 第一次跳跃的距离是固定的
jump(530)
time.sleep(1)

# 匹配小跳棋的模板
temp1 = cv2.imread('temp_player3.png', 0)
# temp1 = cv2.imread('tmp_all.png', 0)
w1, h1 = temp1.shape[::-1]
# 匹配游戏结束画面的模板
temp_end = cv2.imread('temp_end.jpg', 0)
# 匹配中心小圆点的模板
temp_white_circle = cv2.imread('temp_white_circle.jpg', 0)
w2, h2 = temp_white_circle.shape[::-1]

# 循环直到游戏失败结束
for i in range(10000):
    # get_screenshot(0)
    img_rgb = cv2.imread('10.png', 0)
    # img_rgb=np.rot90(img_rgb)
    # 如果在游戏截图中匹配到带"再玩一局"字样的模板，则循环中止
    res_end = cv2.matchTemplate(img_rgb, temp_end, cv2.TM_CCOEFF_NORMED)
    if cv2.minMaxLoc(res_end)[1] > 0.95:
        print('Game over!')
        break

    img_rgb,canny_img=getScreen(img_rgb)
    cv2.imwrite("pre.png",img_rgb)
    # 模板匹配截图中小跳棋的位置
    # canny_img=pre_process(canny_img)
    res1 = cv2.matchTemplate(img_rgb, temp1, cv2.TM_CCOEFF_NORMED)
    min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(res1)
    

    left_top = max_loc1  # 左上角
    right_bottom = (left_top[0] + w1, left_top[1] + h1)  # 右下角

    center1_loc = (int((left_top[0] + right_bottom[0])/2) , int((left_top[1] + right_bottom[1])/2)+int(h1/2))
    print(center1_loc)
    cv2.rectangle(img_rgb, left_top, right_bottom, 255, 2)

    # 先尝试匹配截图中的中心原点，
    # 如果匹配值没有达到0.95，则使用边缘检测匹配物块上沿

    res2 = cv2.matchTemplate(img_rgb, temp_white_circle, cv2.TM_CCOEFF_NORMED)
    min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(res2)
    if max_val2 > 0.95:
        print('found white circle!')
        x_center, y_center = max_loc2[0] + w2 // 2, max_loc2[1] + h2 // 2
    else:
        # 边缘检测
        H, W = canny_img.shape
        cv2.imwrite("canny.png",canny_img)
        # 消去小跳棋轮廓对边缘检测结果的干扰
        for k in range(left_top[1] , right_bottom[1]):
            for b in range(left_top[0], right_bottom[0]):
                canny_img[k][b] = 0
        img_rgb, x_center, y_center = get_center(canny_img)

    # 将图片输出以供调试
    img_rgb = cv2.circle(img_rgb, (x_center, y_center), 10, 255, -1)
    img_rgb = cv2.circle(img_rgb, center1_loc, 10, 255, -1)
    # cv2.rectangle(canny_img, max_loc1, center1_loc, 255, 2)
    cv2.imwrite('last.png', img_rgb)

    distance = (center1_loc[0] - x_center) ** 2 + (center1_loc[1] - y_center) ** 2
    distance = distance ** 0.5
    jump(distance)
    time.sleep(1.3)