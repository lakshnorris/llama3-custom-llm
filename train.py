from transformers import LlamaForCausalLM, LlamaTokenizer, Trainer, TrainingArguments
from datasets import load_dataset

# Load pre-trained Llama model and tokenizer
model_name = "llama-3"
model = LlamaForCausalLM.from_pretrained(model_name)
tokenizer = LlamaTokenizer.from_pretrained(model_name)

# Load your dataset
data_files = {"train": "data/train.csv", "test": "data/test.csv"}
dataset = load_dataset('csv', data_files=data_files)

# Tokenize the dataset
def tokenize_function(examples):
    return tokenizer(examples['text'], padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Set training arguments
training_args = TrainingArguments(
    output_dir="./results",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['test']
)

# Start training
trainer.train()
