# analysis.py: Full data exploration, cleaning, and visualization script
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
from wordcloud import WordCloud
import os

# Ensure plots save in current directory
os.makedirs('plots', exist_ok=True)  # Optional: Create a plots folder

print("=== Loading and Exploring CORD-19 Metadata ===")

# Load the dataset (sample 10k rows for speed; adjust as needed)
df = pd.read_csv('metadata.csv', low_memory=False).head(10000)

# Basic info (as requested)
print("Dataset Shape:", df.shape)
print("\nData Types:")
print(df.dtypes)
print("\nBasic Stats:")
print(df.describe(include='all'))

# Check missing values (as requested)
print("\nMissing Values per Column:")
missing = df.isnull().sum()
print(missing[missing > 0].sort_values(ascending=False))

print("\nFirst 5 rows:")
print(df.head())

# Simple visualization example (as in your snippet)
print("\n=== Basic Cleaning ===")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
print("Year column added. Sample years:", df['year'].dropna().unique())

# Drop rows with no title or publish_time, then handle invalid years
df_clean = df.dropna(subset=['title', 'publish_time']).copy()
df_clean['year'] = df_clean['publish_time'].dt.year
df_clean = df_clean.dropna(subset=['year'])
df_clean['year'] = df_clean['year'].astype(int)

print(f"Cleaned Data Shape: {df_clean.shape}")
print("Year Range:", df_clean['year'].min(), "to", df_clean['year'].max())

# Explore key patterns
print("\n=== Key Patterns ===")
year_counts = df_clean['year'].value_counts().sort_index()
print("Publications by Year:\n", year_counts)

top_journals = df_clean['journal'].value_counts().head(10)
print("\nTop 10 Journals:\n", top_journals)

# Note: 'source_x' might vary; use 'source' if needed
source_counts = df_clean.get('source_x', df_clean['source']).value_counts().head(5)
print("\nTop 5 Sources:\n", source_counts)

print("\n=== Generating Visualizations ===")

# Viz 1: Publications by Year (Bar Plot)
plt.figure(figsize=(10, 6))
plt.bar(year_counts.index, year_counts.values, color='skyblue')
plt.title('COVID-19 Publications by Year')
plt.xlabel('Year')
plt.ylabel('Number of Publications')
plt.xticks(year_counts.index)
plt.grid(axis='y', alpha=0.3)
plt.savefig('publications_by_year.png', dpi=300, bbox_inches='tight')
plt.show()  # Optional: Shows plot if running in an IDE with GUI
print("Saved: publications_by_year.png")

# Viz 2: Top Journals (Seaborn Bar Plot)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_journals.values, y=top_journals.index, palette='viridis')
plt.title('Top 10 Journals by Publication Count')
plt.xlabel('Number of Publications')
plt.tight_layout()
plt.savefig('top_journals.png', dpi=300, bbox_inches='tight')
plt.show()
print("Saved: top_journals.png")

# Viz 3: Word Cloud for Titles (Optional)
print("Generating word cloud...")
titles_text = ' '.join(df_clean['title'].dropna().astype(str).tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles_text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Paper Titles')
plt.savefig('title_wordcloud.png', dpi=300, bbox_inches='tight')
plt.show()
print("Saved: title_wordcloud.png")

# Save cleaned data for Streamlit
df_clean.to_csv('cleaned_metadata.csv', index=False)
print("\n=== Done! ===")
print("Cleaned data saved as 'cleaned_metadata.csv'")
print("Plots saved as PNG files.")
print("Run 'python streamlit_app.py' next for the app.")