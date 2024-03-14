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
`python3 ../OpenNMT-py/train.py --config enasl_ft_4600_run01.yaml --train_from tg-pretrain/models/tg-pretrain_03_step_4600.pt --reset_optim keep_states --log_file tg-pretrain/enasl_ft_4600_run01.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_4600_run02.yaml --train_from tg-pretrain/models/tg-pretrain_03_step_4600.pt --reset_optim keep_states --log_file tg-pretrain/enasl_ft_4600_run02.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_4600_run03.yaml --train_from tg-pretrain/models/tg-pretrain_03_step_4600.pt --reset_optim keep_states --log_file tg-pretrain/enasl_ft_4600_run03.log`

`for i in {4800..9600..200}; do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_4600_01_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-finetune/run03_01/step_${i}_pre_01.txt ; done`
`for i in {4800..9600..200}; do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_4600_02_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-finetune/run03_02/step_${i}_pre_02.txt ; done`
`for i in {4800..9600..200}; do  python3 ../OpenNMT-py/translate.py -model tg-finetune/tg-finetune_4600_03_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-finetune/run03_03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-finetune/run03_01/* asl/runs/tg-finetune/run03_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-finetune/run03_02/* asl/runs/tg-finetune/run03_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-finetune/run03_03/* asl/runs/tg-finetune/run03_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-finetune/run03_01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-finetune/run03_02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-finetune/run03_03 >> test.txt`

----------------------------------------------------------------------------------------------

## Encoder embeddings

### pretrain phase
`python3 ../OpenNMT-py/build_vocab.py --config enasl_pt_enc_vocab.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config enasl_pt_enc_run01.yaml --log_file tg-pt-enc/enasl_pt_enc_run01.log`
`python3 ../OpenNMT-py/train.py --config enasl_pt_enc_run02.yaml --log_file tg-pt-enc/enasl_pt_enc_run02.log`
`python3 ../OpenNMT-py/train.py --config enasl_pt_enc_run03.yaml --log_file tg-pt-enc/enasl_pt_enc_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pt-enc/tg-pt-enc_01_step_${i}.pt -src en_test_tok.txt -output tg-pt-enc/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pt-enc/tg-pt-enc_02_step_${i}.pt -src en_test_tok.txt -output tg-pt-enc/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pt-enc/tg-pt-enc_03_step_${i}.pt -src en_test_tok.txt -output tg-pt-enc/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-pt-enc/run01/* asl/runs/tg-pt-enc/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-pt-enc/run02/* asl/runs/tg-pt-enc/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-pt-enc/run03/* asl/runs/tg-pt-enc/run03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-pt-enc/run01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-pt-enc/run02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-pt-enc/run03 >> test.txt`

### finetune phase

### run01 @ 5200 epochs
`python3 ../OpenNMT-py/train.py --config enasl_ft_enc_5200_run01.yaml --train_from tg-pt-enc/models/tg-pt-enc_01_step_5200.pt --reset_optim keep_states --log_file tg-ft-enc/enasl_ft_enc_5200_run01.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_enc_5200_run02.yaml --train_from tg-pt-enc/models/tg-pt-enc_01_step_5200.pt --reset_optim keep_states --log_file tg-ft-enc/enasl_ft_enc_5200_run02.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_enc_5200_run03.yaml --train_from tg-pt-enc/models/tg-pt-enc_01_step_5200.pt --reset_optim keep_states --log_file tg-ft-enc/enasl_ft_enc_5200_run03.log`

`for i in {5400..10200..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-enc/tg-ft-enc_5200_01_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-enc/run01_01/step_${i}_pre_01.txt ; done`
`for i in {5400..10200..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-enc/tg-ft-enc_5200_02_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-enc/run01_02/step_${i}_pre_02.txt ; done`
`for i in {5400..10200..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-enc/tg-ft-enc_5200_03_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-enc/run01_03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-enc/run01_01/* asl/runs/tg-ft-enc/run01_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-enc/run01_02/* asl/runs/tg-ft-enc/run01_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-enc/run01_03/* asl/runs/tg-ft-enc/run01_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-enc/run01_01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-enc/run01_02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-enc/run01_03 >> test.txt`

### run02 @ 6200 epochs
`python3 ../OpenNMT-py/train.py --config enasl_ft_enc_6200_run01.yaml --train_from tg-pt-enc/models/tg-pt-enc_02_step_6200.pt --reset_optim keep_states --log_file tg-ft-enc/enasl_ft_enc_6200_run01.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_enc_6200_run02.yaml --train_from tg-pt-enc/models/tg-pt-enc_02_step_6200.pt --reset_optim keep_states --log_file tg-ft-enc/enasl_ft_enc_6200_run02.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_enc_6200_run03.yaml --train_from tg-pt-enc/models/tg-pt-enc_02_step_6200.pt --reset_optim keep_states --log_file tg-ft-enc/enasl_ft_enc_6200_run03.log`

