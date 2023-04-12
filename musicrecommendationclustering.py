# -*- coding: utf-8 -*-
"""MusicRecommendationClustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13vt0Au7nE-dbe9IIebsTmOfPApExA3Qn
"""

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df=pd.read_csv('combined.csv')
df

df = df.drop('Track ID' , axis=1)
df.head(5)

X = df[['Danceability', 'Energy', 'Loudness' , 'Liveness']]

# Split the dataset into training and test datasets
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

# Perform clustering on the training dataset
kmeans = KMeans(n_clusters=2)
kmeans.fit(X_train)

# Predict the clusters for the test dataset
y_pred = kmeans.predict(X_test)

# Evaluate the accuracy using a ground truth label (if available)
y_true = df['Liked'].values[:len(X_test)]
accuracy = accuracy_score(y_true, y_pred)
print(accuracy)

# Visualize the clustering results
plt.scatter(X_test['Loudness'], X_test['Energy'], c=y_pred)
plt.title('Clustering Results')
plt.xlabel('Danceability')
plt.ylabel('Energy')
plt.show()
