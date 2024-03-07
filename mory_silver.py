#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
A script to implement the 'General Data Augmentation Rules' from
Moryossef et al. (2021) "Data Augmentation for Sign Language Gloss
Translation"

running: python mory_silver.py <input_monolingual_file> <output_file_name>

2023-03-07
euan.mcgill@upf.edu
'''

import spacy as sp
import sys
from random import randint
from permute_window import permutation

# Lemmatise and restrict PoS category
def lem_n_pos(infile):
    print("Generating silver glosses by rules...\n\n")
    with open(infile, 'r', encoding='utf8') as ff:
        nlp = sp.load("fi_core_news_md")
        lem_sents = []
        for line in ff:
            doc = nlp(line)
            pos = ' '.join(token.lemma_ for token in doc if token.pos_ == "VERB" or\
                token.pos_ == "NOUN" or token.pos_ == "PRON" or token.pos_ == "PROPN"\
                or token.pos_ == "ADJ" or token.pos_ == "ADV" or token.pos_ == "NUM")
            lem_sents.append(pos.lower())
        return lem_sents

# Discard tokens with p=0.2
def discarder(alltok):
    print("Randomly dropping and reordering tokens...\n\n")
    dis_sents = []
    for sent in alltok:
        dis = []
        for tok in sent.split():
            rno = randint(1,5)
            if rno == 5:
                pass
            elif rno < 5:
                dis.append(tok)
        dis_sents.append(' '.join(dis))
    return(dis_sents)

# Permute tokens within a window of 4 (maybe just use other script)
def permute(distok):
    per_sents = []
    for line in distok:
        per = permutation(line.split(), 4)
        per_sents.append(' '.join(p for p in per))
    print("Done!\n")
    return per_sents

def main():
    infile = sys.argv[1]
    outfile = sys.argv[2]
    alltok = lem_n_pos(infile)
    distok = discarder(alltok)
    pertok = permute(distok)
    with open(outfile, 'w', encoding='utf8') as out:
        for line in pertok:
            out.write(line+'\n')

if __name__ == '__main__':
    print("\n\nRunning: python mory_silver.py <input_monolingual_file>\
           <output_file_name>\n\n\n")
    main()