`for i in {6400..11200..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-enc/tg-ft-enc_6200_01_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-enc/run02_01/step_${i}_pre_01.txt ; done`
`for i in {6400..11200..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-enc/tg-ft-enc_6200_02_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-enc/run02_02/step_${i}_pre_02.txt ; done`
`for i in {6400..11200..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-enc/tg-ft-enc_6200_03_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-enc/run02_03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-enc/run02_01/* asl/runs/tg-ft-enc/run02_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-enc/run02_02/* asl/runs/tg-ft-enc/run02_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-enc/run02_03/* asl/runs/tg-ft-enc/run02_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-enc/run02_01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-enc/run02_02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-enc/run02_03 >> test.txt`

### run03 @ 2800 epochs
`python3 ../OpenNMT-py/train.py --config enasl_ft_enc_2800_run01.yaml --train_from tg-pt-enc/models/tg-pt-enc_03_step_2800.pt --reset_optim keep_states --log_file tg-pt-enc/enasl_ft_enc_2800_run01.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_enc_2800_run02.yaml --train_from tg-pt-enc/models/tg-pt-enc_03_step_2800.pt --reset_optim keep_states --log_file tg-pt-enc/enasl_ft_enc_2800_run02.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_enc_2800_run03.yaml --train_from tg-pt-enc/models/tg-pt-enc_03_step_2800.pt --reset_optim keep_states --log_file tg-pt-enc/enasl_ft_enc_2800_run03.log`

`for i in {3000..7800..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-enc/tg-ft-enc_2800_01_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-enc/run03_01/step_${i}_pre_01.txt ; done`
`for i in {3000..7800..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-enc/tg-ft-enc_2800_02_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-enc/run03_02/step_${i}_pre_02.txt ; done`
`for i in {3000..7800..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-enc/tg-ft-enc_2800_03_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-enc/run03_03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-enc/run03_01/* asl/runs/tg-ft-enc/run03_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-enc/run03_02/* asl/runs/tg-ft-enc/run03_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-enc/run03_03/* asl/runs/tg-ft-enc/run03_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-enc/run03_01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-enc/run03_02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-enc/run03_03 >> test.txt`

## Decoder embeddings

### pretrain phase
`python3 ../OpenNMT-py/build_vocab.py --config enasl_pt_dec_vocab.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config enasl_pt_dec_run01.yaml --log_file tg-pt-dec/enasl_pt_dec_run01.log`
`python3 ../OpenNMT-py/train.py --config enasl_pt_dec_run02.yaml --log_file tg-pt-dec/enasl_pt_dec_run02.log`
`python3 ../OpenNMT-py/train.py --config enasl_pt_dec_run03.yaml --log_file tg-pt-dec/enasl_pt_dec_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pt-dec/tg-pt-dec_01_step_${i}.pt -src en_test_tok.txt -output tg-pt-dec/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pt-dec/tg-pt-dec_02_step_${i}.pt -src en_test_tok.txt -output tg-pt-dec/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pt-dec/tg-pt-dec_03_step_${i}.pt -src en_test_tok.txt -output tg-pt-dec/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-pt-dec/run01/* asl/runs/tg-pt-dec/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-pt-dec/run02/* asl/runs/tg-pt-dec/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-pt-dec/run03/* asl/runs/tg-pt-dec/run03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-pt-dec/run01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-pt-dec/run02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-pt-dec/run03 >> test.txt`

### finetune phase

### run01 @ 9400 epochs
`python3 ../OpenNMT-py/train.py --config enasl_ft_dec_9400_run01.yaml --train_from tg-pt-dec/models/tg-pt-dec_01_step_9400.pt --reset_optim keep_states --log_file tg-ft-dec/enasl_ft_dec_9400_run01.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_dec_9400_run02.yaml --train_from tg-pt-dec/models/tg-pt-dec_01_step_9400.pt --reset_optim keep_states --log_file tg-ft-dec/enasl_ft_dec_9400_run02.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_dec_9400_run03.yaml --train_from tg-pt-dec/models/tg-pt-dec_01_step_9400.pt --reset_optim keep_states --log_file tg-ft-dec/enasl_ft_dec_9400_run03.log`

`for i in {9600..14400..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-dec/tg-ft-dec_9400_01_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-dec/run01_01/step_${i}_pre_01.txt ; done`
`for i in {9600..14400..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-dec/tg-ft-dec_9400_02_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-dec/run01_02/step_${i}_pre_02.txt ; done`
`for i in {9600..14400..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-dec/tg-ft-dec_9400_03_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-dec/run01_03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-dec/run01_01/* asl/runs/tg-ft-dec/run01_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-dec/run01_02/* asl/runs/tg-ft-dec/run01_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-dec/run01_03/* asl/runs/tg-ft-dec/run01_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-dec/run01_01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-dec/run01_02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-dec/run01_03 >> test.txt`

