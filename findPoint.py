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


# testList = []
# for i in range(10):
#     for j in range(10):
#         if i == 0 or i == 9 or j == 0 or j == 9:
#             testList.append([i, j])
#
# # testList.append([11, 11])
# # testList.append([12, 9])
# #
# # a1, a2, a3, a4 = findPoint(testList)
# # print(a1, a2, a3, a4)