# Gloss2Text - ASL

----------------------------------------------------------------------------------------------
## STAGE 1 - Baseline
----------------------------------------------------------------------------------------------

`python3 ../OpenNMT-py/build_vocab.py --config aslen_run01.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config aslen_run01.yaml --log_file gt/aslen_run01.log`
`python3 ../OpenNMT-py/train.py --config aslen_run02.yaml --log_file gt/aslen_run02.log`
`python3 ../OpenNMT-py/train.py --config aslen_run03.yaml --log_file gt/aslen_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt/gt_01_step_${i}.pt -src asl_test.txt -output gt/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt/gt_02_step_${i}.pt -src asl_test.txt -output gt/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt/gt_03_step_${i}.pt -src asl_test.txt -output gt/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt/run01/* asl/runs/gt/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt/run02/* asl/runs/gt/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt/run03/* asl/runs/gt/run03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt/run01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt/run02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt/run03 >> test.txt`

----------------------------------------------------------------------------------------------

## encoder embeddings

`python3 ../OpenNMT-py/build_vocab.py --config aslen_enc_run01.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config aslen_enc_run01.yaml --log_file gt-enc/aslen_enc_run01.log`
`python3 ../OpenNMT-py/train.py --config aslen_enc_run02.yaml --log_file gt-enc/aslen_enc_run02.log`
`python3 ../OpenNMT-py/train.py --config aslen_enc_run03.yaml --log_file gt-enc/aslen_enc_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-enc/gt_01_step_${i}.pt -src asl_test.txt -output gt-enc/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-enc/gt_02_step_${i}.pt -src asl_test.txt -output gt-enc/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-enc/gt_03_step_${i}.pt -src asl_test.txt -output gt-enc/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt-enc/run01/* asl/runs/gt-enc/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt-enc/run02/* asl/runs/gt-enc/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt-enc/run03/* asl/runs/gt-enc/run03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt-enc/run01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt-enc/run02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt-enc/run03 >> test.txt`

----------------------------------------------------------------------------------------------

## decoder embeddings

`python3 ../OpenNMT-py/build_vocab.py --config aslen_dec_run01.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config aslen_dec_run01.yaml --log_file gt-dec/aslen_dec_run01.log`
`python3 ../OpenNMT-py/train.py --config aslen_dec_run02.yaml --log_file gt-dec/aslen_dec_run02.log`
`python3 ../OpenNMT-py/train.py --config aslen_dec_run03.yaml --log_file gt-dec/aslen_dec_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-dec/gt_01_step_${i}.pt -src asl_test.txt -output gt-dec/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-dec/gt_02_step_${i}.pt -src asl_test.txt -output gt-dec/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-dec/gt_03_step_${i}.pt -src asl_test.txt -output gt-dec/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt-dec/run01/* asl/runs/gt-dec/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt-dec/run02/* asl/runs/gt-dec/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt-dec/run03/* asl/runs/gt-dec/run03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt-dec/run01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt-dec/run02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt-dec/run03 >> test.txt`

----------------------------------------------------------------------------------------------

## encoder + decoder embeddings

`python3 ../OpenNMT-py/build_vocab.py --config aslen_both_run01.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config aslen_both_run01.yaml --log_file gt-both/aslen_both_run01.log`
`python3 ../OpenNMT-py/train.py --config aslen_both_run02.yaml --log_file gt-both/aslen_both_run02.log`
`python3 ../OpenNMT-py/train.py --config aslen_both_run03.yaml --log_file gt-both/aslen_both_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-both/gt_01_step_${i}.pt -src asl_test.txt -output gt-both/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-both/gt_02_step_${i}.pt -src asl_test.txt -output gt-both/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-both/gt_03_step_${i}.pt -src asl_test.txt -output gt-both/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt-both/run01/* asl/runs/gt-both/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt-both/run02/* asl/runs/gt-both/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt-both/run03/* asl/runs/gt-both/run03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt-both/run01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt-both/run02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt-both/run03 >> test.txt`

----------------------------------------------------------------------------------------------
## STAGE 2 - PT+FT
----------------------------------------------------------------------------------------------

### pretrain phase

`python3 ../OpenNMT-py/build_vocab.py --config aslen_pt_vocab.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config aslen_pt_run01.yaml --log_file gt-pretrain/aslen_pt_run01.log`
`python3 ../OpenNMT-py/train.py --config aslen_pt_run02.yaml --log_file gt-pretrain/aslen_pt_run02.log`
`python3 ../OpenNMT-py/train.py --config aslen_pt_run03.yaml --log_file gt-pretrain/aslen_pt_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-pretrain/gt-pretrain_01_step_${i}.pt -src asl_test.txt -output gt-pretrain/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-pretrain/gt-pretrain_02_step_${i}.pt -src asl_test.txt -output gt-pretrain/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model gt-pretrain/gt-pretrain_03_step_${i}.pt -src asl_test.txt -output gt-pretrain/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt-pretrain/run01/* asl/runs/gt-pretrain/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt-pretrain/run02/* asl/runs/gt-pretrain/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt-pretrain/run03/* asl/runs/gt-pretrain/run03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt-pretrain/run01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt-pretrain/run02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt-pretrain/run03 >> test.txt`

### finetune phase