### run02 @ 10000 epochs
`python3 ../OpenNMT-py/train.py --config enasl_ft_dec_10000_run01.yaml --train_from tg-pt-dec/models/tg-pt-dec_02_step_10000.pt --reset_optim keep_states --log_file tg-ft-dec/enasl_ft_dec_10000_run01.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_dec_10000_run02.yaml --train_from tg-pt-dec/models/tg-pt-dec_02_step_10000.pt --reset_optim keep_states --log_file tg-ft-dec/enasl_ft_dec_10000_run02.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_dec_10000_run03.yaml --train_from tg-pt-dec/models/tg-pt-dec_02_step_10000.pt --reset_optim keep_states --log_file tg-ft-dec/enasl_ft_dec_10000_run03.log`

`for i in {10200..15000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-dec/tg-ft-dec_10000_01_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-dec/run02_01/step_${i}_pre_01.txt ; done`
`for i in {10200..15000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-dec/tg-ft-dec_10000_02_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-dec/run02_02/step_${i}_pre_02.txt ; done`
`for i in {10200..15000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-dec/tg-ft-dec_10000_03_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-dec/run02_03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-dec/run02_01/* asl/runs/tg-ft-dec/run02_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-dec/run02_02/* asl/runs/tg-ft-dec/run02_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-dec/run02_03/* asl/runs/tg-ft-dec/run02_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-dec/run02_01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-dec/run02_02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-dec/run02_03 >> test.txt`

### run03 @ 6400 epochs
`python3 ../OpenNMT-py/train.py --config enasl_ft_dec_6400_run01.yaml --train_from tg-pt-dec/models/tg-pt-dec_03_step_6400.pt --reset_optim keep_states --log_file tg-pt-dec/enasl_ft_dec_6400_run01.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_dec_6400_run02.yaml --train_from tg-pt-dec/models/tg-pt-dec_03_step_6400.pt --reset_optim keep_states --log_file tg-pt-dec/enasl_ft_dec_6400_run02.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_dec_6400_run03.yaml --train_from tg-pt-dec/models/tg-pt-dec_03_step_6400.pt --reset_optim keep_states --log_file tg-pt-dec/enasl_ft_dec_6400_run03.log`

`for i in {6400..11400..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-dec/tg-ft-dec_6400_01_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-dec/run03_01/step_${i}_pre_01.txt ; done`
`for i in {6400..11400..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-dec/tg-ft-dec_6400_02_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-dec/run03_02/step_${i}_pre_02.txt ; done`
`for i in {6400..11400..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-dec/tg-ft-dec_6400_03_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-dec/run03_03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-dec/run03_01/* asl/runs/tg-ft-dec/run03_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-dec/run03_02/* asl/runs/tg-ft-dec/run03_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-dec/run03_03/* asl/runs/tg-ft-dec/run03_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-dec/run03_01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-dec/run03_02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-dec/run03_03 >> test.txt`

## Encoder + Decoder embeddings

### pretrain phase
`python3 ../OpenNMT-py/build_vocab.py --config enasl_pt_both_vocab.yaml --n_sample 50000`

`python3 ../OpenNMT-py/train.py --config enasl_pt_both_run01.yaml --log_file tg-pt-both/enasl_pt_both_run01.log`
`python3 ../OpenNMT-py/train.py --config enasl_pt_both_run02.yaml --log_file tg-pt-both/enasl_pt_both_run02.log`
`python3 ../OpenNMT-py/train.py --config enasl_pt_both_run03.yaml --log_file tg-pt-both/enasl_pt_both_run03.log`

`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pt-both/tg-pt-both_01_step_${i}.pt -src en_test_tok.txt -output tg-pt-both/run01/step_${i}_pre_01.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pt-both/tg-pt-both_02_step_${i}.pt -src en_test_tok.txt -output tg-pt-both/run02/step_${i}_pre_02.txt ; done`
`for i in {200..10000..200}; do  python3 ../OpenNMT-py/translate.py -model tg-pt-both/tg-pt-both_03_step_${i}.pt -src en_test_tok.txt -output tg-pt-both/run03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-pt-both/run01/* asl/runs/tg-pt-both/run01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-pt-both/run02/* asl/runs/tg-pt-both/run02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-pt-both/run03/* asl/runs/tg-pt-both/run03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-pt-both/run01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-pt-both/run02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-pt-both/run03 >> test.txt`

