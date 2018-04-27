import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('7.png')
rows, cols = img.shape[:2]
# 原图中卡片的四个角点
pts1 = np.float32([[502, 325],[979, 309],  [520, 1229],[1030, 1219]])
# 变换后分别在左上、右上、左下、右下四个点
pts2 = np.float32([[0, 0], [480, 0], [0, 900], [480, 900]])
# 生成透视变换矩阵
M = cv2.getPerspectiveTransform(pts1, pts2)
# 进行透视变换
dst = cv2.warpPerspective(img, M, (480, 900))
plt.subplot(121), plt.imshow(img[:, :, ::-1]), plt.title('input')
plt.subplot(122), plt.imshow(dst[:, :, ::-1]), plt.title('output')
plt.show()