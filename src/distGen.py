import os
import numpy as np
from numpy import random

ref_len = 110579
step = 100
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# labels = ['a', 'b']


def read_cnv(path):
    abspath = os.path.abspath(path)
    file = open(abspath, 'r')
    next(file) #skip first line
    arr = []
    for line in file:
        tmp = line.split()
        tmp = [int(tmp[1]), int(tmp[2]), tmp[8]]
        arr.append(tmp)
    return arr


def get_score(X):
    score = []
    j = 0
    for i in range(0, ref_len, step):
        while j < len(X) and X[j][1] < i:
            j = j + 1

        if len(X) <= j:
            score.append('neutral')
        elif i < X[j][0]:
            score.append('neutral')
        elif X[j][0] <= i and i <= X[j][1]:
            score.append(X[j][2])
            j = j + 1
    return score

def delta(x, y):
    if x == 'neutral' and y == 'neutral':
        return 0
    elif x == 'neutral' and y == 'amp':
        return 1
    elif x == 'neutral' and y == 'del':
        return 1
    elif x == 'amp' and y == 'neutral':
        return 1
    elif x == 'amp' and y == 'amp':
        return -2
    elif x == 'amp' and y == 'del':
        return 2
    elif x == 'del' and y == 'neutral':
        return 1
    elif x == 'del' and y == 'amp':
        return 2
    elif x == 'del' and y == 'del':
        return -2

def calc_dist(X, Y):
    dist = 0
    for i in range(len(X)):
        dist = dist + delta(X[i], Y[i])
    return dist

def dist_mat():
    dict = {}
    for x in labels:
        tmp = read_cnv('data\\%s_cnv.output' % (x))
        dict[x] = get_score(tmp)
    
    d = len(labels)
    mat = np.zeros((d,d))
    for i in range(d):
        for j in range(i+1, d):
            mat[i][j] = calc_dist(dict[labels[i]], dict[labels[j]])
    return mat

print(dist_mat())