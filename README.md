# play.py逻辑
第一次跳跃的距离是固定的，所以我们可以通过这来调节系数。

## 载入
载入相机拍摄的图片以及模版（都为灰度图
## 获取屏幕
1. 先进行高斯模糊（降低噪声），
2. 然后canny边缘检测，
3. 再进行一次高斯模糊（将断开的线连到一起），
4. 使用findContours找到轮廓，
5. 把其中形成的多边形面积最大的轮廓作为手机屏幕轮廓，
6. 再通过寻找轮廓点的左上，左下，左下，右下四个点，找到矩形端点，
7. 通过透视变换转成一个750x1334分辨率的屏幕

原图
<img src="https://github.com/Jarvis-K/wechat_jump/blob/master/10.png" width = 50% height=50% alt="原图" align=center />

处理后
<img src="https://github.com/Jarvis-K/wechat_jump/blob/master/canny.png" width = 50% height=50% alt="canny" align=center />

## 识别棋子
通过屏幕的灰度图，直接进行模版匹配即可
## 获取目标点
1. 先通过模版匹配小白点，有的话，则认为是目标点，
2. 先删除棋子的边缘值，然后通过寻找400以后的第一个非0像素点p，其所在行非0点的行号取均值即为center\_x，y\_top=p.y，从p往下，直至遇到一个另一个非0点，认为其是y\_bottom，因而center\_y= (y\_top+y\_bottom)/2

结果
<img src="https://github.com/Jarvis-K/wechat_jump/blob/master/last.png" width = 50% height=50% alt="canny" align=center />
## 计算目标时间
直接计算欧式距离，再乘以一与手机相关的参数，即可得到时间

## 机械臂点触
WAITING IN QUEUE


# Todo
## queue
1. 测试跳跃参数
2. 连上机械臂

## bug may exist
1. 手机边缘反光，预处理如果无法消除，则可能导致找不到屏幕的四个端点（findpoint可能需要做修改）
2. 如果检测失败，或者识别不成功，应该重新读取新的图片



