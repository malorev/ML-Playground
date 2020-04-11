import pandas as pd
import os

DATASETS_PATH = "datasets/csv"
DATASET_NAME = "purchases_index.csv"

path = os.path.join(DATASETS_PATH, DATASET_NAME)

df = pd.read_csv(path, index_col=0) # Uses first column of the CSV file as the row labels of the dataframe

print(df.head())