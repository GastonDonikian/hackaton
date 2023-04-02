import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import cdist

# Read data from CSV file
df = pd.read_csv('dataFilterByUs.csv')
# Remove the first two columns
df = df.iloc[:, 2:]

# Remove the last four columns
df = df.iloc[:, :-5]
# Separate columns into arrays

# Create dummy variables for the third and fourth columns
df = pd.get_dummies(df, columns=['sex', 'ethnicity'])

X = df.values
column_names = df.columns


# Standardize the feature matrix
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
print(column_names)
print(X_std)
# Perform PCA
pca = PCA()
pca.fit(X_std)

def get_trait_weights():


    # Print the index of each column in descending order of importance
    variance_ratios = pca.explained_variance_ratio_
    sorted_indices = np.argsort(variance_ratios)[::-1]
    answer = {}
    for i in sorted_indices:
        answer[column_names[i]] = variance_ratios[i]
        # print(f"Column name {column_names[i]} has a variance ratio of {(variance_ratios[i]*100):.2f} %")
    # print(answer)
    return answer


# Function to return 10 nearest points to a given input
def get_nearest_points(input_point):
    input_std = scaler.transform([input_point])
    input_pca = pca.transform(input_std)
    distances = cdist(input_pca, pca.transform(X_std), 'euclidean')
    nearest_indices = np.argsort(distances)[0][:10]
    nearest_points = X[nearest_indices]
    nearest_distances = distances[0][nearest_indices]
    return nearest_points, nearest_distances


# Example usage of the function
# print(get_trait_weights())
input_point = [70,0,4,10,2,1,0,1, 0,0,0]
nearest_points, nearest_distances = get_nearest_points(input_point)
print(f"The 10 nearest points to {input_point} are:\n{nearest_points}")
print(f"The distances of the 10 nearest points are:\n{nearest_distances}")