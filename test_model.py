import torch
import transformers
from train_model import train_model

model = transformers.AutoModelForSeq2SeqLM.from_pretrained("gpt-3-medium")

def test_model(model):
  """Tests a model by asking it to answer a few questions."""
  questions = ["How many active agency customers did we have on January 1st, 2022?", "When did we get the highest number of users per day in Q1 2023?", "When did we get the maximum of daily visits on the website in 2022?"]
  for question in questions:
    encoded_question = encoder(question.strip().lower(), return_tensors="pt")
    output = model.generate(encoded_question, max_length=100, do_sample=True)
    print(f"Question: {question}")
    print(f"Generated SQL query: {output}")

test_model(model)