### run01 @ 8200 epochs
`python3 ../OpenNMT-py/train.py --config aslen_ft_8200_run01.yaml --train_from gt-pretrain/models/gt-pretrain_01_step_8200.pt --reset_optim keep_states --log_file gt-pretrain/aslen_ft_8200_run01.log`
`python3 ../OpenNMT-py/train.py --config aslen_ft_8200_run02.yaml --train_from gt-pretrain/models/gt-pretrain_01_step_8200.pt --reset_optim keep_states --log_file gt-pretrain/aslen_ft_8200_run02.log`
`python3 ../OpenNMT-py/train.py --config aslen_ft_8200_run03.yaml --train_from gt-pretrain/models/gt-pretrain_01_step_8200.pt --reset_optim keep_states --log_file gt-pretrain/aslen_ft_8200_run03.log`

`for i in {8400..13200..200}; do  python3 ../OpenNMT-py/translate.py -model gt-finetune/gt-finetune_8200_01_step_${i}.pt --ban_unk_token -src asl_test.txt -output gt-finetune/run01_01/step_${i}_pre_01.txt ; done`
`for i in {8400..13200..200}; do  python3 ../OpenNMT-py/translate.py -model gt-finetune/gt-finetune_8200_02_step_${i}.pt --ban_unk_token -src asl_test.txt -output gt-finetune/run01_02/step_${i}_pre_02.txt ; done`
`for i in {8400..13200..200}; do  python3 ../OpenNMT-py/translate.py -model gt-finetune/gt-finetune_8200_03_step_${i}.pt --ban_unk_token -src asl_test.txt -output gt-finetune/run01_03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt-finetune/run01_01/* asl/runs/gt-finetune/run01_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt-finetune/run01_02/* asl/runs/gt-finetune/run01_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt-finetune/run01_03/* asl/runs/gt-finetune/run01_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt-finetune/run01_01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt-finetune/run01_02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt-finetune/run01_03 >> test.txt`

### run02 @ 8800 epochs
`python3 ../OpenNMT-py/train.py --config aslen_ft_8800_run01.yaml --train_from gt-pretrain/models/gt-pretrain_02_step_8800.pt --reset_optim keep_states --log_file gt-pretrain/aslen_ft_8800_run01.log`
`python3 ../OpenNMT-py/train.py --config aslen_ft_8800_run02.yaml --train_from gt-pretrain/models/gt-pretrain_02_step_8800.pt --reset_optim keep_states --log_file gt-pretrain/aslen_ft_8800_run02.log`
`python3 ../OpenNMT-py/train.py --config aslen_ft_8800_run03.yaml --train_from gt-pretrain/models/gt-pretrain_02_step_8800.pt --reset_optim keep_states --log_file gt-pretrain/aslen_ft_8800_run03.log`

`for i in {9000..13800..200}; do  python3 ../OpenNMT-py/translate.py -model gt-finetune/gt-finetune_8800_01_step_${i}.pt --ban_unk_token -src asl_test.txt -output gt-finetune/run02_01/step_${i}_pre_01.txt ; done`
`for i in {9000..13800..200}; do  python3 ../OpenNMT-py/translate.py -model gt-finetune/gt-finetune_8800_02_step_${i}.pt --ban_unk_token -src asl_test.txt -output gt-finetune/run02_02/step_${i}_pre_02.txt ; done`
`for i in {9000..13800..200}; do  python3 ../OpenNMT-py/translate.py -model gt-finetune/gt-finetune_8800_03_step_${i}.pt --ban_unk_token -src asl_test.txt -output gt-finetune/run02_03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt-finetune/run02_01/* asl/runs/gt-finetune/run02_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt-finetune/run02_02/* asl/runs/gt-finetune/run02_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt-finetune/run02_03/* asl/runs/gt-finetune/run02_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt-finetune/run02_01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt-finetune/run02_02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt-finetune/run02_03 >> test.txt`

### run03 @ 9800 epochs
`python3 ../OpenNMT-py/train.py --config aslen_ft_9800_run01.yaml --train_from gt-pretrain/models/gt-pretrain_03_step_9800.pt --reset_optim keep_states --log_file gt-pretrain/aslen_ft_9800_run01.log`
`python3 ../OpenNMT-py/train.py --config aslen_ft_9800_run02.yaml --train_from gt-pretrain/models/gt-pretrain_03_step_9800.pt --reset_optim keep_states --log_file gt-pretrain/aslen_ft_9800_run02.log`
`python3 ../OpenNMT-py/train.py --config aslen_ft_9800_run03.yaml --train_from gt-pretrain/models/gt-pretrain_03_step_9800.pt --reset_optim keep_states --log_file gt-pretrain/aslen_ft_9800_run03.log`

`for i in {10000..14800..200}; do  python3 ../OpenNMT-py/translate.py -model gt-finetune/gt-finetune_9800_01_step_${i}.pt --ban_unk_token -src asl_test.txt -output gt-finetune/run03_01/step_${i}_pre_01.txt ; done`
`for i in {10000..14800..200}; do  python3 ../OpenNMT-py/translate.py -model gt-finetune/gt-finetune_9800_02_step_${i}.pt --ban_unk_token -src asl_test.txt -output gt-finetune/run03_02/step_${i}_pre_02.txt ; done`
`for i in {10000..14800..200}; do  python3 ../OpenNMT-py/translate.py -model gt-finetune/gt-finetune_9800_03_step_${i}.pt --ban_unk_token -src asl_test.txt -output gt-finetune/run03_03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt-finetune/run03_01/* asl/runs/gt-finetune/run03_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt-finetune/run03_02/* asl/runs/gt-finetune/run03_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/gt-finetune/run03_03/* asl/runs/gt-finetune/run03_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt-finetune/run03_01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt-finetune/run03_02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/en_test_tok.txt -d asl/runs/gt-finetune/run03_03 >> test.txt`
