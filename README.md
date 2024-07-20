# Custom Language Model with Llama 3

This repository provides a working example of creating and deploying a custom language model using Llama 3.

## Prerequisites

- Python 3.7+
- Basic knowledge of machine learning and programming

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/llama3-custom-llm.git
    cd llama3-custom-llm
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Place your training and testing data in the `data/` directory.

## Training the Model

Run the `train.py` script to fine-tune the Llama 3 model on your dataset:
```bash
python train.py

## Deploying the Model

Run the app.py script to start a Flask API for your model:

```bash
python app.py
```

You can now send POST requests to http://0.0.0.0:5000/predict with a JSON payload containing the text you want to generate predictions for.

# Example Request
```bash
curl -X POST http://0.0.0.0:5000/predict -H "Content-Type: application/json" -d '{"text":"Your input text here"}'
```
# Files
train.py: Script to fine-tune the Llama 3 model.
app.py: Script to deploy the fine-tuned model using Flask.
data/: Directory to store training and testing data.

# Medium Article

https://medium.com/@lakshnorris/creating-a-custom-language-model-with-llama-3-a-working-example-a3f84e0fbf85
