# import pandas as pd

import sys
import os
import numpy as np
sys.path.insert(0, "./utils/metrics/")
sys.path.insert(1, './utils')
from nmt_eval import compute_metrics

# METRICS = ['BLEU-GMEAN', 'BLEU-1', 'BLEU-2', 'BLEU-3', 'BLEU-4', 'BLEU-1 (NLTK)', 'BLEU-2 (NLTK)', 'BLEU-3 (NLTK)', 'BLEU-4 (NLTK)', 'METEOR', 'ROUGE_1-F_SCORE', 'ROUGE_1-R_SCORE', 'ROUGE_1-P_SCORE', 'ROUGE_2-F_SCORE', 'ROUGE_2-R_SCORE', 'ROUGE_2-P_SCORE', 'ROUGE_L-F_SCORE', 'ROUGE_L-R_SCORE', 'ROUGE_L-P_SCORE', 'SACREBLEU-CHAR', 'SACREBLEU-INTL', 'TER']
METRICS = ['METEOR', 'ROUGE_L-F_SCORE', 'SACREBLEU-INTL', 'SACREBLEU-CHAR']

if len(sys.argv) < 3:
    print("Usage:")
    print("- python calculate_metrics.py REFERENCE_FILE -d CANDIDATES_DIR")
    print("- python calculate_metrics.py REFERENCE_FILE -r CANDIDATE_PREFIX RANGE_START RANGE_END RANGE_STEP")
    print("- python calculate_metrics.py REFERENCE_FILE -f CANDIDATE_FILE")
    exit(1)

REFERENCE = sys.argv[1]

if sys.argv[2] == '-d':
    # compare to all files in a directory
    CANDIDATE_ROOT = sys.argv[3]
    CANDIDATES = [CANDIDATE_ROOT + '/' + filename for filename in os.listdir(CANDIDATE_ROOT)]
elif sys.argv[2] == '-r':
    # compare to a range
    CANDIDATE_PREFIX = sys.argv[3]
    RANGE_FROM = int(sys.argv[4])
    RANGE_TO = int(sys.argv[5])
    RANGE_STEP = int(sys.argv[6])
    CANDIDATES = [CANDIDATE_PREFIX + str(step) + ".txt" for step in range(RANGE_FROM,RANGE_TO,RANGE_STEP)]
elif sys.argv[2] == '-f':
    # compare to a single file
    CANDIDATES = [sys.argv[3]]

with open(REFERENCE) as f:
    reference = [s.strip() for s in f.readlines()]

print("References:",len(reference))

all_results = []

for candidate_file in CANDIDATES:
    print(candidate_file)
    with open(candidate_file) as f:
        candidate = [s.strip() for s in f.readlines()]
    results = compute_metrics(reference, candidate)
    all_results.append([candidate_file.split('/')[-1]] + [results[m] for m in METRICS])

print("FILE\t" + "\t".join(s.replace(' ','_') for s in METRICS))
for r in all_results:
    print("\t".join([str(s) for s in r]))
