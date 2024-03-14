# Significance testing

# NGT T2G (Done)

### Baseline vs. Baseline-enc
echo "N2G T2G" && python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt ngt/runs/tg/run03/step_9800_pre_03.txt ngt/runs/tg-enc/run01/step_5000_pre_01.txt
p=0.318

### Baseline vs. Baseline-dec
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt ngt/runs/tg/run03/step_9800_pre_03.txt ngt/runs/tg-dec/run01/step_9200_pre_01.txt
p=0.003

### Baseline vs. Baseline-both
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt ngt/runs/tg/run03/step_9800_pre_03.txt ngt/runs/tg-both/run02/step_9600_pre_02.txt
p=0.477

### Baseline vs. PTFT
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt ngt/runs/tg/run03/step_9800_pre_03.txt ngt/runs/tg-finetune/run03_02/step_11600_pre_02.txt
p=0.01

### Baseline vs. PTFT-enc
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt ngt/runs/tg/run03/step_9800_pre_03.txt ngt/runs/tg-ft-enc/run03_03/step_14600_pre_03.txt
p<0.00

### Baseline vs. PTFT-dec
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt ngt/runs/tg/run03/step_9800_pre_03.txt ngt/runs/tg-ft-dec/run02_01/step_8600_pre_01.txt
p=0.372

### Baseline vs. PTFT-both
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt ngt/runs/tg/run03/step_9800_pre_03.txt ngt/runs/tg-ft-both/run01_01/step_7800_pre_01.txt
p<0.00

### PTFT vs. PTFT-enc
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt ngt/runs/tg-finetune/run03_02/step_11600_pre_02.txt ngt/runs/tg-ft-enc/run03_03/step_14600_pre_03.txt
p=0.05

# NGT G2T (Done)

### PTFT vs. PTFT-enc
echo "ngt g2t" && python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok ngt/data/CorpusNGT/nlngt_test_nl.txt ngt/runs/gt-finetune/run03_01/step_11600_pre_01.txt ngt/runs/gt-ft-enc/run03_03/step_13200_pre_03.txt
p=0.228

### PTFT vs. PTFT-dec
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok ngt/data/CorpusNGT/nlngt_test_nl.txt ngt/runs/gt-finetune/run03_01/step_11600_pre_01.txt ngt/runs/gt-ft-dec/run02_03/step_10200_pre_03.txt
p=0.265

### PTFT vs. PTFT-both
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok ngt/data/CorpusNGT/nlngt_test_nl.txt ngt/runs/gt-finetune/run03_01/step_11600_pre_01.txt ngt/runs/gt-ft-both/run01_02/step_13400_pre_02.txt
p=0.342

# ASL T2G

### Baseline vs. Baseline-enc
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok asl/data/parallel/asl_test.txt asl/runs/tg/run02/step_9000_pre_02.txt asl/runs/tg-enc/run01/step_9200_pre_01.txt
p=0.056

### Baseline vs. Baseline-dec
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok asl/data/parallel/asl_test.txt asl/runs/tg/run02/step_9000_pre_02.txt asl/runs/tg-dec/run01/step_4800_pre_01.txt
p=0.083

### Baseline vs. Baseline-both
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok asl/data/parallel/asl_test.txt asl/runs/tg/run02/step_9000_pre_02.txt asl/runs/tg-both/run03/step_8400_pre_03.txt
p=0.230

### Baseline vs. PTFT
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok asl/data/parallel/asl_test.txt asl/runs/tg/run02/step_9000_pre_02.txt asl/runs/tg-finetune/run03_02/step_9600_pre_02.txt
p=0.050

### Baseline vs. PTFT-enc
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok asl/data/parallel/asl_test.txt asl/runs/tg/run02/step_9000_pre_02.txt asl/runs/tg-ft-enc/run02_01/step_10600_pre_01.txt
p=0.008

### Baseline vs. PTFT-dec
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok asl/data/parallel/asl_test.txt asl/runs/tg/run02/step_9000_pre_02.txt asl/runs/tg-ft-dec/run03_03/step_11400_pre_03.txt
p=0.062

### Baseline vs. PTFT-both
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok asl/data/parallel/asl_test.txt asl/runs/tg/run02/step_9000_pre_02.txt asl/runs/tg-ft-both/run02_03/step_5400_pre_03.txt

### PTFT vs. PTFT-enc
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok asl/data/parallel/asl_test.txt asl/runs/tg-finetune/run03_02/step_9600_pre_02.txt asl/runs/tg-ft-enc/run02_01/step_10600_pre_01.txt

### PTFT vs. PTFT-dec
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok asl/data/parallel/asl_test.txt asl/runs/tg-finetune/run03_02/step_9600_pre_02.txt asl/runs/tg-ft-dec/run03_03/step_11400_pre_03.txt

### PTFT vs. PTFT-both
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok asl/data/parallel/asl_test.txt asl/runs/tg-finetune/run03_02/step_9600_pre_02.txt asl/runs/tg-ft-both/run02_03/step_5400_pre_03.txt

# ASL G2T

### Baseline vs. PTFT
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok asl/data/parallel/en_test_tok.txt asl/runs/gt/run02/step_5400_pre_02.txt asl/runs/gt-finetune/run01_02/step_12200_pre_02.txt

### Baseline vs. PTFT-enc
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok asl/data/parallel/en_test_tok.txt asl/runs/gt/run02/step_5400_pre_02.txt asl/runs/gt-ft-enc/run02_03/step_10200_pre_03.txt

### Baseline vs. PTFT-dec
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok asl/data/parallel/en_test_tok.txt asl/runs/gt/run02/step_5400_pre_02.txt asl/runs/gt-ft-dec/run03_02/step_11400_pre_02.txt