### finetune phase

### run01 @ 3200 epochs
`python3 ../OpenNMT-py/train.py --config enasl_ft_both_3200_run01.yaml --train_from tg-pt-both/models/tg-pt-both_01_step_3200.pt --reset_optim keep_states --log_file tg-ft-both/enasl_ft_both_3200_run01.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_both_3200_run02.yaml --train_from tg-pt-both/models/tg-pt-both_01_step_3200.pt --reset_optim keep_states --log_file tg-ft-both/enasl_ft_both_3200_run02.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_both_3200_run03.yaml --train_from tg-pt-both/models/tg-pt-both_01_step_3200.pt --reset_optim keep_states --log_file tg-ft-both/enasl_ft_both_3200_run03.log`

`for i in {3400..8200..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-both/tg-ft-both_3200_01_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-both/run01_01/step_${i}_pre_01.txt ; done`
`for i in {3400..8200..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-both/tg-ft-both_3200_02_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-both/run01_02/step_${i}_pre_02.txt ; done`
`for i in {3400..8200..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-both/tg-ft-both_3200_03_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-both/run01_03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-both/run01_01/* asl/runs/tg-ft-both/run01_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-both/run01_02/* asl/runs/tg-ft-both/run01_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-both/run01_03/* asl/runs/tg-ft-both/run01_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-both/run01_01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-both/run01_02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-both/run01_03 >> test.txt`

### run02 @ 800 epochs
`python3 ../OpenNMT-py/train.py --config enasl_ft_both_800_run01.yaml --train_from tg-pt-both/models/tg-pt-both_02_step_800.pt --reset_optim keep_states --log_file tg-ft-both/enasl_ft_both_800_run01.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_both_800_run02.yaml --train_from tg-pt-both/models/tg-pt-both_02_step_800.pt --reset_optim keep_states --log_file tg-ft-both/enasl_ft_both_800_run02.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_both_800_run03.yaml --train_from tg-pt-both/models/tg-pt-both_02_step_800.pt --reset_optim keep_states --log_file tg-ft-both/enasl_ft_both_800_run03.log`

`for i in {1000..5800..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-both/tg-ft-both_800_01_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-both/run02_01/step_${i}_pre_01.txt ; done`
`for i in {1000..5800..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-both/tg-ft-both_800_02_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-both/run02_02/step_${i}_pre_02.txt ; done`
`for i in {1000..5800..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-both/tg-ft-both_800_03_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-both/run02_03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-both/run02_01/* asl/runs/tg-ft-both/run02_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-both/run02_02/* asl/runs/tg-ft-both/run02_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-both/run02_03/* asl/runs/tg-ft-both/run02_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-both/run02_01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-both/run02_02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-both/run02_03 >> test.txt`

### run03 @ 8600 epochs
`python3 ../OpenNMT-py/train.py --config enasl_ft_both_8600_run01.yaml --train_from tg-pt-both/models/tg-pt-both_03_step_8600.pt --reset_optim keep_states --log_file tg-pt-both/enasl_ft_both_8600_run01.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_both_8600_run02.yaml --train_from tg-pt-both/models/tg-pt-both_03_step_8600.pt --reset_optim keep_states --log_file tg-pt-both/enasl_ft_both_8600_run02.log`
`python3 ../OpenNMT-py/train.py --config enasl_ft_both_8600_run03.yaml --train_from tg-pt-both/models/tg-pt-both_03_step_8600.pt --reset_optim keep_states --log_file tg-pt-both/enasl_ft_both_8600_run03.log`

`for i in {8800..13600..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-both/tg-ft-both_8600_01_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-both/run03_01/step_${i}_pre_01.txt ; done`
`for i in {8800..13600..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-both/tg-ft-both_8600_02_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-both/run03_02/step_${i}_pre_02.txt ; done`
`for i in {8800..13600..200}; do  python3 ../OpenNMT-py/translate.py -model tg-ft-both/tg-ft-both_8600_03_step_${i}.pt --ban_unk_token -src en_test_tok.txt -output tg-ft-both/run03_03/step_${i}_pre_03.txt ; done`

`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-both/run03_01/* asl/runs/tg-ft-both/run03_01`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-both/run03_02/* asl/runs/tg-ft-both/run03_02`
`scp -i ~/Documents/misc/oracle-cloud/ssh-key-2023-05-11.key ubuntu@158.178.202.202:asl_exps/tg-ft-both/run03_03/* asl/runs/tg-ft-both/run03_03`

`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-both/run03_01 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-both/run03_02 >> test.txt`
`python calculate_metrics.py ~/Documents/git/gloss_embeddings/asl/data/parallel/asl_test.txt -d asl/runs/tg-ft-both/run03_03 >> test.txt`
