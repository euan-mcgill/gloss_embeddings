# Gloss2Text - NGT

----------------------------------------------------------------------------------------------
## STAGE 1 - Baseline
----------------------------------------------------------------------------------------------

`python3 ../OpenNMT-py/build_vocab.py --config ngtnl_run01.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config ngtnl_run01.yaml --log_file gt/ngtnl_run01.log`
`python3 ../OpenNMT-py/train.py --config ngtnl_run02.yaml --log_file gt/ngtnl_run02.log`
`python3 ../OpenNMT-py/train.py --config ngtnl_run03.yaml --log_file gt/ngtnl_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt/gt_01_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt/gt_02_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt/gt_03_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt/run01/* ngt/runs/gt/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt/run02/* ngt/runs/gt/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt/run03/* ngt/runs/gt/run03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt/run01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt/run02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt/run03 >> test.txt`

----------------------------------------------------------------------------------------------

## encoder embeddings

`python3 ../OpenNMT-py/build_vocab.py --config ngtnl_enc_run01.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config ngtnl_enc_run01.yaml --log_file gt/ngtnl_enc_run01.log`
`python3 ../OpenNMT-py/train.py --config ngtnl_enc_run02.yaml --log_file gt/ngtnl_enc_run02.log`
`python3 ../OpenNMT-py/train.py --config ngtnl_enc_run03.yaml --log_file gt/ngtnl_enc_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt/gt_01_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt/enc01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt/gt_02_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt/enc02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt/gt_03_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt/enc03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt/enc01/* ngt/runs/gt/enc01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt/enc02/* ngt/runs/gt/enc02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt/enc03/* ngt/runs/gt/enc03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt/enc01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt/enc02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt/enc03 >> test.txt`

----------------------------------------------------------------------------------------------

## decoder embeddings

`python3 ../OpenNMT-py/build_vocab.py --config ngtnl_dec_run01.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config ngtnl_dec_run01.yaml --log_file gt/ngtnl_dec_run01.log`
`python3 ../OpenNMT-py/train.py --config ngtnl_dec_run02.yaml --log_file gt/ngtnl_dec_run02.log`
`python3 ../OpenNMT-py/train.py --config ngtnl_dec_run03.yaml --log_file gt/ngtnl_dec_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt/gt_01_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt/dec01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt/gt_02_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt/dec02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt/gt_03_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt/dec03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt/dec01/* ngt/runs/gt/dec01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt/dec02/* ngt/runs/gt/dec02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt/dec03/* ngt/runs/gt/dec03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt/dec01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt/dec02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt/dec03 >> test.txt`

----------------------------------------------------------------------------------------------

## encoder + decoder embeddings

`python3 ../OpenNMT-py/build_vocab.py --config ngtnl_both_run01.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config ngtnl_both_run01.yaml --log_file gt/ngtnl_both_run01.log`
`python3 ../OpenNMT-py/train.py --config ngtnl_both_run02.yaml --log_file gt/ngtnl_both_run02.log`
`python3 ../OpenNMT-py/train.py --config ngtnl_both_run03.yaml --log_file gt/ngtnl_both_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt/gt_01_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt/both01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt/gt_02_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt/both02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt/gt_03_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt/both03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt/both01/* ngt/runs/gt/both01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt/both02/* ngt/runs/gt/both02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt/both03/* ngt/runs/gt/both03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt/both01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt/both02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt/both03 >> test.txt`

----------------------------------------------------------------------------------------------
## STAGE 2 - PT+FT
----------------------------------------------------------------------------------------------

### pretrain phase

`python3 ../OpenNMT-py/build_vocab.py --config ngtnl_pt_vocab.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config ngtnl_pt_run01.yaml --log_file gt-pretrain/ngtnl_pt_run01.log`
`python3 ../OpenNMT-py/train.py --config ngtnl_pt_run02.yaml --log_file gt-pretrain/ngtnl_pt_run02.log`
`python3 ../OpenNMT-py/train.py --config ngtnl_pt_run03.yaml --log_file gt-pretrain/ngtnl_pt_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-pretrain/gt-pretrain_01_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt-pretrain/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-pretrain/gt-pretrain_02_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt-pretrain/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-pretrain/gt-pretrain_03_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt-pretrain/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-pretrain/run01/* ngt/runs/gt-pretrain/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-pretrain/run02/* ngt/runs/gt-pretrain/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-pretrain/run03/* ngt/runs/gt-pretrain/run03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-pretrain/run01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-pretrain/run02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-pretrain/run03 >> test.txt`

