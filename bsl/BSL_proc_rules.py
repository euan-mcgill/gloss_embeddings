#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
These rules are based on "BSL Corpus Annotation Conventions v2.1", Kearsy Cormier et al.
from  July 2015

The purpose of these rules are to lexicalise the glosses and retain the original meaning
as much as possible for the purposes of machine learning tasks.

contact: {euan.mcgill, santiago.egea}@upf.edu
17/07/2023
'''

import re
#import sys

with open('both_hands_glosses_v2.txt', 'r') as bslcorp, \
     open('free_translation_aligned_v2.txt', 'r') as eng, \
     open('both_hands_glosses_v3.txt', 'w') as out:
    for signs, line in zip(bslcorp, eng):
        #print(signs, line)
        # Template: re.sub(r'', r'', signs_)
        signs_qmk = re.sub(r'\?', r'', signs) # All question mark tags for guessed sign
        signs_ptb = re.sub(r'PT:BODY-', r'', signs_qmk) # all body part prefixes
        signs_sls = re.sub(r'(/.+?)(\s)', r'\2', signs_ptb) # remove trailing possible other annotations after slash, may have to implement >1 time
        signs_ats = re.sub(r'(ADD-TO-SIGNBANK\()(.+?)(\))', r'\2', signs_sls) # remove ADD-TO-SIGNBANK annotator tag and brackets
        signs_atb = re.sub(r'ADD-TO-SIG(B|)N(-|)BANK(\(|)', r'', signs_ats) # remove variations and errors thereof
        # Personal pronoun section (replacement rules) c.f. Sutton-Spence & Woll (2000, p.42)
        signs_osn = re.sub(r'PT:PRO1SG', r'I', signs_atb)
        signs_osg = re.sub(r'PT:POSS1SG', r'MY', signs_osn)
        signs_tsn = re.sub(r'PT:PRO2SG', r'YOU', signs_osg)
        signs_tsg = re.sub(r'PT:POSS2SG', r'YOUR', signs_tsn)
        signs_hsn = re.sub(r'PT:PRO3SG', r'THEY', signs_tsg)
        signs_hsg = re.sub(r'PT:PO(SS|R)3SG', r'THEIR', signs_hsn)
        signs_opn = re.sub(r'PT:PRO1PL', r'WE', signs_hsg)
        signs_opg = re.sub(r'PT:POSS1PL', r'OUR', signs_opn)
        signs_tpn = re.sub(r'PT:PRO2PL', r'YOU-PLURAL', signs_opg)
        signs_tpg = re.sub(r'PT:POSS2PL', r'YOUR-PLURAL', signs_tpn)
        signs_hpn = re.sub(r'PT:PRO3PL', r'THEY-PLURAL', signs_tpg)
        signs_hpg = re.sub(r'PT:POSS3PL', r'THEIR-PLURAL', signs_hpn)
            # end of personal pronoun section
        signs_lbp = re.sub(r'PT:LBUOY', r'', signs_hpg) # list buoy signifier remove
        signs_lbt = re.sub(r'LBUOY-', r'LBUOY ', signs_lbp) # keep list buoy as a single token
        signs_fbp = re.sub(r'(PT:|)FBUOY', r'', signs_lbt) # remove tag from fragment buoy
        signs_dsp = re.sub(r'  ', r' ', signs_fbp) # double space rm
        # Locative pointing signs
        if re.search(r'\bthere\b', line):
            signs_loc = re.sub(r'PT:LOC', 'THERE', signs_dsp)
        elif re.search(r'\bhere\b', line):
            signs_loc = re.sub(r'PT:LOC', 'HERE', signs_dsp)
        else:
            signs_loc = re.sub(r'PT:LOC', 'THERE', signs_dsp)
        # Demonstrative pointing signs
        if re.search(r'\bthat\b', line):
            signs_det = re.sub(r'PT:DET', r'THAT', signs_loc)
        elif re.search(r'\bthis\b', line):
            signs_det = re.sub(r'PT:DET', r'THIS', signs_loc)
        else:
            signs_det = re.sub(r'PT:DET', r'THAT', signs_loc)
        signs_ptc = re.sub(r'PT:', r'IT', signs_det) # unlabelled pointing signs
        signs_clp = re.sub(r'G:CA:', r'', signs_ptc) # classifier predicate markers
        signs_ges = re.sub(r'G:\S+', r'', signs_clp) # remove gestures
        signs_dep = re.sub(r'((DSS|DSH|DSEW|DSEP))', r'\1 ', signs_ges) # add space after depicting signs
        signs_dss = re.sub(r'DSS', r'SHAPE', signs_dep) # Series of depicting signs types
        signs_dsw = re.sub(r'DSEW', r'WHOLE', signs_dss)
        signs_dsp = re.sub(r'DSEP', r'PART', signs_dsw)
        signs_dsh = re.sub(r'DSH', r'HOLD', signs_dsp)
        signs_fst = re.sub(r'(\(|)(FALSE(-|--)START)(\)|)', r'', signs_dsh)
        # movement type signs
        signs_mvt = re.sub(r'(-|:)(AT|BE|MOVE|PIVOT)', r' \2', signs_fst)
        signs_mov = re.sub(r'(AT|BE|MOVE|PIVOT)(:)', r'\1 ', signs_mvt)
        signs_tth = re.sub(r'\(1-VERT\)', r'TALL-THIN', signs_mov)
        signs_lth = re.sub(r'\((1-HORI|1|3|4)\)', r'LONG-THIN', signs_tth)
        signs_tls = re.sub(r'\(2-DOWN\)', r'LEGS-STAND', signs_lth)
        signs_tlr = re.sub(r'\((BENT|BENT0|)2-HORI\)', r'LEGS-RECLINE', signs_tls)
        signs_man = re.sub(r'\((5-HORI|5)\)', r'MULTIPLE', signs_tlr)
        signs_veh = re.sub(r'\((FLAT-(LATERAL|HORI)|ASL-VEH)\)', r'VEHICLE-LIKE', signs_man) # a few of these have no examples in the current incomplete annotated corpus
        signs_dua = re.sub(r'\(2\)', r'DUAL', signs_veh)
        signs_nar = re.sub(r'\(SPOON\)', r'STRAIGHT-NARROW', signs_dua)
        signs_fla = re.sub(r'\(FLAT\)', r'FLAT-OBJECT', signs_nar)
        signs_sph = re.sub(r'\((CYL|O)\)', r'CYLINDRICAL', signs_fla)
        signs_rnd = re.sub(r'\(SPHERE\)', r'ROUND', signs_sph)
        signs_tnf = re.sub(r'\(CLOSED\)', r'THIN-FLAT', signs_rnd)
        signs_tkf = re.sub(r'\(OPEN\)', r'THICK-FLAT', signs_tnf)
        signs_fro = re.sub(r'\(SMALL_(OPEN|CLOSED)\)', r'FLAT-ROUND', signs_tkf)
        signs_thn = re.sub(r'\((FIST|GRIP)\)', r'POLE', signs_fro)
        signs_exo = re.sub(r'\(Y\)', r'OPPOSITE-EXTENSIONS', signs_thn)
        signs_esl = re.sub(r'\(A-DOT\)', r'COMPACT', signs_exo)
        signs_crv = re.sub(r'\(HOOK\)', r'BENT', signs_esl)
        signs_itw = re.sub(r'\(WISH\)', r'INTERTWINED', signs_crv)
        signs_fgp = re.sub(r'\(RUDE\)', r'FINGERTIP', signs_itw)
        signs_snw = re.sub(r'\(PINKY\)', r'SMALL-NARROW', signs_fgp)
        signs_tve = re.sub(r'\(HORNS\)', r'HORN-LIKE', signs_snw)
        signs_swp = re.sub(r'\(OPEN-8\)', r'SWIPE', signs_tve)
        # end of depicting sign movement types
        signs_snm = re.sub(r'(SN:)(.+?)(\(.+?\))', r'\2', signs_swp) # sign names retain only name
        signs_iph = re.sub(r'(\(|)INDECIPHERABLE(\)|)', r'', signs_snm) # remove indecipherable markers
        signs_lex = re.sub(r'(\d+|[a-m])', r'', signs_iph) # lexical variant markers
        signs_brk = re.sub(r'\(.*?\)', r'', signs_lex) # remove rest of bracketed items
        signs_fsp = re.sub(r'FS:(.-|)', r'', signs_brk) # remove fingerspell tag
        signs_crt = re.sub(r'\^', r'-', signs_fsp) # replace carets with dashes for compounds
        signs_trs = re.sub(r'   ', r' ', signs_crt)
        signs_dbs = re.sub(r'  ', r' ', signs_trs)
        out.write(signs_dbs.strip()+'\n')