### Baseline vs. PTFT-both
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok asl/data/parallel/en_test_tok.txt asl/runs/gt/run02/step_5400_pre_02.txt asl/runs/gt-ft-both/run01_02/step_14400_pre_02.txt

### PTFT vs. PTFT-enc
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok asl/data/parallel/en_test_tok.txt asl/runs/gt-finetune/run01_02/step_12200_pre_02.txt asl/runs/gt-ft-enc/run02_03/step_10200_pre_03.txt

### PTFT vs. PTFT-dec
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok asl/data/parallel/en_test_tok.txt asl/runs/gt-finetune/run01_02/step_12200_pre_02.txt asl/runs/gt-ft-dec/run03_02/step_11400_pre_02.txt

### PTFT vs. PTFT-both
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok asl/data/parallel/en_test_tok.txt asl/runs/gt-finetune/run01_02/step_12200_pre_02.txt asl/runs/gt-ft-both/run01_02/step_14400_pre_02.txt


# FinSL T2G

### Baseline vs. Baseline-enc
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok fsl/data/test_gloss.txt fsl/runs/t2g_base_noemb_out_test_model_step_8400.txt fsl/runs/t2g_base_embenc_out_test_model_step_9500.txt

### Baseline vs. Baseline-both
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok fsl/data/test_gloss.txt fsl/runs/t2g_base_noemb_out_test_model_step_8400.txt fsl/runs/t2g_base_embboth_out_test_model_step_4300.txt

### Baseline vs. PTFT
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok fsl/data/test_gloss.txt fsl/runs/t2g_base_noemb_out_test_model_step_8400.txt fsl/runs/t2g_ptft_noemb_out_test_model_5100_step_12400.txt

### Baseline vs. PTFT-enc
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok fsl/data/test_gloss.txt fsl/runs/t2g_base_noemb_out_test_model_step_8400.txt fsl/runs/t2g_ptft_emb fsl/runs/t2g_ptft_embenc_out_test_model_3900_step_12100.txt

### Baseline vs. PTFT-dec
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok fsl/data/test_gloss.txt fsl/runs/t2g_base_noemb_out_test_model_step_8400.txt fsl/runs/t2g_ptft_emb fsl/runs/t2g_ptft_embdec_out_test_model_4200_step_8900.txt

### Baseline vs. PTFT-both
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok fsl/data/test_gloss.txt fsl/runs/t2g_base_noemb_out_test_model_step_8400.txt fsl/runs/t2g_ptft_emb fsl/runs/t2g_ptft_embboth_out_test_model_2800_step_10700.txt

### PTFT vs. PTFT-enc
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok fsl/data/test_gloss.txt fsl/runs/t2g_ptft_noemb_out_test_model_5100_step_12400.txt fsl/runs/t2g_ptft_embenc_out_test_model_3900_step_12100.txt

### PTFT vs. PTFT-dec
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok fsl/data/test_gloss.txt fsl/runs/t2g_ptft_noemb_out_test_model_5100_step_12400.txt fsl/runs/t2g_ptft_embdec_out_test_model_4200_step_8900.txt

### PTFT vs. PTFT-both
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok fsl/data/test_gloss.txt fsl/runs/t2g_ptft_noemb_out_test_model_5100_step_12400.txt fsl/runs/t2g_ptft_embboth_out_test_model_2800_step_10700.txt


# FinSL G2T

### Baseline vs. Baseline-enc
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok fsl/data/test_text.txt fsl/runs/g2t_base_noemb_out_test_model_step_9600.txt fsl/runs/

### Baseline vs. Baseline-dec
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok fsl/data/test_text.txt fsl/runs/g2t_base_noemb_out_test_model_step_9600.txt fsl/runs/

### Baseline vs. Baseline-both
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok fsl/data/test_text.txt fsl/runs/g2t_base_noemb_out_test_model_step_9600.txt fsl/runs/

### Baseline vs. PTFT
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok fsl/data/test_text.txt fsl/runs/g2t_base_noemb_out_test_model_step_9600.txt fsl/runs/g2t_ptft_noemb_out_test_model_9000_step_15000.txt

### Baseline vs. PTFT-enc
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok fsl/data/test_text.txt fsl/runs/g2t_base_noemb_out_test_model_step_9600.txt fsl/runs/g2t_base_embenc_out_test_model_step_10000.txt

### Baseline vs. PTFT-dec
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok fsl/data/test_text.txt fsl/runs/g2t_base_noemb_out_test_model_step_9600.txt fsl/runs/g2t_base_embdec_out_test_model_step_8400.txt

### Baseline vs. PTFT-both
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok fsl/data/test_text.txt fsl/runs/g2t_base_noemb_out_test_model_step_9600.txt fsl/runs/g2t_base_embboth_out_test_model_step_7400.txt

### PTFT vs. PTFT-enc
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok fsl/data/test_text.txt fsl/runs/g2t_ptft_noemb_out_test_model_9000_step_15000.txt fsl/runs/g2t_base_embenc_out_test_model_step_10000.txt

### PTFT vs. PTFT-dec
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok fsl/data/test_text.txt fsl/runs/g2t_ptft_noemb_out_test_model_9000_step_15000.txt fsl/runs/g2t_base_embdec_out_test_model_step_8400.txt

### PTFT vs. PTFT-both
python ../util-scripts/paired-bootstrap.py --eval_type bleu_detok fsl/data/test_text.txt fsl/runs/g2t_ptft_noemb_out_test_model_9000_step_15000.txt fsl/runs/g2t_base_embboth_out_test_model_step_7400.txt
