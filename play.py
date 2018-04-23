#coding:utf-8
import os
import cv2
import numpy as np
import time
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

def pre_process(img_rgb):
    img0=img_rgb
    img_rgb = cv2.GaussianBlur(img_rgb, (3, 3), 0)
    canny_img = cv2.Canny(img_rgb,100, 200)
    img = canny_img

    # get four point
    # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
    gray=img
    ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)   
      
    # _,contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
    _,contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)  
    cv2.drawContours(img,contours,0,(0,0,0),10)  
    pentagram = contours[0] 
    leftmost = tuple(pentagram[:,0][pentagram[:,:,0].argmin()])  
    rightmost = tuple(pentagram[:,0][pentagram[:,:,0].argmax()]) 
    upmost = tuple(pentagram[:,0][pentagram[:,:,1].argmax()])  
    downmost = tuple(pentagram[:,0][pentagram[:,:,1].argmin()]) 
    print(leftmost) 
    print(rightmost)
    print(downmost)
    print(upmost)

    #warp
    rows, cols = img.shape[:2]
    # 原图中卡片的四个角点
    # pts1 = np.float32([list(leftmost),list(downmost),list(upmost),list(rightmost)])
    pts1 = np.float32([[502, 325],[979, 309],  [520, 1229],[1030, 1219]])
    # 变换后分别在左上、右上、左下、右下四个点
    pts2 = np.float32([[0, 0], [480, 0], [0, 900], [480, 900]])
    # 生成透视变换矩阵
    M = cv2.getPerspectiveTransform(pts1, pts2)
    # 进行透视变换
    dst = cv2.warpPerspective(img, M, (480, 900))
    dst0 = cv2.warpPerspective(img0, M, (480, 900))
    # plt.subplot(121), plt.imshow(img[:, :, ::-1]), plt.title('input')
    # plt.subplot(122), plt.imshow(dst[:, :, ::-1]), plt.title('output')
    # plt.show()
    return dst0,dst


# 第一次跳跃的距离是固定的
jump(530)
time.sleep(1)

# 匹配小跳棋的模板
temp1 = cv2.imread('tmp_player.png', 0)
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
    img_rgb = cv2.imread('6.png', 0)

    # 如果在游戏截图中匹配到带"再玩一局"字样的模板，则循环中止
    res_end = cv2.matchTemplate(img_rgb, temp_end, cv2.TM_CCOEFF_NORMED)
    if cv2.minMaxLoc(res_end)[1] > 0.95:
        print('Game over!')
        break

    img_rgb,canny_img=pre_process(img_rgb)
    cv2.imshow("aaa",img_rgb)
    # 模板匹配截图中小跳棋的位置
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
        # img_rgb = cv2.GaussianBlur(img_rgb, (3, 3), 0)
        # cv2.imwrite('last.png', img_rgb)
        # canny_img = cv2.Canny(img_rgb,200, 500)
        # canny_img = cv2.Canny(img_rgb,100, 200)
        # img_rgb=cv2.floodFill(img_rgb, mask, (w-1,h-1), (255,255,255), (2,2,2),(3,3,3),8)
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