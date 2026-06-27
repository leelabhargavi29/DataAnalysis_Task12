Task 12: Feature Engineering

Objective:
Perform feature engineering on the California Housing dataset.

Tools Used:
- Python
- Pandas
- NumPy
- Scikit-learn

Dataset:
California Housing Dataset (housing.csv)

Steps Performed:
1. Loaded the dataset.
2. Created a new feature:
   - Rooms_per_Occupant = AveRooms / AveOccup
3. Applied Log Transformation:
   - Population_Log = log1p(Population)
4. Applied Label Encoding:
   - Income_Level based on MedInc.
5. Saved the enhanced dataset as enhanced_housing.csv.

Output Files:
- enhanced_housing.csv

Interview Questions:

1. What is Feature Engineering?
Feature Engineering is the process of creating, transforming, or selecting features from raw data to improve machine learning model performance.

2. One-Hot Encoding vs Label Encoding?
-Label Encoding
Converts categories into numbers.
Example: Low=0, Medium=1, High=2
-One-Hot Encoding
Creates separate binary columns.
