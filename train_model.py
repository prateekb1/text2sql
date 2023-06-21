import transformers
import torch
from encode_dataset import encoded_dataset


def train_model(encoded_dataset):
  """Trains a model from a dataset of encoded SQL queries and natural language questions."""
  model = transformers.AutoModelForSeq2SeqLM.from_pretrained("gpt-3-medium")
  optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
  for epoch in range(10):
    for query, question in encoded_dataset:
      loss = model(query, question, labels=question)[0]
      optimizer.zero_grad()
      loss.backward()
      optimizer.step()

train_model(encoded_dataset)
