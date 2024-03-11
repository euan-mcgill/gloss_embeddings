# Text2Gloss - ASL

----------------------------------------------------------------------------------------------
## STAGE 1 - Baseline
----------------------------------------------------------------------------------------------

`python3 ../OpenNMT-py/build_vocab.py --config enasl_run01.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config enasl_run01.yaml --log_file tg/enasl_run01.log`
`python3 ../OpenNMT-py/train.py --config enasl_run02.yaml --log_file tg/enasl_run02.log`
`python3 ../OpenNMT-py/train.py --config enasl_run03.yaml --log_file tg/enasl_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg/tg_01_step_${i}.pt -src en_test_tok.txt -output tg/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg/tg_02_step_${i}.pt -src en_test_tok.txt -output tg/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg/tg_03_step_${i}.pt -src en_test_tok.txt -output tg/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg/run01/* asl/runs/tg/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg/run02/* asl/runs/tg/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg/run03/* asl/runs/tg/run03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg/run01 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg/run02 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg/run03 >> metrics.txt`

----------------------------------------------------------------------------------------------
## STAGE 1a - Baseline + embs
----------------------------------------------------------------------------------------------

## encoder embs
`python3 ../OpenNMT-py/build_vocab.py --config enasl_enc_run01.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config enasl_enc_run01.yaml --log_file tg-enc/enasl_enc_run01.log`
`python3 ../OpenNMT-py/train.py --config enasl_enc_run02.yaml --log_file tg-enc/enasl_enc_run02.log`
`python3 ../OpenNMT-py/train.py --config enasl_enc_run03.yaml --log_file tg-enc/enasl_enc_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-enc/tg_01_step_${i}.pt -src en_test_tok.txt -output tg-enc/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-enc/tg_02_step_${i}.pt -src en_test_tok.txt -output tg-enc/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-enc/tg_03_step_${i}.pt -src en_test_tok.txt -output tg-enc/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-enc/run01/* asl/runs/tg-enc/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-enc/run02/* asl/runs/tg-enc/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-enc/run03/* asl/runs/tg-enc/run03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-enc/run01 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-enc/run02 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-enc/run03 >> metrics.txt`

## decoder embs
`python3 ../OpenNMT-py/build_vocab.py --config enasl_dec_run01.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config enasl_dec_run01.yaml --log_file tg-dec/enasl_dec_run01.log`
`python3 ../OpenNMT-py/train.py --config enasl_dec_run02.yaml --log_file tg-dec/enasl_dec_run02.log`
`python3 ../OpenNMT-py/train.py --config enasl_dec_run03.yaml --log_file tg-dec/enasl_dec_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-dec/tg_01_step_${i}.pt -src en_test_tok.txt -output tg-dec/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-dec/tg_02_step_${i}.pt -src en_test_tok.txt -output tg-dec/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-dec/tg_03_step_${i}.pt -src en_test_tok.txt -output tg-dec/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-dec/run01/* asl/runs/tg-dec/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-dec/run02/* asl/runs/tg-dec/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-dec/run03/* asl/runs/tg-dec/run03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-dec/run01 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-dec/run02 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-dec/run03 >> metrics.txt`

## encoder and decoder embs
`python3 ../OpenNMT-py/build_vocab.py --config enasl_both_run01.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config enasl_both_run01.yaml --log_file tg-both/enasl_both_run01.log`
`python3 ../OpenNMT-py/train.py --config enasl_both_run02.yaml --log_file tg-both/enasl_both_run02.log`
`python3 ../OpenNMT-py/train.py --config enasl_both_run03.yaml --log_file tg-both/enasl_both_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-both/tg_01_step_${i}.pt -src en_test_tok.txt -output tg-both/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-both/tg_02_step_${i}.pt -src en_test_tok.txt -output tg-both/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-both/tg_03_step_${i}.pt -src en_test_tok.txt -output tg-both/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-both/run01/* asl/runs/tg-both/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-both/run02/* asl/runs/tg-both/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-both/run03/* asl/runs/tg-both/run03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-both/run01 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-both/run02 >> metrics.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-both/run03 >> metrics.txt`

----------------------------------------------------------------------------------------------
## STAGE 2 - PT+FT
----------------------------------------------------------------------------------------------

