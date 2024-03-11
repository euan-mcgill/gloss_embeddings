#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Dataset splits for en/ASL

python asl_splits english_file asl_file

'''

with open('asl/data/parallel/asl.txt', 'r', encoding='utf8') as asl, \
     open('asl/data/parallel/asl_train.txt', 'w', encoding='utf8') as asl_tr, \
     open('asl/data/parallel/asl_dev.txt', 'w', encoding='utf8') as asl_dv, \
     open('asl/data/parallel/asl_test.txt', 'w', encoding='utf8') as asl_tt:
    counter = 0
    for line in asl:
        if counter < 103                      or counter >= 173 and counter < 372 or\
             counter >= 387 and counter < 516 or counter >= 544 and counter < 739 or\
             counter >= 762 and counter < 826 or counter >= 879 and counter < 1111 or\
             counter >= 1130 and counter < 1202 or counter >= 1288 and counter < 1412 or\
             counter >= 1464 and counter < 1504 or counter >= 1537 and counter < 1965 or\
             counter >= 2001 and counter < 2082 or counter >= 2149 and counter < 2228 or\
             counter >= 2300 and counter < 2633 or counter >= 2658 and counter < 2689 or\
             counter >= 2701 and counter < 2813 or counter >= 2825 and counter < 2933:
            asl_tr.write(line)
        elif counter >= 136 and counter < 173 or counter >= 519 and counter < 544 or\
             counter >= 739 and counter < 762 or counter >= 1412 and counter < 1458 or\
             counter >= 1965 and counter < 2001 or counter >= 2082 and counter < 2094 or\
             counter >= 2228 and counter < 2300:
            asl_dv.write(line)
        elif counter >= 103 and counter < 136 or counter >= 372 and counter < 387 or\
             counter >= 516 and counter < 519 or counter >= 826 and counter < 879 or\
             counter >= 1111 and counter < 1130 or counter >= 1202 and counter < 1288 or\
             counter >= 1458 and counter < 1464 or counter >= 1504 and counter < 1537 or\
             counter >= 2094 and counter < 2149 or counter >= 2633 and counter < 2658 or\
             counter >= 2689 and counter < 2701 or counter >= 2813 and counter < 2825:
            asl_tt.write(line)
        else:
            print(counter,"Line out of range!")
        counter += 1

with open('asl/data/parallel/en.txt', 'r', encoding='utf8') as en, \
     open('asl/data/parallel/en_train.txt', 'w', encoding='utf8') as en_tr, \
     open('asl/data/parallel/en_dev.txt', 'w', encoding='utf8') as en_dv, \
     open('asl/data/parallel/en_test.txt', 'w', encoding='utf8') as en_tt:
    counter = 0
    for line in en:
        if counter < 103                      or counter >= 173 and counter < 372 or\
             counter >= 387 and counter < 516 or counter >= 544 and counter < 739 or\
             counter >= 762 and counter < 826 or counter >= 879 and counter < 1111 or\
             counter >= 1130 and counter < 1202 or counter >= 1288 and counter < 1412 or\
             counter >= 1464 and counter < 1504 or counter >= 1537 and counter < 1965 or\
             counter >= 2001 and counter < 2082 or counter >= 2149 and counter < 2228 or\
             counter >= 2300 and counter < 2633 or counter >= 2658 and counter < 2689 or\
             counter >= 2701 and counter < 2813 or counter >= 2825 and counter < 2933:
            en_tr.write(line)
        elif counter >= 136 and counter < 173 or counter >= 519 and counter < 544 or\
             counter >= 739 and counter < 762 or counter >= 1412 and counter < 1458 or\
             counter >= 1965 and counter < 2001 or counter >= 2082 and counter < 2094 or\
             counter >= 2228 and counter < 2300:
            en_dv.write(line)
        elif counter >= 103 and counter < 136 or counter >= 372 and counter < 387 or\
             counter >= 516 and counter < 519 or counter >= 826 and counter < 879 or\
             counter >= 1111 and counter < 1130 or counter >= 1202 and counter < 1288 or\
             counter >= 1458 and counter < 1464 or counter >= 1504 and counter < 1537 or\
             counter >= 2094 and counter < 2149 or counter >= 2633 and counter < 2658 or\
             counter >= 2689 and counter < 2701 or counter >= 2813 and counter < 2825:
            en_tt.write(line)
        else:
            print(counter,"Line out of range!")
        counter += 1