### finetune phase

### run 1 @ 4600 epochs

`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_4600_run01.yaml --train_from gt-pretrain/models/gt-pretrain_01_step_4600.pt --reset_optim keep_states --log_file gt-finetune/ngtnl_ft_4600_run01.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_4600_run02.yaml --train_from gt-pretrain/models/gt-pretrain_01_step_4600.pt --reset_optim keep_states --log_file gt-finetune/ngtnl_ft_4600_run02.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_4600_run03.yaml --train_from gt-pretrain/models/gt-pretrain_01_step_4600.pt --reset_optim keep_states --log_file gt-finetune/ngtnl_ft_4600_run03.log`

`for ((i = 4800; i<= 9600; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-finetune/gt-finetune_4600_01_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-finetune/run01_01/step_${i}_pre_01.txt; done`
`for ((i = 4800; i<= 9600; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-finetune/gt-finetune_4600_02_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-finetune/run01_02/step_${i}_pre_02.txt; done`
`for ((i = 4800; i<= 9600; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-finetune/gt-finetune_4600_03_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-finetune/run01_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-finetune/run01_01/*.txt ngt/runs/gt-finetune/run01_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-finetune/run01_02/*.txt ngt/runs/gt-finetune/run01_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-finetune/run01_03/*.txt ngt/runs/gt-finetune/run01_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-finetune/run01_01 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-finetune/run01_02 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-finetune/run01_03 >> metrics.txt`

