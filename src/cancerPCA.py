import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Read data from CSV file
df = pd.read_csv('dataFilterByUs.csv')
# Remove the first two columns
df = df.iloc[:, 2:]

# Remove the last four columns
df = df.iloc[:, :-4]
# Separate columns into arrays

# Create dummy variables for the third and fourth columns
df = pd.get_dummies(df, columns=['sex', 'ethnicity'])

X = df.values
column_names = df.columns


# Standardize the feature matrix
scaler = StandardScaler()
X_std = scaler.fit_transform(X)

# Perform PCA
pca = PCA()
pca.fit(X_std)

# Print the index of each column in descending order of importance
variance_ratios = pca.explained_variance_ratio_
sorted_indices = np.argsort(variance_ratios)[::-1]
for i in sorted_indices:
    print(f"Column name {column_names[i]} has a variance ratio of {(variance_ratios[i]*100):.2f} %")
