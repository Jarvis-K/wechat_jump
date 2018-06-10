# coding:utf-8
import os
import cv2
import numpy as np
import time
import pylab as pl
import random
import threading
import time
from DobotDemoForPython import DobotDllType as dType
from math import *


CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

#Load Dll
api = dType.load()


postion=[237.7514,49.2358,-25.7501, 7.1569]
def init():
    # dType.SetHOMEParams(api,postion[0],postion[1],postion[2],postion[3], isQueued=1)
    speed1=100
    speed = 500
    coordinate=4000
    dType.SetPTPJointParams(api, speed1,speed1,speed1,speed1,speed1,speed1,speed1,speed1, isQueued=1)
    # dType.SetPTPCommonParams(api, speed, speed, isQueued=1)
    dType.SetPTPCoordinateParams(api,coordinate,coordinate,coordinate,coordinate,isQueued=1)
    # Async Home
    # dType.SetHOMECmd(api, temp=0, isQueued=1)

def init1():
    speed1=100
    speed = 500
    coordinate=9000
    dType.SetPTPJointParams(api, speed1,speed1,speed1,speed1,speed1,speed1,speed1,speed1, isQueued=1)
    dType.SetPTPCoordinateParams(api,coordinate,coordinate,coordinate,coordinate,isQueued=1)

def work(press_time):
    print("worktime",press_time)
    print(type(press_time))
    dType.SetQueuedCmdClear(api)
    init()

    waitTime=press_time*0.001
    offset=0;offset1=0
    for i in range(0, 5):
        print(i)
        if i % 4 == 0:
            offset = 0;offset1=-70
        elif i % 4 == 1:
            offset = 0;offset1=0
        elif i % 4 == 2:
            offset = 20;offset1=0
        elif i % 4 == 3:
            offset = 0;offset1=0
        # time.sleep(2)

        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,postion[0]+offset1,postion[1],postion[2]-offset,postion[3])[0]  # 移动

        dType.SetWAITCmd(api, waitTime)
        dType.SetQueuedCmdStartExec(api)

def work1(press_time):
    i=0
    print("worktime",press_time)
    print(type(press_time))
    dType.SetQueuedCmdClear(api)
    if press_time<=450:
        init1()
    else:
        init()

    waitTime=press_time*0.001
    # waitTime=waitTime1
    offset=0
    for i in range(0, 2):
        print(i)
        if i % 2 == 0:
            offset=20
        elif i % 2 == 1:
            offset=0

        lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,postion[0],postion[1],postion[2]-offset,postion[3])[0]  # 移动

        dType.SetWAITCmd(api, waitTime)
        dType.SetQueuedCmdStartExec(api)
    while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
        dType.dSleep(0)

    dType.SetQueuedCmdStopExec(api)
    dType.SetQueuedCmdClear(api)


def moveForward():

    dType.SetQueuedCmdClear(api)
    init()

    offset=0;offset1=0
    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,postion[0],postion[1],postion[2],postion[3])[0]  # 移动


    dType.SetQueuedCmdStartExec(api)

    while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
        dType.dSleep(0)

    dType.SetQueuedCmdStopExec(api)
    dType.SetQueuedCmdClear(api)

def moveBack():

    dType.SetQueuedCmdClear(api)
    init()

    lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode,postion[0]-70,postion[1],postion[2],postion[3])[0]  # 移动

    dType.SetQueuedCmdStartExec(api)

    while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
        dType.dSleep(0)


    #Stop to Execute Command Queued
    dType.SetQueuedCmdStopExec(api)
    dType.SetQueuedCmdClear(api)



def jump(distance):
    # 这个参数还需要针对屏幕分辨率进行优化
    coffine=1.19
    press_time = int(distance * coffine)
    print(distance)

    # 生成随机手机屏幕模拟触摸点
    # 模拟触摸点如果每次都是同一位置，成绩上传可能无法通过验证
    rand = random.randint(0, 9) * 10
    cmd = ('adb shell input swipe %i %i %i %i ' + str(press_time)) \
          % (320 + rand, 410 + rand, 320 + rand, 410 + rand)
    os.system(cmd)
    print(cmd)
    print("press_time: ",press_time)
    return press_time
    # os.remove("last.png")


