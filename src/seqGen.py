import os
from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

random.seed(10)

_prim_len = 100000
_padding = _prim_len/100
_mu = _prim_len/100
_sigma = _mu/2
_lambda = 1
_lambda_tree = 5


def get_prim_seq():
    str = 'A'*(_prim_len//4) + 'T'*(_prim_len//4) + \
        'G'*(_prim_len//4) + 'C'*(_prim_len//4)
    l = list(str)
    random.shuffle(l)
    str = ''.join(l)
    return str


def deletion(seq):
    # from where
    f = random.randint(_padding, len(seq)-_padding-_mu)
    # how much
    l = math.floor(random.normal(loc=_mu, scale=_sigma))
    while l <= 0 or f+l >= len(seq)-_padding:
        l = math.floor(random.normal(loc=_mu, scale=_sigma))
        # print('Inside deletion')
    str = seq[:f] + seq[f+l:]
    return str


def tendem_repeat(seq):
    # from where
    f = random.randint(_padding, len(seq)-_padding-_mu)
    # how much
    l = math.floor(random.normal(loc=_mu, scale=_sigma))
    while l <= 0 or f+l >= len(seq)-_padding:
        l = math.floor(random.normal(loc=_mu, scale=_sigma))
        # print('Inside tendem')
    # how many
    m = random.poisson(lam=_lambda) + 1

    # rep = '(' + seq[f:f+l] + ')'
    rep = seq[f:f+l]
    str = seq[:f+l] + rep*m + seq[f+l:]

    # seq = seq[:f] + '(' + seq[f:f+l] + ')' + seq[f+l:]
    # print('Bef tendem: %s'%(seq))
    # print('Aft tendem: %s'%(str))
    return str


def duplication(seq):
    # from where
    f = random.randint(_padding, len(seq)-_padding-_mu)
    # how much
    l = math.floor(random.normal(loc=_mu, scale=_sigma))
    while l <= 0 or f+l >= len(seq)-_padding:
        l = math.floor(random.normal(loc=_mu, scale=_sigma))
        # print('Inside duplication 1')
    # how many
    m = random.poisson(lam=_lambda) + 1
    # to where
    arr = []
    for i in range(m):
        pos = random.randint(0, len(seq))
        while pos >= f and pos < f+l:  # so that duplication is not placed within duplication
            pos = random.randint(0, len(seq))
            # print('Inside duplication 2')
        arr.append(pos)
    arr.sort()

    str = seq[:]
    # rep = '(' + seq[f:f+l] + ')'
    rep = seq[f:f+l]
    for i in range(len(arr)):
        str = str[:arr[i]+i*l] + rep + str[arr[i]+i*l:]

    # seq = seq[:f] + '(' + seq[f:f+l] + ')' + seq[f+l:]
    # print('Bef dup: %s'%(seq))
    # print('Aft dup: %s'%(str))
    return str


def mutation(seq):
    # print('mutation on %s' % (seq))
    new_seq = seq
    m = random.poisson(lam=_lambda_tree)
    arr = random.randint(1, 3, size=m)
    for a in arr:
        if a == 1:
            new_seq = deletion(new_seq)
        elif a == 2:
            new_seq = tendem_repeat(new_seq)
        else:
            new_seq = duplication(new_seq)
    return new_seq


all_nodes = {}


class treeNode:
    def __init__(self, seq, label):
        global all_nodes
        self.seq = seq
        self.label = label
        self.left = None
        self.right = None
        all_nodes[label] = seq

    def is_leaf(self):
        if self.left or self.right:
            return False
        return True

    def get_newic(self):
        if self.is_leaf():
            return self.label
        left_str = self.left.get_newic()
        right_str = self.right.get_newic()
        return '(' + left_str + ',' + right_str + ')'


seq = get_prim_seq()
N1 = treeNode(mutation(seq), 'abcdefghij')
N2 = treeNode(mutation(N1.seq), 'abcde')
N3 = treeNode(mutation(N2.seq), 'ab')
N4 = treeNode(mutation(N3.seq), 'a')
N5 = treeNode(mutation(N3.seq), 'b')
N6 = treeNode(mutation(N2.seq), 'cde')
N7 = treeNode(mutation(N6.seq), 'c')
N8 = treeNode(mutation(N6.seq), 'de')
N9 = treeNode(mutation(N8.seq), 'd')
N10 = treeNode(mutation(N8.seq), 'e')
N11 = treeNode(mutation(N1.seq), 'fghij')
N12 = treeNode(mutation(N11.seq), 'fg')
N13 = treeNode(mutation(N12.seq), 'f')
N14 = treeNode(mutation(N12.seq), 'g')
N15 = treeNode(mutation(N11.seq), 'hij')
N16 = treeNode(mutation(N15.seq), 'h')
N17 = treeNode(mutation(N15.seq), 'ij')
N18 = treeNode(mutation(N17.seq), 'i')
N19 = treeNode(mutation(N17.seq), 'j')


def write_to_fasta(label, seq):
    path = os.path.abspath('..\copyEvol\data\%s.txt' % (label))
    outfile = open(path, 'w')
    outfile.write('>' + label + '\n' + seq + '\n')
    outfile.close()


def write_to_newick(root):
    path = os.path.abspath('..\copyEvol\data\ref_tree.newick')
    outfile = open(path, 'w')
    outstr = root.get_newic()
    outstr = '[&R] ' + outstr + ';'
    outfile.write(outstr)
    outfile.close()


for label in all_nodes:
    write_to_fasta(label, all_nodes[label])

# write_to_fasta(get_prim_seq())
# write_to_newick(N1)
