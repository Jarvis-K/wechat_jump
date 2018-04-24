def findPoint(pointSet):
    left = 100000
    right = 0
    top  = 100000
    bottom = 0
    lefty = 100000
    righty = 0
    bottomx = 100000
    topx = 0
    leftP = []
    rightP = []
    topP = []
    bottomP = []
    for point in pointSet:
        if point[0] < left:
            left = point[0]
        elif point[0] > right:
            right = point[0]
        if point[1] < top:
            top = point[1]
        elif point[1] >= bottom:
            bottom = point[1]
    for point in pointSet:
        if point[0] == left and point[1] < lefty:
            lefty = point[1]
        if point[0] == right and point[1] > righty:
            righty = point[1]
        if point[1] == bottom and point[0] < bottomx:
            bottomx = point[0]
        if point[1] == top and point[0] > topx:
            topx = point[0]
    # 返回左，右，上，下的坐标
    return left, lefty, right, righty, bottom, bottomx, top, topx
    # print(left, lefty, right, righty, bottom, bottomx, top, topx)


# testList = []
# for i in range(10):
#     for j in range(10):
#         if i == 0 or i == 9 or j == 0 or j == 9:
#             testList.append([i, j])
#
# testList.append([11, 11])
# testList.append([12, 9])
# a1, a2, a3, a4, a5, a6, a7, a8 = findPoint(testList)
# print(a1, a2, a3, a4, a5, a6, a7, a8)