def get_center(img_canny, ):
    # 利用边缘检测的结果寻找物块的上沿和下沿
    # 进而计算物块的中心点

    startY=520
    linewith1=np.nonzero([max(row) for row in img_canny[startY:]])
    y_center=0
    x_center=0
    maxl=0
    cnt=0
    cnt0=0
    l=0; r = 0
    maxl1=0
    flag=False
    for i in range(len(linewith1[0])):
        # print(i)
        y0_temp = linewith1[0][i] + startY
        x0_list = np.nonzero(canny_img[y0_temp])[0]
        if x0_list[-1]-x0_list[0]<20:
            continue
        if flag  and x0_list[-1]-x0_list[0]-maxl>150:

            print("-1   len(x0_list[0]) :", len(x0_list), "x0_list: ", x0_list)
           
            cnt0+=1

            if cnt0>20 :
                cnt=0
                maxl=x0_list[-1]-x0_list[0]
                x_center = int((x0_list[-1] + x0_list[0]) / 2)
                y_center = y0_temp
            continue
        if  x0_list[-1]-x0_list[0]>maxl :
            print("0  len(x0_list[0]) :",len(x0_list),"x0_list: ",x0_list)
            cnt=0
            flag=True
            cnt0=0
            maxl=x0_list[-1]-x0_list[0]
            l=x0_list[0];r=x0_list[-1]
            x_center=int((x0_list[-1]+x0_list[0])/2)
            y_center=y0_temp
        if x0_list[-1]-x0_list[0]<=maxl and maxl>50 :
            print("1  len(x0_list[0]) :", len(x0_list), "x0_list: ", x0_list)
            # break
            cnt0=0
            cnt+=1
            if cnt>3:
                break
    print("l is ",l,'\t','r is' , r , '\t','x_c is ',x_center)
    print("x_center,y_center: ",x_center,y_center)
    return img_canny,x_center,y_center

def find4point(points):
    lt = None
    rt = None
    lb = None
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
    # img_rgb = cv2.GaussianBlur(img_rgb, (11,11), 0)

    img_rgb = cv2.bilateralFilter(img_rgb,7, 80, 80)

    # img_rgb = cv2.medianBlur(img_rgb, 7)
    # cv2.imwrite("a11.png",img_rgb)
    # img_rgb =cv2.GaussianBlur(img_rgb, (9,9), 0)
    canny_img = cv2.Canny(img_rgb, 10, 28)
    # canny_img = cv2.GaussianBlur(canny_img, (11,11), 0)
    img_rgb=canny_img
    # gray_lap = cv2.Laplacian(img_rgb,cv2.CV_32F,ksize = 3)
    # img_rgb = cv2.convertScaleAbs(gray_lap)
    img_rgb = cv2.GaussianBlur(img_rgb, (9,13), 0)
    # cv2.imwrite("ccc.png",img_rgb)
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
    cv2.drawContours(canny_img,contours0,maxi,(0,0,0),40)
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
    lu,ld,ru,rd=find4point(box)
    print(lu,ru,ld,rd)
    #warp
    # 原图中卡片的四个角点


    pts1 = np.float32([lu,ru, ld, rd])

    # 变换后分别在左上、右上、左下、右下四个点
    pts2 = np.float32([[0, 0], [1080, 0], [0, 1920], [1080, 1920]])
    # 生成透视变换矩阵
    M = cv2.getPerspectiveTransform(pts1, pts2)
    # 进行透视变换
    dst = cv2.warpPerspective(canny_img, M, (1080, 1920))
    dst0 = cv2.warpPerspective(img0, M, (1080,1920))
    # plt.subplot(121), plt.imshow(img[:, :, ::-1]), plt.title('input')
    # plt.subplot(122), plt.imshow(dst[:, :, ::-1]), plt.title('output')
    # plt.show()
    return dst0,dst


