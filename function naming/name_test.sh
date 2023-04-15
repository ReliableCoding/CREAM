lang=java #programming language
beam_size=1
batch_size=256
source_length=256
target_length=32
data_dir=data
output_dir=output/model_name
dev_file=$data_dir/valid.jsonl
test_file=$data_dir/test.jsonl
test_model=$output_dir/checkpoint-best-bleu/pytorch_model.bin #checkpoint for test
alpha=0.6
fusion=0.1

python run_causal.py --do_test --model_type roberta --model_name_or_path microsoft/codebert-base --load_model_path $test_model --dev_filename $dev_file --test_filename $test_file --alpha $alpha --fusion $fusion  --output_dir $output_dir --max_source_length $source_length --max_target_length $target_length --beam_size $beam_size --eval_batch_size $batch_size
