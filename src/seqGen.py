from numpy import random
import numpy as np
import matplotlib.pyplot as plt
from numpy.random.mtrand import randint
import seaborn as sns
<<<<<<< HEAD
import math

_prim_len = 100
_padding = 10
_mew = 10
_sigma = 5
_lambda = 1
=======
import os
>>>>>>> acf38f6f6aa30b25b1f7018ea7f8f82651cd53be


class treeNode:
    def __init__(self, seq):
        self.seq = seq
        self.left = None
        self.right = None

    def is_leaf(self):
        if self.left or self.right:
            return False
        return True

    def get_newic(self):
        if self.is_leaf():
            return self.seq
        left_str = self.left.get_newic()
        right_str = self.right.get_newic()
        return '(' + left_str + ',' + right_str + ')'


N1 = treeNode('a')
N2 = treeNode('b')
N3 = treeNode('c')
N4 = treeNode('d')
N5 = treeNode('e')
N6 = treeNode('')
N7 = treeNode('')
N8 = treeNode('')
N9 = treeNode('')
N6.left = N4
N6.right = N5
N7.left = N3
N7.right = N6
N8.left = N2
N8.right = N7
N9.left = N1
N9.right = N8

print(N9.get_newic())


def get_prim_seq():
    str = 'A'*(_prim_len//4) + 'T'*(_prim_len//4) + 'G'*(_prim_len//4) + 'C'*(_prim_len//4)
    l = list(str)
    random.shuffle(l)
    str = ''.join(l)
    return str


def deletion(seq):
    # from where
    f = random.randint(_padding, len(seq)-_padding)
    # how much
    l = math.floor(random.normal(loc=_mew, scale=_sigma))
    while l <= 0 or f+l >= len(seq)-_padding:
        l = math.floor(random.normal(loc=_mew, scale=_sigma))
    str = seq[:f] + seq[f+l:]
    return str


def tendem_repeat(seq):
    # from where
    f = random.randint(_padding, len(seq)-_padding)
    # how much
    l = math.floor(random.normal(loc=_mew, scale=_sigma))
    while l <= 0 or f+l >= len(seq)-_padding:
        l = math.floor(random.normal(loc=_mew, scale=_sigma))
    # how many
    m = random.poisson(lam=_lambda) + 1
    rep = '(' + seq[f:f+l] + ')'
    str = seq[:f+l] + rep*m + seq[f+l:]

    # seq = seq[:f] + '(' + seq[f:f+l] + ')' + seq[f+l:]
    # print("Bef tendem: %s"%(seq))
    # print("Aft tendem: %s"%(str))
    return str


def duplication(seq):
    # from where
    f = random.randint(_padding, len(seq)-_padding)
    # how much
    l = math.floor(random.normal(loc=_mew, scale=_sigma))
    while l <= 0 or f+l >= len(seq)-_padding:
        l = math.floor(random.normal(loc=_mew, scale=_sigma))
    # how many
    m = random.poisson(lam=_lambda) + 1
    # to where
    arr = []
    for i in range(m):
        num = random.randint(_padding, len(seq)-_padding)
        while num >= f and num < f+l:
            num = random.randint(_padding, len(seq)-_padding)
        arr.append(num)
    arr.sort()

    str = seq[:]
    rep = '(' + seq[f:f+l] + ')'
    for i in range(len(arr)):
        str = str[:arr[i]+i*l] + rep + str[arr[i]+i*l:]

    # seq = seq[:f] + '(' + seq[f:f+l] + ')' + seq[f+l:]
    # print("Bef dup: %s"%(seq))
    # print("Aft dup: %s"%(str))
    return str


str = get_prim_seq()
print(str)

<<<<<<< HEAD
tendem_repeat(str)
duplication(str)
=======

def write_to_fasta(seq):
    path = os.path.abspath("../data/ref.txt")
    outfile = open(path, "w")
    outfile.write(">" + "primary_seq" + "\n" + seq + "\n")
    outfile.close()


def write_to_newick(root):
    path = os.path.abspath("../data/ref_tree.newick")
    outfile = open(path, "w")
    outstr = root.get_newic()
    outstr = "[&R] " + outstr + ";"
    outfile.write(outstr)
    outfile.close()


write_to_fasta(get_prim_seq())
write_to_newick(N9)
>>>>>>> acf38f6f6aa30b25b1f7018ea7f8f82651cd53be
