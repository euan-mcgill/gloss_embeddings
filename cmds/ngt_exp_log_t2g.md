# Text2Gloss - NGT

----------------------------------------------------------------------------------------------
## STAGE 1 - Baseline
----------------------------------------------------------------------------------------------

`python3 ../OpenNMT-py/build_vocab.py --config nlngt_run01.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config nlngt_run01.yaml --log_file tg/nlngt_run01.log`
`python3 ../OpenNMT-py/train.py --config nlngt_run02.yaml --log_file tg/nlngt_run02.log`
`python3 ../OpenNMT-py/train.py --config nlngt_run03.yaml --log_file tg/nlngt_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg/tg_01_step_${i}.pt -src nlngt_test_nl.txt -output tg/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg/tg_02_step_${i}.pt -src nlngt_test_nl.txt -output tg/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg/tg_03_step_${i}.pt -src nlngt_test_nl.txt -output tg/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg/run01/* ngt/runs/tg/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg/run02/* ngt/runs/tg/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg/run03/* ngt/runs/tg/run03`

`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg/run01`
`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg/run02`
`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg/run03`

----------------------------------------------------------------------------------------------
## STAGE 1a - Baseline + embs
----------------------------------------------------------------------------------------------

## encoder embs
`python3 ../OpenNMT-py/build_vocab.py --config nlngt_enc_run01.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config nlngt_enc_run01.yaml --log_file tg-enc/nlngt_enc_run01.log`
`python3 ../OpenNMT-py/train.py --config nlngt_enc_run02.yaml --log_file tg-enc/nlngt_enc_run02.log`
`python3 ../OpenNMT-py/train.py --config nlngt_enc_run03.yaml --log_file tg-enc/nlngt_enc_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-enc/tg_01_step_${i}.pt -src nlngt_test_nl.txt -output tg-enc/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-enc/tg_02_step_${i}.pt -src nlngt_test_nl.txt -output tg-enc/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-enc/tg_03_step_${i}.pt -src nlngt_test_nl.txt -output tg-enc/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-enc/run01/* ngt/runs/tg-enc/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-enc/run02/* ngt/runs/tg-enc/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-enc/run03/* ngt/runs/tg-enc/run03`

`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-enc/run01`
`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-enc/run02`
`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-enc/run03`

## decoder embs
`python3 ../OpenNMT-py/build_vocab.py --config nlngt_dec_run01.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config nlngt_dec_run01.yaml --log_file tg-dec/nlngt_dec_run01.log`
`python3 ../OpenNMT-py/train.py --config nlngt_dec_run02.yaml --log_file tg-dec/nlngt_dec_run02.log`
`python3 ../OpenNMT-py/train.py --config nlngt_dec_run03.yaml --log_file tg-dec/nlngt_dec_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-dec/tg_01_step_${i}.pt -src nlngt_test_nl.txt -output tg-dec/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-dec/tg_02_step_${i}.pt -src nlngt_test_nl.txt -output tg-dec/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-dec/tg_03_step_${i}.pt -src nlngt_test_nl.txt -output tg-dec/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-dec/run01/* ngt/runs/tg-dec/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-dec/run02/* ngt/runs/tg-dec/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-dec/run03/* ngt/runs/tg-dec/run03`

`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-dec/run01`
`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-dec/run02`
`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-dec/run03`

## encoder and decoder embs
`python3 ../OpenNMT-py/build_vocab.py --config nlngt_both_run01.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config nlngt_both_run01.yaml --log_file tg-both/nlngt_both_run01.log`
`python3 ../OpenNMT-py/train.py --config nlngt_both_run02.yaml --log_file tg-both/nlngt_both_run02.log`
`python3 ../OpenNMT-py/train.py --config nlngt_both_run03.yaml --log_file tg-both/nlngt_both_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-both/tg_01_step_${i}.pt -src nlngt_test_nl.txt -output tg-both/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-both/tg_02_step_${i}.pt -src nlngt_test_nl.txt -output tg-both/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-both/tg_03_step_${i}.pt -src nlngt_test_nl.txt -output tg-both/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-both/run01/* ngt/runs/tg-both/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-both/run02/* ngt/runs/tg-both/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-both/run03/* ngt/runs/tg-both/run03`

`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-both/run01`
`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-both/run02`
`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-both/run03`

----------------------------------------------------------------------------------------------
## STAGE 2 - PT+FT
----------------------------------------------------------------------------------------------

### pretrain phase

`python3 ../OpenNMT-py/build_vocab.py --config nlngt_pt_vocab.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config nlngt_pt_run01.yaml --log_file tg-pretrain/nlngt_pt_run01.log`
`python3 ../OpenNMT-py/train.py --config nlngt_pt_run02.yaml --log_file tg-pretrain/nlngt_pt_run02.log`
`python3 ../OpenNMT-py/train.py --config nlngt_pt_run03.yaml --log_file tg-pretrain/nlngt_pt_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pretrain/tg-pretrain_01_step_${i}.pt -src nlngt_test_nl.txt -output tg-pretrain/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pretrain/tg-pretrain_02_step_${i}.pt -src nlngt_test_nl.txt -output tg-pretrain/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pretrain/tg-pretrain_03_step_${i}.pt -src nlngt_test_nl.txt -output tg-pretrain/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-pretrain/run01/* ngt/runs/tg-pretrain/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-pretrain/run02/* ngt/runs/tg-pretrain/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-pretrain/run03/* ngt/runs/tg-pretrain/run03`

`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-pretrain/run01`
`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-pretrain/run02`
`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-pretrain/run03`

### finetune phase

### run 1 @ 7600 epochs

