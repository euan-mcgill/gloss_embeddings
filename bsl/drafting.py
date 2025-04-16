#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import spacy as sp
import sys

'''
Creating synthetic BSL data through a rule based approach:
This code aims to model BSL grammar by modelling Topic-Comment structure (NOW IN VENV),
interrogative syntax, a lack of verbal inflection, and modelling BSL's 
pronomial structure
'''

if len(sys.argv) < 3:
    print("Usage: python make_synth_bsl.py SOURCE_FILE TARGET_FILE")
    exit(1)

en = sys.argv[1]
out = sys.argv[2]

### emulating Luis' method section
# def get_token_info(token):
#     return { "pre": False, "text": token.text, "pos": token.pos_, "morph": token.morph, "dep": token.dep_, "lemma": token.lemma_, "head": token.head }

# nlp = sp.load("en_core_web_trf")

# with open(en, 'r', encoding='utf-8') as eng, open(out, 'w', encoding='utf-8'):
#     for line in eng:
#         line = line.strip()
#         if len(line) == 0:
#             pass
#         else:
#             tokens = [get_token_info(t) for t in nlp(line)]
            #print(tokens)
        #tokens = nlp(line)
        #for token in tokens:
        #    print(token, token.lemma_, token.pos_, token.dep_, token.morph)

nlp = sp.load("en_core_web_trf")
#nlp = sp.load("en_core_web_lg")


keep_tokens = []
with open(en, 'r', encoding='utf-8') as eng:
    for line in eng:
        print(line)
        print([(token.lemma_, token.dep_) for token in nlp(line.strip())])
        print('\n')
