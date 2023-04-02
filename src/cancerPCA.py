import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import cdist






# Function to return 10 nearest points to a given input
def get_nearest_points(input_point):
        # Read data from CSV file
    df = pd.read_csv('dataFilterByUs.csv')
    df = df[df['cancerType'] == input_point['cancerType']]
    all_data = pd.read_csv('dataFilterByUs.csv').values
    
    input_point = [input_point['age'],input_point['mentalHealth'],input_point['generalHealth'],input_point['tumorSize'],input_point['cancerStage'],1 if input_point['sex'] == 0 else 0, 1 if input_point['sex'] == 1 else 0,
                             1 if input_point['ethnicity'] == 0 else 0,1 if input_point['ethnicity'] == 1 else 0,1 if input_point['ethnicity'] == 2 else 0,1 if input_point['ethnicity'] == 3 else 0]

    # Remove the first two columns
    print(df)
    df = df.iloc[:, 2:]

    # Remove the last four columns
    df = df.iloc[:, :-5]
    # Separate columns into arrays

    # Create dummy variables for the third and fourth columns
    df = pd.get_dummies(df, columns=['sex', 'ethnicity'])

    X = df.values
    column_names = df.columns
    print(column_names)

    # Standardize the feature matrix
    scaler = StandardScaler()
    X_std = scaler.fit_transform(X)
    # Perform PCA
    pca = PCA()
    pca.fit(X_std)
    
    input_std = scaler.transform([input_point])
    input_pca = pca.transform(input_std)
    distances = cdist(input_pca, pca.transform(X_std), 'euclidean')
    nearest_indices = np.argsort(distances)[0][:10]
    nearest_points = all_data[nearest_indices]
    nearest_distances = distances[0][nearest_indices]
    max_distance = np.max(nearest_distances)
    similarities = np.round((max_distance - nearest_distances) / max_distance * 100, 2)
    nearest_points = np.concatenate((nearest_points, np.array(similarities)[:, np.newaxis]), axis=1)
    return nearest_points

# # Example usage of the function
# input_point = {'age':70, 'sex':0,'ethnicity':1,'mentalHealth':4,'generalHealth':10,'tumorSize':10,'cancerType':0,'cancerStage':1}
# nearest_points = get_nearest_points(input_point)

# print(f"The 10 nearest points to {input_point} are:\n{nearest_points}\n")