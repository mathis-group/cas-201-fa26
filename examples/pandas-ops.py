import pandas as pd
import numpy as np
data_path = "examples/data/winequality-white.csv"

wine_data = pd.read_csv(data_path)

print(wine_data.columns)
low_scores = wine_data[wine_data["quality"] <= 4]
high_scores = wine_data[wine_data["quality"] >= 8]
print(f"High Score pH: {high_scores["free sulfur dioxide"].mean()}")
print(f"Low Score pH: {low_scores["free sulfur dioxide"].mean()}")