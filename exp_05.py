# -*- coding: utf-8 -*-
"""Exp_05

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-n0Zpk9vXz8hnjFznxvH0nScpOoMG64g
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('/content/Wholesale customers data.csv')
print(data.isnull().sum())

data.describe()

plt.figure(figsize=(15, 10))
sns.pairplot(data)
plt.suptitle("Pairwise Scatter Plots", y=1.02)  # Adjust the title position
plt.show()

correlation_matrix = data.corr()
print(correlation_matrix)
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

from scipy.cluster.hierarchy import dendrogram, linkage
numerical_df = data.select_dtypes(include=['int64', 'float64'])
linkage_matrix = linkage(numerical_df, method='ward')

plt.figure(figsize=(15, 8))
dendrogram(linkage_matrix, leaf_rotation=90, leaf_font_size=10)
plt.title("Dendrogram")
plt.xlabel("Data Points")
plt.ylabel("Euclidean Distance")
plt.show()

from sklearn.cluster import KMeans

# Select numerical columns for clustering
numerical_df = data[['Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicassen']]

# Initialize an empty list to store the inertia values
inertia = []

# Calculate the inertia for different values of k (number of clusters)
K_range = range(1, 11)  # You can change the range to explore more values
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(numerical_df)
    inertia.append(kmeans.inertia_)

# Plot the elbow graph
plt.figure(figsize=(10, 6))
plt.plot(K_range, inertia, marker='o')
plt.title('Elbow Method For Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia (Sum of Squared Distances)')
plt.grid(True)
plt.show()

from sklearn.cluster import KMeans

numerical_df = data[['Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicassen']]

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # You can change 'n_clusters' as needed
data['Cluster'] = kmeans.fit_predict(numerical_df)

# Display the first few rows to see the assigned clusters
print(data)

columns = numerical_df.columns

for col1, col2 in combinations(columns, 2):
    plt.figure(figsize=(10, 7))
    plt.scatter(numerical_df[col1], numerical_df[col2], c=data['Cluster'], cmap='viridis', marker='o')
    plt.title(f'Scatter Plot: {col1} vs {col2}')
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.colorbar(label='Cluster Label')
    plt.grid(True)
    plt.show()