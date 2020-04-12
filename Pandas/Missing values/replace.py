import pandas as pd
import os

DATASETS_PATH = "datasets"
DATASET = "property_dataset.csv"

path = os.path.join(DATASETS_PATH, DATASET)

df = pd.read_csv(path, na_values=["n/a", "?", "--"])

print(df)