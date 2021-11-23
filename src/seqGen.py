from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


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
    str = 'A'*25000 + 'T'*25000 + 'G'*25000 + 'C'*25000
    l = list(str)
    random.shuffle(l)
    str = ''.join(l)
    return str


def deletion(seq):
    pass

print(get_prim_seq())