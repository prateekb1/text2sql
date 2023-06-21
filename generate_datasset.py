import random

def generate_dataset():
  """Generates a dataset of SQL queries and natural language questions."""
  dataset = []
  for _ in range(100):
    table_name = "marketing_data"
    column_name = "active_agency_customers"
    date = random.choice(["2022-01-01", "2022-02-01", "2022-03-01"])
    query = f"SELECT COUNT(*) AS total_active_agency_customers FROM {table_name} WHERE date = '{date}';"
    question = f"How many active agency customers did we have on {date}?"
    dataset.append((query, question))
  return dataset

dataset = generate_dataset()