### run 2 @ 1600 epochs
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_1600_run01.yaml --train_from gt-pretrain/models/gt-pretrain_02_step_1600.pt --reset_optim keep_states --log_file gt-finetune/ngtnl_ft_1600_run01.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_1600_run02.yaml --train_from gt-pretrain/models/gt-pretrain_02_step_1600.pt --reset_optim keep_states --log_file gt-finetune/ngtnl_ft_1600_run02.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_1600_run03.yaml --train_from gt-pretrain/models/gt-pretrain_02_step_1600.pt --reset_optim keep_states --log_file gt-finetune/ngtnl_ft_1600_run03.log`

`for ((i = 1800; i<= 6600; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-finetune/gt-finetune_1600_01_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-finetune/run02_01/step_${i}_pre_01.txt; done`
`for ((i = 1800; i<= 6600; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-finetune/gt-finetune_1600_02_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-finetune/run02_02/step_${i}_pre_02.txt; done`
`for ((i = 1800; i<= 6600; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-finetune/gt-finetune_1600_03_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-finetune/run02_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-finetune/run02_01/*.txt ngt/runs/gt-finetune/run02_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-finetune/run02_02/*.txt ngt/runs/gt-finetune/run02_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-finetune/run02_03/*.txt ngt/runs/gt-finetune/run02_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-finetune/run02_01 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-finetune/run02_02 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-finetune/run02_03 >> metrics.txt`

### run 3 @ 6600 epochs
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_6600_run01.yaml --train_from gt-pretrain/models/gt-pretrain_03_step_6600.pt --reset_optim keep_states --log_file gt-finetune/ngtnl_ft_6600_run01.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_6600_run02.yaml --train_from gt-pretrain/models/gt-pretrain_03_step_6600.pt --reset_optim keep_states --log_file gt-finetune/ngtnl_ft_6600_run02.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_6600_run03.yaml --train_from gt-pretrain/models/gt-pretrain_03_step_6600.pt --reset_optim keep_states --log_file gt-finetune/ngtnl_ft_6600_run03.log`

`for ((i = 6800; i<= 11600; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-finetune/gt-finetune_6600_01_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-finetune/run03_01/step_${i}_pre_01.txt; done`
`for ((i = 6800; i<= 11600; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-finetune/gt-finetune_6600_02_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-finetune/run03_02/step_${i}_pre_02.txt; done`
`for ((i = 6800; i<= 11600; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-finetune/gt-finetune_6600_03_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-finetune/run03_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-finetune/run03_01/*.txt ngt/runs/gt-finetune/run03_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-finetune/run03_02/*.txt ngt/runs/gt-finetune/run03_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-finetune/run03_03/*.txt ngt/runs/gt-finetune/run03_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-finetune/run03_01 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-finetune/run03_02 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-finetune/run03_03 >> metrics.txt`

----------------------------------------------------------------------------------------------
## encoder embeddings

### pretrain phase

`python3 ../OpenNMT-py/build_vocab.py --config ngtnl_pt_enc_vocab.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config ngtnl_pt_enc_run01.yaml --log_file gt-pretrain/ngtnl_pt_enc_run01.log`
`python3 ../OpenNMT-py/train.py --config ngtnl_pt_enc_run02.yaml --log_file gt-pretrain/ngtnl_pt_enc_run02.log`
`python3 ../OpenNMT-py/train.py --config ngtnl_pt_enc_run03.yaml --log_file gt-pretrain/ngtnl_pt_enc_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-pretrain/gt-pretrain_01_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt-pretrain/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-pretrain/gt-pretrain_02_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt-pretrain/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-pretrain/gt-pretrain_03_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt-pretrain/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-pretrain/run01/* ngt/runs/gt-pretrain/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-pretrain/run02/* ngt/runs/gt-pretrain/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-pretrain/run03/* ngt/runs/gt-pretrain/run03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-pretrain/run01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-pretrain/run02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-pretrain/run03 >> test.txt`

### finetune phase

### run 1 @ 6400 epochs

`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_enc_6400_run01.yaml --train_from gt-pretrain/models/enc/gt-pretrain_01_step_6400.pt --reset_optim keep_states --log_file gt-ft-enc/ngtnl_ft_enc_6400_run01.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_enc_6400_run02.yaml --train_from gt-pretrain/models/enc/gt-pretrain_01_step_6400.pt --reset_optim keep_states --log_file gt-ft-enc/ngtnl_ft_enc_6400_run02.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_enc_6400_run03.yaml --train_from gt-pretrain/models/enc/gt-pretrain_01_step_6400.pt --reset_optim keep_states --log_file gt-ft-enc/ngtnl_ft_enc_6400_run03.log`

`for ((i = 6600; i<= 11400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-enc/gt-finetune_6400_01_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-enc/run01_01/step_${i}_pre_01.txt; done`
`for ((i = 6600; i<= 11400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-enc/gt-finetune_6400_02_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-enc/run01_02/step_${i}_pre_02.txt; done`
`for ((i = 6600; i<= 11400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-enc/gt-finetune_6400_03_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-enc/run01_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-enc/run01_01/*.txt ngt/runs/gt-ft-enc/run01_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-enc/run01_02/*.txt ngt/runs/gt-ft-enc/run01_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-enc/run01_03/*.txt ngt/runs/gt-ft-enc/run01_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-enc/run01_01 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-enc/run01_02 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-enc/run01_03 >> metrics.txt`

### run 2 @ 8000 epochs
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_enc_8000_run01.yaml --train_from gt-pretrain/models/enc/gt-pretrain_02_step_8000.pt --reset_optim keep_states --log_file gt-ft-enc/ngtnl_ft_enc_8000_run01.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_enc_8000_run02.yaml --train_from gt-pretrain/models/enc/gt-pretrain_02_step_8000.pt --reset_optim keep_states --log_file gt-ft-enc/ngtnl_ft_enc_8000_run02.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_enc_8000_run03.yaml --train_from gt-pretrain/models/enc/gt-pretrain_02_step_8000.pt --reset_optim keep_states --log_file gt-ft-enc/ngtnl_ft_enc_8000_run03.log`

`for ((i = 8200; i<= 13000; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-enc/gt-finetune_8000_01_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-enc/run02_01/step_${i}_pre_01.txt; done`
`for ((i = 8200; i<= 13000; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-enc/gt-finetune_8000_02_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-enc/run02_02/step_${i}_pre_02.txt; done`
`for ((i = 8200; i<= 13000; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-enc/gt-finetune_8000_03_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-enc/run02_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-enc/run02_01/*.txt ngt/runs/gt-ft-enc/run02_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-enc/run02_02/*.txt ngt/runs/gt-ft-enc/run02_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-enc/run02_03/*.txt ngt/runs/gt-ft-enc/run02_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-enc/run02_01 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-enc/run02_02 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-enc/run02_03 >> metrics.txt`

### run 3 @ 9200 epochs
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_enc_9200_run01.yaml --train_from gt-pretrain/models/enc/gt-pretrain_03_step_9200.pt --reset_optim keep_states --log_file gt-ft-enc/ngtnl_ft_enc_9200_run01.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_enc_9200_run02.yaml --train_from gt-pretrain/models/enc/gt-pretrain_03_step_9200.pt --reset_optim keep_states --log_file gt-ft-enc/ngtnl_ft_enc_9200_run02.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_enc_9200_run03.yaml --train_from gt-pretrain/models/enc/gt-pretrain_03_step_9200.pt --reset_optim keep_states --log_file gt-ft-enc/ngtnl_ft_enc_9200_run03.log`

`for ((i = 9400; i<= 14200; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-enc/gt-finetune_9200_01_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-enc/run03_01/step_${i}_pre_01.txt; done`
`for ((i = 9400; i<= 14200; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-enc/gt-finetune_9200_02_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-enc/run03_02/step_${i}_pre_02.txt; done`
`for ((i = 9400; i<= 14200; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-enc/gt-finetune_9200_03_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-enc/run03_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-enc/run03_01/*.txt ngt/runs/gt-ft-enc/run03_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-enc/run03_02/*.txt ngt/runs/gt-ft-enc/run03_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-enc/run03_03/*.txt ngt/runs/gt-ft-enc/run03_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-enc/run03_01 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-enc/run03_02 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-enc/run03_03 >> metrics.txt`

----------------------------------------------------------------------------------------------
## decoder embeddings

### pretrain phase

`python3 ../OpenNMT-py/build_vocab.py --config ngtnl_pt_dec_vocab.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config ngtnl_pt_dec_run01.yaml --log_file gt-pretrain/ngtnl_pt_dec_run01.log`
`python3 ../OpenNMT-py/train.py --config ngtnl_pt_dec_run02.yaml --log_file gt-pretrain/ngtnl_pt_dec_run02.log`
`python3 ../OpenNMT-py/train.py --config ngtnl_pt_dec_run03.yaml --log_file gt-pretrain/ngtnl_pt_dec_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-pretrain/gt-pretrain_01_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt-pretrain/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-pretrain/gt-pretrain_02_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt-pretrain/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-pretrain/gt-pretrain_03_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt-pretrain/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-pretrain/run01/* ngt/runs/gt-pretrain/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-pretrain/run02/* ngt/runs/gt-pretrain/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-pretrain/run03/* ngt/runs/gt-pretrain/run03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-pretrain/run01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-pretrain/run02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-pretrain/run03 >> test.txt`

### finetune phase

### run 1 @ 3800 epochs

`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_dec_3800_run01.yaml --train_from gt-pretrain/models/dec/gt-pretrain_01_step_3800.pt --reset_optim keep_states --log_file gt-ft-dec/ngtnl_ft_dec_3800_run01.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_dec_3800_run02.yaml --train_from gt-pretrain/models/dec/gt-pretrain_01_step_3800.pt --reset_optim keep_states --log_file gt-ft-dec/ngtnl_ft_dec_3800_run02.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_dec_3800_run03.yaml --train_from gt-pretrain/models/dec/gt-pretrain_01_step_3800.pt --reset_optim keep_states --log_file gt-ft-dec/ngtnl_ft_dec_3800_run03.log`

`for ((i = 4000; i<= 8800; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-dec/gt-finetune_3800_01_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-dec/run01_01/step_${i}_pre_01.txt; done`
`for ((i = 4000; i<= 8800; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-dec/gt-finetune_3800_02_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-dec/run01_02/step_${i}_pre_02.txt; done`
`for ((i = 4000; i<= 8800; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-dec/gt-finetune_3800_03_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-dec/run01_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-dec/run01_01/*.txt ngt/runs/gt-ft-dec/run01_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-dec/run01_02/*.txt ngt/runs/gt-ft-dec/run01_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-dec/run01_03/*.txt ngt/runs/gt-ft-dec/run01_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-dec/run01_01 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-dec/run01_02 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-dec/run01_03 >> metrics.txt`

### run 2 @ 5200 epochs
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_dec_5200_run01.yaml --train_from gt-pretrain/models/dec/gt-pretrain_02_step_5200.pt --reset_optim keep_states --log_file gt-ft-dec/ngtnl_ft_dec_5200_run01.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_dec_5200_run02.yaml --train_from gt-pretrain/models/dec/gt-pretrain_02_step_5200.pt --reset_optim keep_states --log_file gt-ft-dec/ngtnl_ft_dec_5200_run02.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_dec_5200_run03.yaml --train_from gt-pretrain/models/dec/gt-pretrain_02_step_5200.pt --reset_optim keep_states --log_file gt-ft-dec/ngtnl_ft_dec_5200_run03.log`

`for ((i = 5400; i<= 10200; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-dec/gt-finetune_5200_01_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-dec/run02_01/step_${i}_pre_01.txt; done`
`for ((i = 5400; i<= 10200; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-dec/gt-finetune_5200_02_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-dec/run02_02/step_${i}_pre_02.txt; done`
`for ((i = 5400; i<= 10200; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-dec/gt-finetune_5200_03_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-dec/run02_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-dec/run02_01/*.txt ngt/runs/gt-ft-dec/run02_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-dec/run02_02/*.txt ngt/runs/gt-ft-dec/run02_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-dec/run02_03/*.txt ngt/runs/gt-ft-dec/run02_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-dec/run02_01 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-dec/run02_02 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-dec/run02_03 >> metrics.txt`

### run 3 @ 2400 epochs
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_dec_2400_run01.yaml --train_from gt-pretrain/models/dec/gt-pretrain_03_step_2400.pt --reset_optim keep_states --log_file gt-ft-dec/ngtnl_ft_dec_2400_run01.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_dec_2400_run02.yaml --train_from gt-pretrain/models/dec/gt-pretrain_03_step_2400.pt --reset_optim keep_states --log_file gt-ft-dec/ngtnl_ft_dec_2400_run02.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_dec_2400_run03.yaml --train_from gt-pretrain/models/dec/gt-pretrain_03_step_2400.pt --reset_optim keep_states --log_file gt-ft-dec/ngtnl_ft_dec_2400_run03.log`

`for ((i = 2600; i<= 7400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-dec/gt-finetune_2400_01_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-dec/run03_01/step_${i}_pre_01.txt; done`
`for ((i = 2600; i<= 7400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-dec/gt-finetune_2400_02_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-dec/run03_02/step_${i}_pre_02.txt; done`
`for ((i = 2600; i<= 7400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-dec/gt-finetune_2400_03_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-dec/run03_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-dec/run03_01/*.txt ngt/runs/gt-ft-dec/run03_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-dec/run03_02/*.txt ngt/runs/gt-ft-dec/run03_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-dec/run03_03/*.txt ngt/runs/gt-ft-dec/run03_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-dec/run03_01 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-dec/run03_02 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-dec/run03_03 >> metrics.txt`

----------------------------------------------------------------------------------------------
## encoder + decoder embeddings

### pretrain phase

`python3 ../OpenNMT-py/build_vocab.py --config ngtnl_pt_both_vocab.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config ngtnl_pt_both_run01.yaml --log_file gt-pretrain/ngtnl_pt_both_run01.log`
`python3 ../OpenNMT-py/train.py --config ngtnl_pt_both_run02.yaml --log_file gt-pretrain/ngtnl_pt_both_run02.log`
`python3 ../OpenNMT-py/train.py --config ngtnl_pt_both_run03.yaml --log_file gt-pretrain/ngtnl_pt_both_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-pretrain/gt-pretrain_01_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt-pretrain/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-pretrain/gt-pretrain_02_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt-pretrain/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-pretrain/gt-pretrain_03_step_${i}.pt -src nlngt_test_gloss_lower.txt -output gt-pretrain/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-pretrain/run01/* ngt/runs/gt-pretrain/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-pretrain/run02/* ngt/runs/gt-pretrain/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-pretrain/run03/* ngt/runs/gt-pretrain/run03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-pretrain/run01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-pretrain/run02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-pretrain/run03 >> test.txt`

### finetune phase

### run 1 @ 8400 epochs

`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_both_8400_run01.yaml --train_from gt-pretrain/models/both/gt-pretrain_01_step_8400.pt --reset_optim keep_states --log_file gt-ft-both/ngtnl_ft_both_8400_run01.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_both_8400_run02.yaml --train_from gt-pretrain/models/both/gt-pretrain_01_step_8400.pt --reset_optim keep_states --log_file gt-ft-both/ngtnl_ft_both_8400_run02.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_both_8400_run03.yaml --train_from gt-pretrain/models/both/gt-pretrain_01_step_8400.pt --reset_optim keep_states --log_file gt-ft-both/ngtnl_ft_both_8400_run03.log`

`for ((i = 8600; i<= 13400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-both/gt-finetune_8400_01_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-both/run01_01/step_${i}_pre_01.txt; done`
`for ((i = 8600; i<= 13400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-both/gt-finetune_8400_02_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-both/run01_02/step_${i}_pre_02.txt; done`
`for ((i = 8600; i<= 13400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-both/gt-finetune_8400_03_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-both/run01_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-both/run01_01/*.txt ngt/runs/gt-ft-both/run01_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-both/run01_02/*.txt ngt/runs/gt-ft-both/run01_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-both/run01_03/*.txt ngt/runs/gt-ft-both/run01_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-both/run01_01 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-both/run01_02 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-both/run01_03 >> metrics.txt`

### run 2 @ 1600 epochs
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_both_1600_run01.yaml --train_from gt-pretrain/models/both/gt-pretrain_02_step_1600.pt --reset_optim keep_states --log_file gt-ft-both/ngtnl_ft_both_1600_run01.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_both_1600_run02.yaml --train_from gt-pretrain/models/both/gt-pretrain_02_step_1600.pt --reset_optim keep_states --log_file gt-ft-both/ngtnl_ft_both_1600_run02.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_both_1600_run03.yaml --train_from gt-pretrain/models/both/gt-pretrain_02_step_1600.pt --reset_optim keep_states --log_file gt-ft-both/ngtnl_ft_both_1600_run03.log`

`for ((i = 1800; i<= 6600; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-both/gt-finetune_1600_01_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-both/run02_01/step_${i}_pre_01.txt; done`
`for ((i = 1800; i<= 6600; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-both/gt-finetune_1600_02_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-both/run02_02/step_${i}_pre_02.txt; done`
`for ((i = 1800; i<= 6600; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-both/gt-finetune_1600_03_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-both/run02_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-both/run02_01/*.txt ngt/runs/gt-ft-both/run02_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-both/run02_02/*.txt ngt/runs/gt-ft-both/run02_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-both/run02_03/*.txt ngt/runs/gt-ft-both/run02_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-both/run02_01 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-both/run02_02 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-both/run02_03 >> metrics.txt`

### run 3 @ 8400 epochs
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_both_8400_run01.yaml --train_from gt-pretrain/models/both/gt-pretrain_03_step_8400.pt --reset_optim keep_states --log_file gt-ft-both/ngtnl_ft_both_2400_run01.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_both_8400_run02.yaml --train_from gt-pretrain/models/both/gt-pretrain_03_step_8400.pt --reset_optim keep_states --log_file gt-ft-both/ngtnl_ft_both_2400_run02.log`
`python3 ../OpenNMT-py/train.py --config  ngtnl_ft_both_8400_run03.yaml --train_from gt-pretrain/models/both/gt-pretrain_03_step_8400.pt --reset_optim keep_states --log_file gt-ft-both/ngtnl_ft_both_2400_run03.log`

`for ((i = 8600; i<= 13400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-both/gt-finetune_8400_01_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-both/run03_01/step_${i}_pre_01.txt; done`
`for ((i = 8600; i<= 13400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-both/gt-finetune_8400_02_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-both/run03_02/step_${i}_pre_02.txt; done`
`for ((i = 8600; i<= 13400; i += 200)); do  python3 ../OpenNMT-py/translate.py -model gt-ft-both/gt-finetune_8400_03_step_${i}.pt --ban_unk_token -src nlngt_test_gloss_lower.txt -output gt-ft-both/run03_03/step_${i}_pre_03.txt; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-both/run03_01/*.txt ngt/runs/gt-ft-both/run03_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-both/run03_02/*.txt ngt/runs/gt-ft-both/run03_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:ngt_exps/gt-ft-both/run03_03/*.txt ngt/runs/gt-ft-both/run03_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-both/run03_01 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-both/run03_02 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/ngt/data/CorpusNGT/nlngt_test_nl.txt -d ngt/runs/gt-ft-both/run03_03 >> metrics.txt`
