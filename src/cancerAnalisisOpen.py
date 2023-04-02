import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from minisom import MiniSom
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Read data from CSV file
df = pd.read_csv('./dataFilterByUs.csv')
print(df)
# Remove rows with NaN values
df = df.dropna()
# Separate columns into arrays
grades = df['grade'].values
tumor_sizes = df['tumorSize'].values
ages = df['age'].values

# Concatenate arrays into feature matrix
X = np.column_stack((grades, tumor_sizes, ages))
scaler = StandardScaler()
X = scaler.fit_transform(X)
# Perform PCA
pca = PCA(n_components=2)
pca.fit(X)
X_pca = pca.transform(X)

# Plot PCA results
plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()

# Perform Kohonen Map
som = MiniSom(x=10, y=10, input_len=3, sigma=1.0, learning_rate=0.5)

# Initialize weights with random values
som.random_weights_init(X)

# Train the map with input data
som.train_random(data=X, num_iteration=100)

# Plot the Kohonen Map
plt.pcolor(som.distance_map().T, cmap='bone_r')
plt.colorbar()

for i, x in enumerate(X):
    if not np.isnan(x).any():
        w = som.winner(x)
        plt.plot(w[0]+0.5, w[1]+0.5, 'o', markerfacecolor='None', markeredgecolor='red', markersize=10, markeredgewidth=2)

# Add a custom point to the plot
custom_point = [1.2, 2.4, 3.6]  # Custom point in feature space
custom_point_norm = scaler.transform([custom_point])  # Normalize custom point
w = som.winner(custom_point_norm[0])  # Determine winner neuron for custom point
plt.plot(w[0]+0.5, w[1]+0.5, 'o', markerfacecolor='blue', markersize=10, markeredgewidth=2)


weights = som.get_weights()
winning_weights = weights[w[0], w[1]]
distances = np.linalg.norm(weights - winning_weights, axis=-1)
nearest_neurons = np.argsort(distances)[:10]
nearest_points = [weights[i][j] for i, j in np.unravel_index(nearest_neurons, (10, 10))]

print("The ten nearest points to the custom point are:")
print(nearest_points)


plt.show()