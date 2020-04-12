import pandas as pd
import os

def print_percentage(a, b, decimal_digits=2):
    percentage = a / b * 100
    percentage = round(percentage * 10 ** decimal_digits) / 10 ** decimal_digits

    print(f"{percentage}% ({a}/{b})\n")

DATASETS_PATH = "datasets"
DATASET = "titanic.csv"

path = os.path.join(DATASETS_PATH, DATASET)

df = pd.read_csv(path)

print("Total count of missing values:", df.isnull().sum().sum(), end="\n\n")

print("Rows with missing values:")
n_rows = df.shape[0]
n_rows_with_missings = df.isnull().any(axis=1).sum()
print_percentage(n_rows_with_missings, n_rows)

print("Number of nulls per column:")
n_missings_per_col =  df.isnull().sum()
print(n_missings_per_col, end="\n\n")

print("Percentage of nulls per column:")
percentage = n_missings_per_col / n_rows * 100
print(round(percentage * 100) / 100)
