# -*- coding: utf-8 -*-
"""Number Of Children Enrolled in Anganwadi Centres Using EDA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wxPN8wUtZPntTknM97web7Ep2xUnqQWH
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/content/number_of_children_enrolled_in_anganwadis_2023_11.csv'
df = pd.read_csv(file_path)

print("Basic Info about the dataset:")
print(df.info())

print("\nFirst few rows of the dataset:")
print(df.head())

print("\nSummary statistics of numerical columns:")
print(df.describe())

correlation_matrix = df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

# Distribution of the 'Tot_Children_0to6M' column
plt.figure(figsize=(10, 6))
sns.histplot(df['Tot_Children_0to6M'], kde=True, color='blue')
plt.title("Distribution of Tot_Children_0to6M")
plt.xlabel("Number of Children")
plt.ylabel("Frequency")
plt.show()

# Box plot for 'Tot_Children_0to6M' across different categories
plt.figure(figsize=(14, 8))
sns.boxplot(x='D_Name', y='Tot_Children_0to6M', data=df)
plt.title("Boxplot of Tot_Children_0to6M across Districts")
plt.xlabel("District Name")
plt.ylabel("Number of Children")
plt.xticks(rotation=45)
plt.show()