### pretrain phase
`python3 ../OpenNMT-py/build_vocab.py --config enasl_pt_vocab.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config enasl_pt_run01.yaml --log_file tg-pretrain/enasl_pt_run01.log`
`python3 ../OpenNMT-py/train.py --config enasl_pt_run02.yaml --log_file tg-pretrain/enasl_pt_run02.log`
`python3 ../OpenNMT-py/train.py --config enasl_pt_run03.yaml --log_file tg-pretrain/enasl_pt_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pretrain/tg-pretrain_01_step_${i}.pt -src en_test_tok.txt -output tg-pretrain/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pretrain/tg-pretrain_02_step_${i}.pt -src en_test_tok.txt -output tg-pretrain/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pretrain/tg-pretrain_03_step_${i}.pt -src en_test_tok.txt -output tg-pretrain/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-pretrain/run01/* asl/runs/tg-pretrain/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-pretrain/run02/* asl/runs/tg-pretrain/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-pretrain/run03/* asl/runs/tg-pretrain/run03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-pretrain/run01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-pretrain/run02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-pretrain/run03 >> test.txt`

### finetune phase

### run01 @ 1200 epochs
`python3 ../OpenNMT-py/train.py --config enasl_ft_1200_run01.yaml --train_from tg-pretrain/models/tg-pretrain_01_step_1200.pt --reset_optim keep_states --log_file tg-pretrain/enasl_ft_1200_run01.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_1200_run02.yaml --train_from tg-pretrain/models/tg-pretrain_01_step_1200.pt --reset_optim keep_states --log_file tg-pretrain/enasl_ft_1200_run02.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_1200_run03.yaml --train_from tg-pretrain/models/tg-pretrain_01_step_1200.pt --reset_optim keep_states --log_file tg-pretrain/enasl_ft_1200_run03.log`

`for i in {1400..6200..200}; do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_1200_01_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-finetune/run01_01/step_${i}_pre_01.txt ; done`
`for i in {1400..6200..200}; do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_1200_02_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-finetune/run01_02/step_${i}_pre_02.txt ; done`
`for i in {1400..6200..200}; do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_1200_03_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-finetune/run01_03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-finetune/run01_01/* asl/runs/tg-finetune/run01_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-finetune/run01_02/* asl/runs/tg-finetune/run01_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-finetune/run01_03/* asl/runs/tg-finetune/run01_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-finetune/run01_01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-finetune/run01_02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-finetune/run01_03 >> test.txt`

### run02 @ 8600 epochs
`python3 ../OpenNMT-py/train.py --config enasl_ft_8600_run01.yaml --train_from tg-pretrain/models/tg-pretrain_02_step_8600.pt --reset_optim keep_states --log_file tg-pretrain/enasl_ft_8600_run01.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_8600_run02.yaml --train_from tg-pretrain/models/tg-pretrain_02_step_8600.pt --reset_optim keep_states --log_file tg-pretrain/enasl_ft_8600_run02.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_8600_run03.yaml --train_from tg-pretrain/models/tg-pretrain_02_step_8600.pt --reset_optim keep_states --log_file tg-pretrain/enasl_ft_8600_run03.log`

`for i in {8800..13600..200}; do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_8600_01_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-finetune/run02_01/step_${i}_pre_01.txt ; done`
`for i in {8800..13600..200}; do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_8600_02_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-finetune/run02_02/step_${i}_pre_02.txt ; done`
`for i in {8800..13600..200}; do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_8600_03_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-finetune/run02_03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-finetune/run02_01/* asl/runs/tg-finetune/run02_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-finetune/run02_02/* asl/runs/tg-finetune/run02_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-finetune/run02_03/* asl/runs/tg-finetune/run02_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-finetune/run02_01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-finetune/run02_02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-finetune/run02_03 >> test.txt`

### run03 @ 4600 epochs
`python3 ../OpenNMT-py/train.py --config enasl_ft_4600_run01.yaml --train_from tg-pretrain/models/tg-pretrain_02_step_4600.pt --reset_optim keep_states --log_file tg-pretrain/enasl_ft_4600_run01.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_4600_run02.yaml --train_from tg-pretrain/models/tg-pretrain_02_step_4600.pt --reset_optim keep_states --log_file tg-pretrain/enasl_ft_4600_run02.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_4600_run03.yaml --train_from tg-pretrain/models/tg-pretrain_02_step_4600.pt --reset_optim keep_states --log_file tg-pretrain/enasl_ft_4600_run03.log`

`for i in {4800..9600..200}; do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_4600_01_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-finetune/run03_01/step_${i}_pre_01.txt ; done`
`for i in {4800..9600..200}; do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_4600_02_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-finetune/run03_02/step_${i}_pre_02.txt ; done`
`for i in {4800..9600..200}; do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_4600_03_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-finetune/run03_03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-finetune/run03_01/* asl/runs/tg-finetune/run03_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-finetune/run03_02/* asl/runs/tg-finetune/run03_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-finetune/run03_03/* asl/runs/tg-finetune/run03_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-finetune/run03_01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-finetune/run03_02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-finetune/run03_03 >> test.txt`
