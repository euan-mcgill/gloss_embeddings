#!/usr/bin/env python3
# -*- coding: utf-8 -*-

counter = 0
with open('all_nl.txt', 'r', encoding='utf-8') as nl, \
     open('nlngt_train_nl.txt', 'w', encoding='utf-8') as nl_train, \
     open('nlngt_dev_nl.txt', 'w', encoding='utf-8') as nl_dev, \
     open('nlngt_test_nl.txt', 'w', encoding='utf-8') as nl_test:
        for line in nl:
            counter += 1
            if counter <= 11875:
                nl_train.write(line)
            elif counter >11875 and counter <= 13359:
                nl_dev.write(line)
            elif counter > 13359 and counter <= 14843:
                nl_test.write(line)
            else:
                print("line out of range")

counter = 0
with open('all_gloss.txt', 'r', encoding='utf-8') as ngt, \
     open('nlngt_train_gloss.txt', 'w', encoding='utf-8') as ngt_train, \
     open('nlngt_dev_gloss.txt', 'w', encoding='utf-8') as ngt_dev, \
     open('nlngt_test_gloss.txt', 'w', encoding='utf-8') as ngt_test:
        for line in ngt:
            counter += 1
            if counter <= 11875:
                ngt_train.write(line)
            elif counter >11875 and counter <= 13359:
                ngt_dev.write(line)
            elif counter > 13359 and counter <= 14843:
                ngt_test.write(line)
            else:
                print("line out of range")
