from flask import Flask, request, jsonify
import torch
from transformers import LlamaTokenizer, LlamaForCausalLM

app = Flask(__name__)

# Load model and tokenizer
model_name = "results"  # Adjust to your saved model path
model = LlamaForCausalLM.from_pretrained(model_name)
tokenizer = LlamaTokenizer.from_pretrained(model_name)

@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.json['text']
    inputs = tokenizer(input_text, return_tensors='pt')
    outputs = model.generate(inputs['input_ids'])
    prediction = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
