#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://medium.com/@ajazturki10/allennlp-dependency-parsing-semantic-role-labelling-coreference-resolution-70637afbe8cf
AllenNLP uses PropBank Annotation. As a result,each verb sense has numbered arguments e.g., ARG-0, ARG-1,
https://garethejones.wordpress.com/2008/03/21/bsl-word-ordering/
https://verbs.colorado.edu/~mpalmer/projects/ace/PBguidelines.pdf - labelling guidelines

etc.

ARG-0 is usually PROTO-AGENT

ARG-1 is usually PROTO-PATIENT

ARG-2 is usually benefactive, instrument, attribute

ARG-3 is usually start point, benefactive, instrument, attribute

ARG-4 is usually end point (e.g., for move or push style verbs)
'''

print("\n\nEnsure a Python 3.7 Virtual Environment is activated and dependencies \
(requirements.txt) are installed! \n\n\n")

from allennlp.predictors.predictor import Predictor
import allennlp_models.tagging
import warnings
import re
import spacy as sp
import sys

def get_tok_info(token):
    return { "pre": False, "text": token.text, "pos": token.pos_, "morph": token.morph, \
             "dep": token.dep_, "lemma": token.lemma_, "head": token.head, "sem": None }

def semantic_role(sent):
    roles = None
    for tok in nlp(sent):
        if tok.dep_ == 'ROOT':
            root = tok
    predictions = predictor.predict(sentence=sent)
    lastresort = None
    for p in predictions["verbs"]:
        if p['verb'] == str(root):
            roles = p["tags"]
        else:
            lastresort = p["tags"]
    if roles is None:
        if lastresort is None:
            roles = ['0'] * len(predictions['words'])
        else:
            roles = lastresort
    assert(roles is not None)
    return roles

def tag_dict(sent):
    rls = semantic_role(sent)
    tokens = [get_tok_info(t) for t in nlp(sent) if not t.is_space]
    assert(len(tokens)==len(rls))
    for idx, vlu in enumerate(rls):
        tokens[idx]["sem"] = vlu
    return tokens

def rule_and_reorder(tagged):
    # Rule containers for each stage
    chkpt_a = []
    chkpt_b = []
    chkpt_c = []
    chkpt_d = []
    times = []
    locations = []
    topics = []
    agents = []
    predicates = []
    verbs = []
    endpoints = []
    others = []
    #### restrict to certain PoS categories ####
    for tag in tagged:
        if tag["pos"] == 'ADJ' or tag["pos"] == 'ADV' \
        or tag["pos"] == 'CCONJ' or tag["pos"] == 'INTJ' \
        or tag["pos"] == 'NOUN' or tag["pos"] == 'NUM' \
        or tag["pos"] == 'PRON' \
        or tag["pos"] == 'PROPN' or tag["pos"] == 'SCONJ' \
        or tag["pos"] == 'VERB' \
        or tag["pos"] == 'PART' and tag["dep"] == 'neg' \
        or tag["pos"] == 'ADP' and re.search(r'(in|from|to|on|before|after)', tag['text']) \
        or tag["pos"] == 'DET' and 'PronType=Art' not in tag['morph'] \
        or tag["pos"] == 'AUX' \
        and re.search(r'(be|ca|can|could|may|must|might|need|should|will|wo|would|\'ll|\'d)', tag['lemma']):
            chkpt_a.append(tag)

    #### ordering of NEG + VERB to VERB + NEG (use deps) ####
    skip_next = False
    for a1, a2 in zip(chkpt_a, chkpt_a[1:]):
        if skip_next:
            skip_next = False
            continue
        if a1['dep'] == 'neg' and a2['pos'] == 'VERB':
            chkpt_b.append(a2.copy())
            chkpt_b.append(a1.copy())
            skip_next = True
        else:
            chkpt_b.append(a1.copy())
    if not skip_next:
        chkpt_b.append(chkpt_a[-1].copy())
    
    #### ordering of ADJ + NOUN to NOUN + ADJ(use deps) ####
    skip_next = False
    for b1, b2 in zip(chkpt_b, chkpt_b[1:]):
        if skip_next:
            skip_next = False
            continue
        if b1['dep'] == 'amod' and re.search(r'(NOUN|PROPN)', b2['pos']):
            chkpt_c.append(b2.copy())
            chkpt_c.append(b1.copy())
            skip_next = True
        else:
            chkpt_c.append(b1.copy())
    if not skip_next:
        chkpt_c.append(chkpt_b[-1].copy())
    
    # PRON + Copula + ADJ -> PRON + ADJ + PRON
    skip_next = False
    skip_again = False
    for c1,c2,c3 in zip(chkpt_c, chkpt_c[1:], chkpt_c[2:]):
        if skip_next:
            skip_next = False
            continue
        if skip_again:
            skip_again = False
            continue
        if c1['pos'] == 'PRON' and re.search(r'(VERB|AUX)', c2['pos']) \
        and re.search(r'(acomp|cop|attr)', c3['dep']):
            chkpt_d.append(c1.copy())
            chkpt_d.append(c3.copy())
            chkpt_d.append(c1.copy())
            skip_next = True
            skip_again = True
        else:
            chkpt_d.append(c1.copy())
    if not skip_next:
        chkpt_d.append(chkpt_c[-2].copy())
        chkpt_d.append(chkpt_c[-1].copy())
    
    #### Word order - topics, args, others and verbs ####
    for glo in chkpt_d:
        #print(glo['text'], glo['pos'], glo['dep'], glo['sem'])
        if re.search(r'ARGM-TMP', glo['sem']):
            times.append(glo.copy())
        elif re.search(r'ARGM-LOC', glo['sem']):
            locations.append(glo.copy())
        elif re.search(r'ARGM-(CAU|PNC)', glo['sem']):
            topics.append(glo.copy())
        elif re.search(r'ARG0', glo['sem']):
            agents.append(glo.copy())
        elif re.search(r'ARG[1-3]', glo['sem']):
            predicates.append(glo.copy())
        elif re.search(r'ARG4', glo['sem']): # not all WH- are ARG4, so move with regex
            endpoints.append(glo.copy())
        elif re.search(r'V', glo['sem']):
            verbs.append(glo.copy())
        else:
            others.append(glo.copy())
    ordered = times + locations + topics + predicates + agents + verbs + endpoints + others
    return ordered

def write_and_regex(ruled):
    # lemmatise and uppercase
    return " ".join(w['lemma'].upper() for w in ruled)

########################################## MAIN ##########################################

print("\n\n\nModels loading...\n\n\n")

warnings.filterwarnings("ignore")
SRL_MODEL_PATH = "https://storage.googleapis.com/allennlp-public-models/structured-prediction-srl-bert.2020.12.15.tar.gz"
predictor = Predictor.from_path(SRL_MODEL_PATH)
nlp = sp.load('en_core_web_sm')
SRC_FILE = sys.argv[1]
TGT_FILE = sys.argv[2]

print("Model loading complete\n\n\n")
print("Glossing in progress...\n\n\n")

# sent = "Uriah and Alex honestly do not think he could not beat the difficult game in under three hours because they have no thumbs?."
# sent = "How much do these two honey doughnuts cost?"
# sent = "What does Alex eat for lunch and where?"
# sem = semantic_role(sent)
# sent = "I am a teacher"
# tagged = tag_dict(sent)
# ruled = rule_and_reorder(tagged)
# for i in tagged:
#     print(i['text'], i['dep'], i['pos'], i['sem'])
# for i in ruled:
#     print(i['text'], i['dep'], i['pos'], i['sem'])
# print(" ".join(w['lemma'].upper() for w in ruled))

with open(SRC_FILE, 'r', encoding='utf-8') as en, \
     open(TGT_FILE, 'w', encoding='utf-8') as out:
    for line in en:
        #roles = semantic_role(line)
        tagged = tag_dict(line.strip())
        ruled = rule_and_reorder(tagged)
        #print(write_and_regex(ruled))
        out.write(write_and_regex(ruled) + '\n')

print("\n\n Glosses created successfully! Now ReGex processing\n\n\n")

# retain FROM and TO and/or FROM-TO
# WH- questions (remember hyphened ones)
# topics then patients ARG-0 and share head (or anything with an ARG0-tag, anything with a tag at all, then 0s)
# Pronouns - regex (he, him = HE[lemma], his = HIS[lemma])
# regex n't -> not and other tokenising problems (ca, n't, 'll etc.)
# numbers
# remove copula BE?

'''
RegExes

