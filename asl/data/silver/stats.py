#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

with open('gloss_raw.txt', 'r', encoding='utf8') as silver:
    pronforms = []
    for line in silver:
        a = re.findall(r'X-\S+', line)
        for b in a:
            pronforms.append(str(b))
    print(set(pronforms))
