import os
import sys
import spacy

if len(sys.argv) < 4:
    print("Usage: python spacy_features.py IN_FILE OUT_TOKEN_FILE OUT_POS_FILE OUT_DEP_FILE")
    exit(1)

IN_FILE = sys.argv[1]
OUT_TOKEN_FILE = sys.argv[2]
OUT_POS_FILE = sys.argv[3]
OUT_DEP_FILE = sys.argv[4]

#nlp = spacy.load("es_core_news_md")
nlp = spacy.load("en_core_web_sm")
#nlp = spacy.load("fi_core_news_md")

def get_features(text):
    tokens = nlp(text)
    return [(str(token), token.pos_, token.dep_) for token in tokens]

with open(IN_FILE) as i, open(OUT_TOKEN_FILE,'w') as ot, open(OUT_POS_FILE,'w') as op, open(OUT_DEP_FILE,'w') as od:
    for line in i:
        line = line.strip()
        feats = get_features(line)
        tokens,pos,dep = zip(*feats)
        ot.write(" ".join(tokens) + '\n')
        op.write(" ".join(pos) + '\n')
        od.write(" ".join(dep) + '\n')