class wechatJump(QtCore.QObject):
    """wechatJump Logic and Motion Part"""
    runSig = QtCore.pyqtSignal()
    runFlag= True
    def runSigCall(self):
        """accept signal from AllForOne to stop jump"""
        self.runFlag = False
    def main(self,w_length,h_length,sig):
        
        self.runFlag=True
        self.runSig.connect(self.runSigCall)
        state = dType.ConnectDobot(api, "", 115200)[0]

        # 匹配小跳棋的模板
        temp1 = cv2.imread('temp_player.jpg', 0)
        w1, h1 = temp1.shape[::-1]
        # 匹配游戏结束画面的模板
        temp_end = cv2.imread('temp_end.jpg', 0)
        # 匹配中心小圆点的模板
        temp_white_circle = cv2.imread('temp_white_circle.jpg', 0)
        w2, h2 = temp_white_circle.shape[::-1]

        # 循环直到游戏失败结束
        for i in range(10000):
            # get_screenshot(0)
            if not self.runFlag:
                    break
            img_rgb = cv2.imread('phone.png', 0)
            img_rgb = np.transpose(img_rgb);
            img_rgb = cv2.flip(img_rgb, 0);
            # cv2.imwrite("imgs/"+str(i)+"_origin.png",img_rgb)
            # 如果在游戏截图中匹配到带"再玩一局"字样的模板，则循环中止
            res_end = cv2.matchTemplate(img_rgb, temp_end, cv2.TM_CCOEFF_NORMED)
            if cv2.minMaxLoc(res_end)[1] > 0.8:
                print('Game over!')
                break


            img_rgb, canny_img = getScreen(img_rgb)
            # cv2.imwrite("pre.png", img_rgb)
            cv2.imwrite("imgs/"+str(i)+"_pre.png",img_rgb)
            # 模板匹配截图中小跳棋的位置
            # canny_img=pre_process(canny_img)
            res1 = cv2.matchTemplate(img_rgb, temp1, cv2.TM_CCOEFF_NORMED)
            min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(res1)
            print(max_val1)
            if(max_val1<0.5):
                continue
            if state == dType.DobotConnect.DobotConnect_NoError:
                print("ccc")
                moveForward()
                print("ddd")

            left_top = max_loc1  # 左上角
            right_bottom = (left_top[0] + w1, left_top[1] + h1)  # 右下角

            center1_loc = (int((left_top[0] + right_bottom[0]) / 2), int((left_top[1] + right_bottom[1]) / 2) + int(h1 / 2))
            print(center1_loc)
            cv2.rectangle(img_rgb, left_top, right_bottom, 255, 2)

            # 先尝试匹配截图中的中心原点，
            # 如果匹配值没有达到0.95，则使用边缘检测匹配物块上沿

            res2 = cv2.matchTemplate(img_rgb, temp_white_circle, cv2.TM_CCOEFF_NORMED)
            min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(res2)
            if max_val2 > 0.91:
                print('found white circle!')
                x_center, y_center = max_loc2[0] + w2 // 2, max_loc2[1] + h2 // 2
            else:
                # 边缘检测
                H, W = canny_img.shape
                # cv2.imwrite("canny.png", canny_img)
                # 消去小跳棋轮廓对边缘检测结果的干扰
                for k in range(left_top[1], right_bottom[1]):
                    for b in range(left_top[0], right_bottom[0]):
                        canny_img[k][b] = 0
                img_rgb, x_center, y_center = get_center(canny_img)

            # 将图片输出以供调试
            img_rgb = cv2.circle(img_rgb, (x_center, y_center), 10, 255, -1)
            img_rgb = cv2.circle(img_rgb, center1_loc, 10, 255, -1)
            # cv2.rectangle(canny_img, max_loc1, center1_loc, 255, 2)
            cv2.imwrite('last.png', img_rgb)
            cv2.imwrite("imgs/"+str(i)+'_last.png',img_rgb)
            print("last write down")

            distance = (center1_loc[0] - x_center) ** 2 + (center1_loc[1] - y_center) ** 2
            distance = distance ** 0.5
            print("distance:", distance)
            press_time = jump(distance)
            sig.emit(press_time)
            # file.writelines(str(distance)+'\t'+str(press_time)+'\n')
            if state == dType.DobotConnect.DobotConnect_NoError:
                work1(press_time)
                time.sleep(1.7)
                moveBack()
                time1=0.2
                time.sleep(time1)
                divide = 500.0
                if press_time/divide<time1:
                    time.sleep(time1)
                else:
                    time.sleep(press_time / divide)
                    print(press_time/divide)

        # Disconnect Dobot
        dType.DisconnectDobot(api)
