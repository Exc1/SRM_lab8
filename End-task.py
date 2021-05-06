import numpy as np
import matplotlib.pyplot as plt

mat2 = [[-2.04, 1.1, ((0.04/0.3)-0.04)-0.9],
        [0.9, -2.04, 1.1, (0.04/0.5)-0.04],
        [0.9, -2.04, 1.1, (0.04/0.7)-0.04],
        [0.9, -2.04, 1.1, (0.04/0.9)-0.04],
        [13, -16.1, (0.04/1.1)-0.04]]


def create_coef(mat):
    list = [[], []]
    list[0].append(-mat[0][1] / mat[0][0])
    list[1].append(mat[0][2] / mat[0][0])
    for i in range(1, len(mat)):
        if i == len(mat) - 1:
            list[0].append(0)
            list[1].append((mat[i][2] - (mat[i][0] * list[1][i - 1])) / (mat[i][1] + mat[i][0] * list[0][i - 1]))
            break
        list[0].append(-mat[i][2] / (mat[i][1] + mat[i][0] * list[0][i - 1]))
        list[1].append((mat[i][3] - (mat[i][0] * list[1][i - 1])) / (mat[i][1] + (mat[i][0] * list[0][i - 1])))
    return list


def get_x(list):
    res = []
    for i in range(len(list[0]) - 1, 0, -1):
        if i == len(list[0]) - 1:
            res.append(list[1][len(list[1]) - 1])
        res.append(list[0][i] * res[len(list[1]) - 1 - i] + list[1][i])
    return res


print("Результат")
print(get_x(create_coef(mat2)))


