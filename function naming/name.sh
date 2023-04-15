lang=java #programming language
lr=5e-5
batch_size=32
beam_size=1
source_length=256
target_length=32
data_dir=data
output_dir=output/model_name
train_file=$data_dir/train.jsonl
dev_file=$data_dir/valid.jsonl
test_file=$data_dir/test.jsonl
eval_steps=1000 #400 for ruby, 600 for javascript, 1000 for others
train_steps=50000 #20000 for ruby, 30000 for javascript, 50000 for others
alpha=0.6
fusion=0.1
pretrained_model=microsoft/codebert-base

python run_causal.py --do_train --do_eval --model_type roberta --model_name_or_path $pretrained_model --train_filename $train_file --dev_filename $dev_file --test_filename $test_file --alpha $alpha --fusion $fusion  --output_dir $output_dir --max_source_length $source_length --max_target_length $target_length --beam_size $beam_size --train_batch_size $batch_size --eval_batch_size $batch_size --learning_rate $lr --train_steps $train_steps --eval_steps $eval_steps 