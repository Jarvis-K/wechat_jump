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
<img src="https://github.com/Jarvis-K/wechat_jump/blob/master/10.png?raw=true" width = 50% height=50% alt="origin" align=center />

处理后
<img src="https://github.com/Jarvis-K/wechat_jump/blob/master/canny.png?raw=true" width = 50% height=50% alt="canny" align=center />

## 识别棋子
通过屏幕的灰度图，直接进行模版匹配即可
## 获取目标点
1. 先通过模版匹配小白点，有的话，则认为是目标点，
2. 先删除棋子的边缘值，由于预处理过程并不能保证很理想，所以在这里我们自己想了个解决方案，我们从400（上面的数字部分跳过）开始，从上往下遍历，设置一个maxl（记录所遇到的行的最左最右点的最大间隔），如果连续三行都小于maxl，则认为maxl即我们需要找的物块行，再取平均，就得到了中心点位置。

结果
<img src="https://github.com/Jarvis-K/wechat_jump/blob/master/last.png?raw=true" width = 50% height=50% alt="result" align=center />

## 计算目标时间
直接计算欧式距离，再乘以一与手机相关的参数，即可得到时间

## 机械臂点触
根据按压时间，先伸出，再往下，再等待press_time，再归位。

# 结果展示



