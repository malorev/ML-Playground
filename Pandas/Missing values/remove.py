import pandas as pd
import os

DATASETS_PATH = "datasets"
DATASET = "titanic.csv"

path = os.path.join(DATASETS_PATH, DATASET)

df = pd.read_csv(path)

n_rows_with_missings = df.isnull().any(axis=1).sum()
print("Rows with missing values before dropping them:", n_rows_with_missings)

#df_copy = df.dropna() # Creates a copy of df without missing values
df.dropna(inplace=True)

n_rows_with_missings = df.isnull().any(axis=1).sum()
print("Rows with missing values after dropping them:", n_rows_with_missings)