Contractions and negative affixes
\bBE N'T\b -> NOT x
\b(WO|WOULD)\b -> WILL x
('LL|'D) -> WILL x
'VE -> HAVE x
\b(CA|COULD)\b -> CAN x
N'T -> NOT x
\b(HAVE|UNDERSTAND)(\s)(NOT)$ -> \3-\1 x
\b(HAVE|UNDERSTAND)(\s)(NOT) -> \3-\1 x
\b(CAN|WILL|KNOW|CARE|LIKE)(\s)(NOT)$ -> \1-\3 x
\b(CAN|WILL|KNOW|CARE|LIKE)(\s)(NOT) -> \1-\3 x
(GET)( )(OVER|ON|OUT) -> \1-\3 x
( 'S | 'S|'S | GET |GET | GET)$ -> 0 x
( 'S | 'S|'S | GET |GET | GET) -> \s x

Pronouns
\bTHEY\b -> THEY-PLURAL x
\b(THEIR|THEIRS)\b -> THEIR-PLURAL x
\b(YOU BOTH|BOTH YOU|YOU TWO)\b -> YOU-PLURAL x
\b(HE|SHE)\b -> THEY x
\b(HIS|HERS)\b -> THEIR x

WH-questions
\b(HOW)(MUCH|MANY|OLD)\b -> \1-\2 x
\b(WHAT\b|WHO\b|WHERE\b|WHEN\b|HOW-MANY\b|HOW-MUCH\b|HOW-OLD\b).(\S.+) -> \2 \1 x

Numbers
\b10\b -> TEN
\b11\b -> ELEVEN
\b1\b -> ONE
(\b)(ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN|ELEVEN|TWELVE)(\b)( )(O'CLOCK) -> \5-\2
(0) -> \sZERO up to (9) -> \sNINE
fixed spacing
\b(YEAR OLD)\b -> YEAR-OLD
(ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN|ELEVEN|TWELVE)( )(ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN|ELEVEN|TWELVE)( )(YEAR OLD) -> AGE-\1 \3
(ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN|ELEVEN|TWELVE)( )(YEAR OLD) -> AGE-\1

From-to
(\bFROM\b)(.)(\S.+)(\bTO\b) -> \3\1-\4

'''

