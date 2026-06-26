import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("california_housing.csv")
print("Original Dataset")
print(df.head())
df["Rooms_per_Occupant"] = df["AveRooms"] / df["AveOccup"]
df["Population_Log"] = np.log1p(df["Population"])
le = LabelEncoder()
df["Income_Level"] = pd.cut(
    df["MedInc"],
    bins=3,
    labels=["Low", "Medium", "High"]
)

df["Income_Level"] = le.fit_transform(df["Income_Level"])
print("\nEnhanced Dataset")
print(df.head())
df.to_csv("enhanced_housing.csv", index=False)
print("\nEnhanced dataset saved as enhanced_housing.csv")