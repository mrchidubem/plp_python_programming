# Assignment: Data Loading, Analysis, and Visualization with Pandas and Matplotlib
# Dataset: Iris Dataset (loaded from public CSV URL)
# Author: Joseph Chidubem Okafor
# Date: September 20, 2025

# Task 1: Data Loading and Exploration
# Step 1: Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # For enhanced plotting styles
import numpy as np  # For numerical operations

# Step 2: Load the dataset using pandas from a public URL
# URL for Iris CSV: https://gist.githubusercontent.com/netj/8836201/raw/iris.csv
url = 'https://gist.githubusercontent.com/netj/8836201/raw/iris.csv'

try:
    df = pd.read_csv(url)
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: File not found. Please check the URL or download the CSV locally.")
    # Fallback: Exit or load local file; for demo, assume success
except Exception as e:
    print(f"An error occurred while loading the data: {e}")

# Step 3: Display the first few rows using .head()
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Step 4: Explore structure - data types and missing values
print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

# Step 5: Clean the dataset - handle missing values
if df.isnull().any().any():
    # Fill numerical columns with mean
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())
    print("Missing values filled with mean for numerical columns.")
else:
    print("No missing values found. Dataset is clean.")

# Task 2: Basic Data Analysis
# Step 1: Compute basic statistics using .describe()
print("\nBasic statistics of numerical columns:")
print(df.describe())

# Step 2: Groupings - mean of sepal length by species (categorical column)
print("\nMean sepal length by species:")
grouped_means = df.groupby('Species')['Sepal.Length'].mean()
print(grouped_means)

# Step 3: Identify patterns/findings
print("\nObservations and Findings:")
print("- Dataset: 150 iris flower samples across 3 species (setosa, versicolor, virginica).")
print("- Setosa has the shortest average sepal length (~5.0 cm), versicolor ~5.9 cm, virginica ~6.6 cm—indicating size progression.")
print("- Petal measurements show even clearer species separation (setosa smallest).")
print("- Overall, data is balanced (50 samples per species) with low variance within groups.")

# Task 3: Data Visualization
# Step 1: Set style for appealing plots
sns.set_style("whitegrid")

# Step 2: Create subplots for 4 visualizations
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Iris Dataset Visualizations', fontsize=16)

# Plot 1: Bar chart - average sepal length across species (categories)
means = df.groupby('Species')['Sepal.Length'].mean()
colors = ['red', 'green', 'blue']  # One per species
axes[0, 0].bar(means.index, means.values, color=colors)
axes[0, 0].set_title('Average Sepal Length by Species')
axes[0, 0].set_xlabel('Species')
axes[0, 0].set_ylabel('Average Sepal Length (cm)')
axes[0, 0].tick_params(axis='x', rotation=45)

# Plot 2: Histogram - distribution of sepal length (numerical)
axes[0, 1].hist(df['Sepal.Length'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
axes[0, 1].set_title('Distribution of Sepal Length')
axes[0, 1].set_xlabel('Sepal Length (cm)')
axes[0, 1].set_ylabel('Frequency')

# Plot 3: Scatter plot - sepal length vs. sepal width (two numerical, colored by species)
sns.scatterplot(data=df, x='Sepal.Length', y='Sepal.Width', hue='Species', ax=axes[1, 0], palette='viridis')
axes[1, 0].set_title('Sepal Length vs. Sepal Width')
axes[1, 0].set_xlabel('Sepal Length (cm)')
axes[1, 0].set_ylabel('Sepal Width (cm)')
axes[1, 0].legend(title='Species', bbox_to_anchor=(1.05, 1), loc='upper left')

# Plot 4: Line chart - trend of petal length over sample index (simulating time-series)
sample_index = np.arange(len(df))
axes[1, 1].plot(sample_index, df['Petal.Length'], color='purple', linewidth=1, alpha=0.7)
axes[1, 1].set_title('Trend of Petal Length Over Samples')
axes[1, 1].set_xlabel('Sample Index')
axes[1, 1].set_ylabel('Petal Length (cm)')

# Step 3: Adjust layout and display
plt.tight_layout()
plt.show()

# Optional: Save the figure for submission
# plt.savefig('iris_visualizations.png', dpi=300, bbox_inches='tight')

# Final notes
print("\nAssignment complete! All tasks done: loaded/explored/cleaned data, analyzed stats/groupings, and created 4 customized visualizations.")
print("Insights from plots: Bar shows species differences; histogram reveals multimodal distribution (one peak per species); scatter clusters species distinctly; line highlights overall increasing trend in petal lengths across samples.")
