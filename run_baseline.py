import os
import sys
import spacy
from rule_baseline import baseline_translation
# from permute_window import permutation

if len(sys.argv) < 3:
    print("Usage: python rule_baseline.py SOURCE_FILE TARGET_FILE")
    exit(1)

SRC_FILE = sys.argv[1]
TGT_FILE = sys.argv[2]

nlp = spacy.load("es_core_news_md")

# def get_person(morph):
#     if "Person=1" in morph:
#         return "YO"
#     elif "Person=2" in morph:
#         return "TÚ"
#     else:
#         return "ÉL"

def get_person(morph):
    if "Person=1" in morph and "Number=Sing":
        return "INDX.PRO:1SG"
    elif "Person=1" in morph and "Number=Plur":
        return "INDX.PRO:1PL"
    elif "Person=2" in morph and "Number=Sing":
        return "INDX.PRO:2SG"
    elif "Person=2" in morph and "Number=Plur":
        return "INDX.PRO:2PL"
    elif "Person=3" in morph and "Number=Sing":
        return "INDX.PRO:3SG"
    elif "Person=3" in morph and "Number=Plur":
        return "INDX.PRO:3PL"
    else:
        return "INDX"

def get_token_info(token):
    return { "pre": False, "text": token.text, "pos": token.pos_, "morph": token.morph, "dep": token.dep_, "lemma": token.lemma_, "head": token.head }

with open(SRC_FILE) as i:
    with open(TGT_FILE, 'w') as o:
        for line in i:
            line = line.strip()
            if len(line) == 0:
                o.write('\n')
            else:
                tokens = [get_token_info(t) for t in nlp(line)]
                o.write(baseline_translation(tokens) + '\n')

print("Now regex cleanup and INDX.DEM, INDX.LOC, INDX.AUX")