`python3 ../OpenNMT-py/train.py --config  nlngt_ft_7600_run01.yaml --train_from tg-pretrain/models/tg-pretrain_01_step_7600.pt --reset_optim keep_states --log_file tg-finetune/nlngt_ft_7600_run01.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_7600_run02.yaml --train_from tg-pretrain/models/tg-pretrain_01_step_7600.pt --reset_optim keep_states --log_file tg-finetune/nlngt_ft_7600_run02.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_7600_run03.yaml --train_from tg-pretrain/models/tg-pretrain_01_step_7600.pt --reset_optim keep_states --log_file tg-finetune/nlngt_ft_7600_run03.log`

`for ((i = 7800; i<= 12600; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_01_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-finetune/run01_01/step_${i}_pre_01.txt; done`
`for ((i = 7800; i<= 12600; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_02_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-finetune/run01_02/step_${i}_pre_02.txt; done`
`for ((i = 7800; i<= 12600; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_03_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-finetune/run01_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-finetune/run01_01/*.txt ngt/runs/runs_finetune/run01_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-finetune/run01_02/*.txt ngt/runs/runs_finetune/run01_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-finetune/run01_03/*.txt ngt/runs/runs_finetune/run01_03`

`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-finetune/run01_01`
`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-finetune/run01_02`
`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-finetune/run01_03`

### run 2 @ 7600 epochs

`python3 ../OpenNMT-py/train.py --config  nlngt_ft_7600_run01.yaml --train_from tg-pretrain/models/tg-pretrain_02_step_7600.pt --reset_optim keep_states --log_file tg-finetune/nlngt_ft_7600_run01.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_7600_run02.yaml --train_from tg-pretrain/models/tg-pretrain_02_step_7600.pt --reset_optim keep_states --log_file tg-finetune/nlngt_ft_7600_run02.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_7600_run03.yaml --train_from tg-pretrain/models/tg-pretrain_02_step_7600.pt --reset_optim keep_states --log_file tg-finetune/nlngt_ft_7600_run03.log`

`for ((i = 7800; i<= 12600; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_7600_01_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-finetune/run02_01/step_${i}_pre_01.txt; done`
`for ((i = 7800; i<= 12600; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_7600_02_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-finetune/run02_02/step_${i}_pre_02.txt; done`
`for ((i = 7800; i<= 12600; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_7600_03_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-finetune/run02_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-finetune/run02_01/*.txt ngt/runs/runs_finetune/run02_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-finetune/run02_02/*.txt ngt/runs/runs_finetune/run02_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-finetune/run02_03/*.txt ngt/runs/runs_finetune/run02_03`

`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-finetune/run02_01`
`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-finetune/run02_02`
`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-finetune/run02_03`

### run 3 @ 8400 epochs

`python3 ../OpenNMT-py/train.py --config  nlngt_ft_8400_run01.yaml --train_from tg-pretrain/models/tg-pretrain_03_step_8400.pt --reset_optim keep_states --log_file tg-finetune/nlngt_ft_8400_run01.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_8400_run02.yaml --train_from tg-pretrain/models/tg-pretrain_03_step_8400.pt --reset_optim keep_states --log_file tg-finetune/nlngt_ft_8400_run02.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_8400_run03.yaml --train_from tg-pretrain/models/tg-pretrain_03_step_8400.pt --reset_optim keep_states --log_file tg-finetune/nlngt_ft_8400_run03.log`

`for ((i = 8600; i<= 13400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_8400_01_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-finetune/run03_01/step_${i}_pre_01.txt; done`
`for ((i = 8600; i<= 13400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_8400_02_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-finetune/run03_02/step_${i}_pre_02.txt; done`
`for ((i = 8600; i<= 13400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_8400_03_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-finetune/run03_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-finetune/run03_01/*.txt ngt/runs/runs_finetune/run03_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-finetune/run03_02/*.txt ngt/runs/runs_finetune/run03_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-finetune/run03_03/*.txt ngt/runs/runs_finetune/run03_03`

`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-finetune/run03_01`
`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-finetune/run03_02`
`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-finetune/run03_03`

----------------------------------------------------------------------------------------------

## encoder embs

### pretrain phase

### finetune phase

----------------------------------------------------------------------------------------------

## decoder embs

### pretrain phase

### finetune phase

----------------------------------------------------------------------------------------------

## both embs

### pretrain phase
`python3 ../OpenNMT-py/build_vocab.py --config nlngt_pt_both_vocab.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config nlngt_pt_both_run01.yaml --log_file tg-pretrain/nlngt_pt_both_run01.log`
`python3 ../OpenNMT-py/train.py --config nlngt_pt_both_run02.yaml --log_file tg-pretrain/nlngt_pt_both_run02.log`
`python3 ../OpenNMT-py/train.py --config nlngt_pt_both_run03.yaml --log_file tg-pretrain/nlngt_pt_both_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pretrain/tg-pretrain_01_step_${i}.pt -src nlngt_test_nl.txt -output tg-pretrain/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pretrain/tg-pretrain_02_step_${i}.pt -src nlngt_test_nl.txt -output tg-pretrain/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pretrain/tg-pretrain_03_step_${i}.pt -src nlngt_test_nl.txt -output tg-pretrain/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-pretrain/run01/* ngt/runs/tg-pretrain/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-pretrain/run02/* ngt/runs/tg-pretrain/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-pretrain/run03/* ngt/runs/tg-pretrain/run03`

`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-pretrain/run01`
`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-pretrain/run02`
`python calculate_metrics.py ~/Documents/corpora/NGT/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-pretrain/run03`

### finetune phase

----------------------------------------------------------------------------------------------
## STAGE 2 - Significance testing
----------------------------------------------------------------------------------------------