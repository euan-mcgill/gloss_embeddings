#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys

'''
As is described in Moryossef et al. (2021), 'drop the remaining tokens
with a probability of p=0.2 and randomly reorder tokens with a maximum
distance d=4'
'''

#text = "KARL MARX MATAR A PAPÁ PROPIO INDX.PRO:1SG"

#gl_cont = [gl for gl in text.split()]

def permutation(lst, group_size):
    for i in range(0, len(lst), group_size):
        group = lst[i:i + group_size]
        random.shuffle(group)
        lst[i:i + group_size] = group
    #print(lst)
    return lst

#permutation(gl_cont, 4)

def write_to_file():
    with open(sys.argv[1], 'r', encoding='utf8') as gl, \
         open(sys.argv[2], 'w', encoding='utf8') as out:
         for line in gl:
            perline = permutation(line.split(), 4)
            out.write(' '.join(perline)+'\n')