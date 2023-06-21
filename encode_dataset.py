import transformers
from generate_datasset import dataset

import transformers

def encode_dataset(dataset):
  """Encodes a dataset of SQL queries and natural language questions."""
  encoder = transformers.AutoModelForSeq2SeqLM.from_pretrained("gpt-3-medium")
  encoded_dataset = []
  for query, question in dataset:
    encoded_query = encoder(query.strip().lower(), return_tensors="pt")
    encoded_question = encoder(question.strip().lower(), return_tensors="pt")
    encoded_dataset.append((encoded_query, encoded_question))
  return encoded_dataset

encoded_dataset = encode_dataset(dataset)
