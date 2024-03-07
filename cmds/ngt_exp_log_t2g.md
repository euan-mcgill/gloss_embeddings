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

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg/run01`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg/run02`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg/run03`

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

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-enc/run01`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-enc/run02`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-enc/run03`

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

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-dec/run01`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-dec/run02`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-dec/run03`

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

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-both/run01`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-both/run02`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-both/run03`

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

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-pretrain/run01`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-pretrain/run02`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-pretrain/run03`

### finetune phase

### run 1 @ 9800 epochs

`python3 ../OpenNMT-py/train.py --config  nlngt_ft_9800_run01.yaml --train_from tg-pretrain/models/tg-pretrain_01_step_9800.pt --reset_optim keep_states --log_file tg-finetune/nlngt_ft_9800_run01.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_9800_run02.yaml --train_from tg-pretrain/models/tg-pretrain_01_step_9800.pt --reset_optim keep_states --log_file tg-finetune/nlngt_ft_9800_run02.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_9800_run03.yaml --train_from tg-pretrain/models/tg-pretrain_01_step_9800.pt --reset_optim keep_states --log_file tg-finetune/nlngt_ft_9800_run03.log`

`for ((i = 10000; i<= 14800; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_9800_01_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-finetune/run01_01/step_${i}_pre_01.txt; done`
`for ((i = 10000; i<= 14800; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_9800_02_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-finetune/run01_02/step_${i}_pre_02.txt; done`
`for ((i = 10000; i<= 14800; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_9800_03_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-finetune/run01_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-finetune/run01_01/*.txt ngt/runs/tg-finetune/run01_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-finetune/run01_02/*.txt ngt/runs/tg-finetune/run01_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-finetune/run01_03/*.txt ngt/runs/tg-finetune/run01_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-finetune/run01_01`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-finetune/run01_02`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-finetune/run01_03`

### run 2 @ 5200 epochs

`python3 ../OpenNMT-py/train.py --config  nlngt_ft_5200_run01.yaml --train_from tg-pretrain/models/tg-pretrain_02_step_5200.pt --reset_optim keep_states --log_file tg-finetune/nlngt_ft_5200_run01.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_5200_run02.yaml --train_from tg-pretrain/models/tg-pretrain_02_step_5200.pt --reset_optim keep_states --log_file tg-finetune/nlngt_ft_5200_run02.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_5200_run03.yaml --train_from tg-pretrain/models/tg-pretrain_02_step_5200.pt --reset_optim keep_states --log_file tg-finetune/nlngt_ft_5200_run03.log`

`for ((i = 5400; i<= 10200; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_5200_01_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-finetune/run02_01/step_${i}_pre_01.txt; done`
`for ((i = 5400; i<= 10200; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_5200_02_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-finetune/run02_02/step_${i}_pre_02.txt; done`
`for ((i = 5400; i<= 10200; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_5200_03_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-finetune/run02_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-finetune/run02_01/*.txt ngt/runs/tg-finetune/run02_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-finetune/run02_02/*.txt ngt/runs/tg-finetune/run02_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-finetune/run02_03/*.txt ngt/runs/tg-finetune/run02_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-finetune/run02_01`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-finetune/run02_02`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-finetune/run02_03`

### run 3 @ 9200 epochs

`python3 ../OpenNMT-py/train.py --config  nlngt_ft_9200_run01.yaml --train_from tg-pretrain/models/tg-pretrain_03_step_9200.pt --reset_optim keep_states --log_file tg-finetune/nlngt_ft_9200_run01.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_9200_run02.yaml --train_from tg-pretrain/models/tg-pretrain_03_step_9200.pt --reset_optim keep_states --log_file tg-finetune/nlngt_ft_9200_run02.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_9200_run03.yaml --train_from tg-pretrain/models/tg-pretrain_03_step_9200.pt --reset_optim keep_states --log_file tg-finetune/nlngt_ft_9200_run03.log`

`for ((i = 9400; i<= 14200; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_9200_01_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-finetune/run03_01/step_${i}_pre_01.txt; done`
`for ((i = 9400; i<= 14200; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_9200_02_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-finetune/run03_02/step_${i}_pre_02.txt; done`
`for ((i = 9400; i<= 14200; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_9200_03_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-finetune/run03_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-finetune/run03_01/*.txt ngt/runs/tg-finetune/run03_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-finetune/run03_02/*.txt ngt/runs/tg-finetune/run03_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-finetune/run03_03/*.txt ngt/runs/tg-finetune/run03_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-finetune/run03_01`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-finetune/run03_02`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-finetune/run03_03`

----------------------------------------------------------------------------------------------
## STAGE 2a - PT+FT + embs
----------------------------------------------------------------------------------------------

## encoder embs

### pretrain phase
`python3 ../OpenNMT-py/build_vocab.py --config nlngt_pt_enc_vocab.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config nlngt_pt_enc_run01.yaml --log_file tg-pretrain/nlngt_pt_enc_run01.log`
`python3 ../OpenNMT-py/train.py --config nlngt_pt_enc_run02.yaml --log_file tg-pretrain/nlngt_pt_enc_run02.log`
`python3 ../OpenNMT-py/train.py --config nlngt_pt_enc_run03.yaml --log_file tg-pretrain/nlngt_pt_enc_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pretrain/tg-pretrain_01_step_${i}.pt -src nlngt_test_nl.txt -output tg-pretrain/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pretrain/tg-pretrain_02_step_${i}.pt -src nlngt_test_nl.txt -output tg-pretrain/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pretrain/tg-pretrain_03_step_${i}.pt -src nlngt_test_nl.txt -output tg-pretrain/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-pretrain/run01/* ngt/runs/tg-pretrain/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-pretrain/run02/* ngt/runs/tg-pretrain/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-pretrain/run03/* ngt/runs/tg-pretrain/run03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-pretrain/run01`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-pretrain/run02`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-pretrain/run03`

### finetune phase

### run 1 @ 10000 epochs

`python3 ../OpenNMT-py/train.py --config  nlngt_ft_enc_10000_run01.yaml --train_from tg-pretrain/models/enc/tg-pretrain_01_step_10000.pt --reset_optim keep_states --log_file tg-ft-enc/nlngt_ft_enc_10000_run01.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_enc_10000_run02.yaml --train_from tg-pretrain/models/enc/tg-pretrain_01_step_10000.pt --reset_optim keep_states --log_file tg-ft-enc/nlngt_ft_enc_10000_run02.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_enc_10000_run03.yaml --train_from tg-pretrain/models/enc/tg-pretrain_01_step_10000.pt --reset_optim keep_states --log_file tg-ft-enc/nlngt_ft_enc_10000_run03.log`

`for ((i = 10200; i<= 15000; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-enc/tg-finetune_10000_01_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-enc/run01_01/step_${i}_pre_01.txt; done`
`for ((i = 10200; i<= 15000; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-enc/tg-finetune_10000_02_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-enc/run01_02/step_${i}_pre_02.txt; done`
`for ((i = 10200; i<= 15000; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-enc/tg-finetune_10000_03_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-enc/run01_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-enc/run01_01/*.txt ngt/runs/tg-ft-enc/run01_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-enc/run01_02/*.txt ngt/runs/tg-ft-enc/run01_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-enc/run01_03/*.txt ngt/runs/tg-ft-enc/run01_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-enc/run01_01`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-enc/run01_02`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-enc/run01_03`

### run 2 @ 9400 epochs

`python3 ../OpenNMT-py/train.py --config  nlngt_ft_enc_9400_run01.yaml --train_from tg-pretrain/models/enc/tg-pretrain_02_step_9400.pt --reset_optim keep_states --log_file tg-ft-enc/nlngt_ft_enc_9400_run01.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_enc_9400_run02.yaml --train_from tg-pretrain/models/enc/tg-pretrain_02_step_9400.pt --reset_optim keep_states --log_file tg-ft-enc/nlngt_ft_enc_9400_run02.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_enc_9400_run03.yaml --train_from tg-pretrain/models/enc/tg-pretrain_02_step_9400.pt --reset_optim keep_states --log_file tg-ft-enc/nlngt_ft_enc_9400_run03.log`

`for ((i = 9600; i<= 14400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-enc/tg-finetune_9400_01_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-enc/run02_01/step_${i}_pre_01.txt; done`
`for ((i = 9600; i<= 14400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-enc/tg-finetune_9400_02_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-enc/run02_02/step_${i}_pre_02.txt; done`
`for ((i = 9600; i<= 14400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-enc/tg-finetune_9400_03_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-enc/run02_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-enc/run02_01/*.txt ngt/runs/tg-ft-enc/run02_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-enc/run02_02/*.txt ngt/runs/tg-ft-enc/run02_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-enc/run02_03/*.txt ngt/runs/tg-ft-enc/run02_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-enc/run02_01`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-enc/run02_02`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-enc/run02_03`

### run 3 @ 9800 epochs

`python3 ../OpenNMT-py/train.py --config  nlngt_ft_enc_9800_run01.yaml --train_from tg-pretrain/models/enc/tg-pretrain_03_step_9800.pt --reset_optim keep_states --log_file tg-ft-enc/nlngt_ft_enc_9800_run01.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_enc_9800_run02.yaml --train_from tg-pretrain/models/enc/tg-pretrain_03_step_9800.pt --reset_optim keep_states --log_file tg-ft-enc/nlngt_ft_enc_9800_run02.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_enc_9800_run03.yaml --train_from tg-pretrain/models/enc/tg-pretrain_03_step_9800.pt --reset_optim keep_states --log_file tg-ft-enc/nlngt_ft_enc_9800_run03.log`

`for ((i = 10000; i<= 14800; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-enc/tg-finetune_9800_01_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-enc/run03_01/step_${i}_pre_01.txt; done`
`for ((i = 10000; i<= 14800; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-enc/tg-finetune_9800_02_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-enc/run03_02/step_${i}_pre_02.txt; done`
`for ((i = 10000; i<= 14800; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-enc/tg-finetune_9800_03_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-enc/run03_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-enc/run03_01/*.txt ngt/runs/tg-ft-enc/run03_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-enc/run03_02/*.txt ngt/runs/tg-ft-enc/run03_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-enc/run03_03/*.txt ngt/runs/tg-ft-enc/run03_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-enc/run03_01`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-enc/run03_02`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-enc/run03_03`

----------------------------------------------------------------------------------------------

## decoder embs

### pretrain phase
`python3 ../OpenNMT-py/build_vocab.py --config nlngt_pt_dec_vocab.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config nlngt_pt_dec_run01.yaml --log_file tg-pretrain/nlngt_pt_dec_run01.log`
`python3 ../OpenNMT-py/train.py --config nlngt_pt_dec_run02.yaml --log_file tg-pretrain/nlngt_pt_dec_run02.log`
`python3 ../OpenNMT-py/train.py --config nlngt_pt_dec_run03.yaml --log_file tg-pretrain/nlngt_pt_dec_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pretrain/tg-pretrain_01_step_${i}.pt -src nlngt_test_nl.txt -output tg-pretrain/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pretrain/tg-pretrain_02_step_${i}.pt -src nlngt_test_nl.txt -output tg-pretrain/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pretrain/tg-pretrain_03_step_${i}.pt -src nlngt_test_nl.txt -output tg-pretrain/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-pretrain/run01/* ngt/runs/tg-pretrain/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-pretrain/run02/* ngt/runs/tg-pretrain/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-pretrain/run03/* ngt/runs/tg-pretrain/run03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-pretrain/run01`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-pretrain/run02`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-pretrain/run03`

### finetune phase

### run 1 @ 6400 epochs

`python3 ../OpenNMT-py/train.py --config  nlngt_ft_dec_6400_run01.yaml --train_from tg-pretrain/models/dec/tg-pretrain_01_step_6400.pt --reset_optim keep_states --log_file tg-ft-dec/nlngt_ft_dec_6400_run01.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_dec_6400_run02.yaml --train_from tg-pretrain/models/dec/tg-pretrain_01_step_6400.pt --reset_optim keep_states --log_file tg-ft-dec/nlngt_ft_dec_6400_run02.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_dec_6400_run03.yaml --train_from tg-pretrain/models/dec/tg-pretrain_01_step_6400.pt --reset_optim keep_states --log_file tg-ft-dec/nlngt_ft_dec_6400_run03.log`

`for ((i = 6600; i<= 11400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-dec/tg-finetune_6400_01_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-dec/run01_01/step_${i}_pre_01.txt; done`
`for ((i = 6600; i<= 11400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-dec/tg-finetune_6400_02_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-dec/run01_02/step_${i}_pre_02.txt; done`
`for ((i = 6600; i<= 11400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-dec/tg-finetune_6400_03_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-dec/run01_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-dec/run01_01/*.txt ngt/runs/tg-ft-dec/run01_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-dec/run01_02/*.txt ngt/runs/tg-ft-dec/run01_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-dec/run01_03/*.txt ngt/runs/tg-ft-dec/run01_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-dec/run01_01`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-dec/run01_02`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-dec/run01_03`

### run 2 @ 6200 epochs

`python3 ../OpenNMT-py/train.py --config  nlngt_ft_dec_6200_run01.yaml --train_from tg-pretrain/models/dec/tg-pretrain_02_step_6200.pt --reset_optim keep_states --log_file tg-ft-dec/nlngt_ft_dec_6200_run01.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_dec_6200_run02.yaml --train_from tg-pretrain/models/dec/tg-pretrain_02_step_6200.pt --reset_optim keep_states --log_file tg-ft-dec/nlngt_ft_dec_6200_run02.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_dec_6200_run03.yaml --train_from tg-pretrain/models/dec/tg-pretrain_02_step_6200.pt --reset_optim keep_states --log_file tg-ft-dec/nlngt_ft_dec_6200_run03.log`

`for ((i = 6400; i<= 11200; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-dec/tg-finetune_6200_01_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-dec/run02_01/step_${i}_pre_01.txt; done`
`for ((i = 6400; i<= 11200; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-dec/tg-finetune_6200_02_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-dec/run02_02/step_${i}_pre_02.txt; done`
`for ((i = 6400; i<= 11200; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-dec/tg-finetune_6200_03_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-dec/run02_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-dec/run02_01/*.txt ngt/runs/tg-ft-dec/run02_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-dec/run02_02/*.txt ngt/runs/tg-ft-dec/run02_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-dec/run02_03/*.txt ngt/runs/tg-ft-dec/run02_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-dec/run02_01`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-dec/run02_02`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-dec/run02_03`

### run 3 @ 10000 epochs

`python3 ../OpenNMT-py/train.py --config  nlngt_ft_dec_10000_run01.yaml --train_from tg-pretrain/models/dec/tg-pretrain_03_step_10000.pt --reset_optim keep_states --log_file tg-ft-dec/nlngt_ft_dec_10000_run01.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_dec_10000_run02.yaml --train_from tg-pretrain/models/dec/tg-pretrain_03_step_10000.pt --reset_optim keep_states --log_file tg-ft-dec/nlngt_ft_dec_10000_run02.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_dec_10000_run03.yaml --train_from tg-pretrain/models/dec/tg-pretrain_03_step_10000.pt --reset_optim keep_states --log_file tg-ft-dec/nlngt_ft_dec_10000_run03.log`

`for ((i = 10200; i<= 15000; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-dec/tg-finetune_10000_01_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-dec/run03_01/step_${i}_pre_01.txt; done`
`for ((i = 10200; i<= 15000; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-dec/tg-finetune_10000_02_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-dec/run03_02/step_${i}_pre_02.txt; done`
`for ((i = 10200; i<= 15000; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-dec/tg-finetune_10000_03_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-dec/run03_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-dec/run03_01/*.txt ngt/runs/tg-ft-dec/run03_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-dec/run03_02/*.txt ngt/runs/tg-ft-dec/run03_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-dec/run03_03/*.txt ngt/runs/tg-ft-dec/run03_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-dec/run03_01`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-dec/run03_02`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-dec/run03_03`

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

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-pretrain/run01`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-pretrain/run02`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-pretrain/run03`

### finetune phase

### run 1 @ 6400 epochs

`python3 ../OpenNMT-py/train.py --config  nlngt_ft_both_6400_run01.yaml --train_from tg-pretrain/models/both/tg-pretrain_01_step_6400.pt --reset_optim keep_states --log_file tg-ft-both/nlngt_ft_both_6400_run01.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_both_6400_run02.yaml --train_from tg-pretrain/models/both/tg-pretrain_01_step_6400.pt --reset_optim keep_states --log_file tg-ft-both/nlngt_ft_both_6400_run02.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_both_6400_run03.yaml --train_from tg-pretrain/models/both/tg-pretrain_01_step_6400.pt --reset_optim keep_states --log_file tg-ft-both/nlngt_ft_both_6400_run03.log`

`for ((i = 6600; i<= 11400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-both/tg-finetune_6400_01_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-both/run01_01/step_${i}_pre_01.txt; done`
`for ((i = 6600; i<= 11400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-both/tg-finetune_6400_02_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-both/run01_02/step_${i}_pre_02.txt; done`
`for ((i = 6600; i<= 11400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-both/tg-finetune_6400_03_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-both/run01_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-both/run01_01/*.txt ngt/runs/tg-ft-both/run01_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-both/run01_02/*.txt ngt/runs/tg-ft-both/run01_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-both/run01_03/*.txt ngt/runs/tg-ft-both/run01_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-both/run01_01`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-both/run01_02`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-both/run01_03`

### run 2 @ 6800 epochs

`python3 ../OpenNMT-py/train.py --config  nlngt_ft_both_6800_run01.yaml --train_from tg-pretrain/models/both/tg-pretrain_02_step_6800.pt --reset_optim keep_states --log_file tg-ft-both/nlngt_ft_both_6800_run01.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_both_6800_run02.yaml --train_from tg-pretrain/models/both/tg-pretrain_02_step_6800.pt --reset_optim keep_states --log_file tg-ft-both/nlngt_ft_both_6800_run02.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_both_6800_run03.yaml --train_from tg-pretrain/models/both/tg-pretrain_02_step_6800.pt --reset_optim keep_states --log_file tg-ft-both/nlngt_ft_both_6800_run03.log`

`for ((i = 7000; i<= 11800; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-both/tg-finetune_6800_01_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-both/run02_01/step_${i}_pre_01.txt; done`
`for ((i = 7000; i<= 11800; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-both/tg-finetune_6800_02_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-both/run02_02/step_${i}_pre_02.txt; done`
`for ((i = 7000; i<= 11800; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-both/tg-finetune_6800_03_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-both/run02_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-both/run02_01/*.txt ngt/runs/tg-ft-both/run02_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-both/run02_02/*.txt ngt/runs/tg-ft-both/run02_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-both/run02_03/*.txt ngt/runs/tg-ft-both/run02_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-both/run02_01`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-both/run02_02`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-both/run02_03`

### run 3 @ 8800 epochs

`python3 ../OpenNMT-py/train.py --config  nlngt_ft_both_8800_run01.yaml --train_from tg-pretrain/models/both/tg-pretrain_03_step_8800.pt --reset_optim keep_states --log_file tg-ft-both/nlngt_ft_both_8800_run01.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_both_8800_run02.yaml --train_from tg-pretrain/models/both/tg-pretrain_03_step_8800.pt --reset_optim keep_states --log_file tg-ft-both/nlngt_ft_both_8800_run02.log`
`python3 ../OpenNMT-py/train.py --config  nlngt_ft_both_8800_run03.yaml --train_from tg-pretrain/models/both/tg-pretrain_03_step_8800.pt --reset_optim keep_states --log_file tg-ft-both/nlngt_ft_both_8800_run03.log`

`for ((i = 9000; i<= 13800; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-both/tg-finetune_8800_01_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-both/run03_01/step_${i}_pre_01.txt; done`
`for ((i = 9000; i<= 13800; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-both/tg-finetune_8800_02_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-both/run03_02/step_${i}_pre_02.txt; done`
`for ((i = 9000; i<= 13800; i += 200)); do  python3 ../OpenNMT-py/translate.py -model tg-ft-both/tg-finetune_8800_03_step_${i}.pt --ban_unk_token -src nlngt_test_nl.txt -output tg-ft-both/run03_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-both/run03_01/*.txt ngt/runs/tg-ft-both/run03_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-both/run03_02/*.txt ngt/runs/tg-ft-both/run03_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/tg-ft-both/run03_03/*.txt ngt/runs/tg-ft-both/run03_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-both/run03_01`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-both/run03_02`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_gloss_lower.txt -d ngt/runs/tg-ft-both/run03_03`

----------------------------------------------------------------------------------------------
## STAGE 3 - Significance testing
----------------------------------------------------------------------------------------------


