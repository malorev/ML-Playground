import pandas as pd
import os

DATASETS_PATH = "datasets/csv"
DATASET_NAME = "purchases.csv"

path = os.path.join(DATASETS_PATH, DATASET_NAME)

df = pd.read_csv(path) # Default row labels: 0, 1, 2, ...

print(df.head())