#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Dataset splits for en/ASL

python asl_splits english_file asl_file

'''

import re

with open('gloss_raw.txt', 'r', encoding='utf8') as synth,\
     open('asl_silver.txt', 'w', encoding='utf8') as silver:
    # {'X-POSS', 'X-IRS', 'X-HE', 'X-I', 'X-OURS', 'X-SHE', 'X-S', 'X-WE', 'X-ITSELF', 'X-MY', 'X-MYSELF', 
    # 'X-IT', 'X-HIMSELF', 'X-YOU', 'X-YOURSELF', 'X-MUST', 'X-Y', 'X-ITS', 'X-MSELVES', 'X-HERSELF', 'X-OURSELVES'}
    for line in synth:
        desc = re.sub(r'DESC-', r'', line)
        me = re.sub(r'\bX-I\b', r'ix-1p', desc)
        my = re.sub(r'(\bX-MY\b|\bX-MYSELF\b)', r'poss-1p', me)
        you = re.sub(r'\bX-YOU\b', r'ix-2p', my)
        your = re.sub(r'\bYOURSELF\b', r'poss-2p', you)
        it = re.sub(r'(\bX-HE\b|\bX-SHE\b|\bX-IT\b)', r'ix-3p:j', your)
        its = re.sub(r'(\bX-POSS\b|\bX-S\b|\bX-ITSELF\b|\bX-ITS\b)', r'poss-3p:i', it)
        his = re.sub(r'(\bX-HIMSELF\b|\bX-HERSELF\b)', r'poss-3p:j', its)
        we = re.sub(r'\bX-WE\b', r'ix-1p-pl', his)
        our = re.sub(r'(\bX-OURSELVES\b|\bX-OURS\b)', r'ix-1p-pl', we)
        they = re.sub(r'\bX-Y\b', r'ix-3p-pl-arc', our)
        them = re.sub(r'\bX-MSELVES\b', r'ix-3p-pl-circle', they)
        punct = re.sub(r'( \.| \,| \?)', r'', them)
        silver.write(punct.lower())
