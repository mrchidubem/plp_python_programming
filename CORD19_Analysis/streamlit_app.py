import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="CORD-19 Analysis", layout="wide")

# Title
st.title("CORD-19 Research Dataset Insights")
st.markdown("A simple analysis of COVID-19 publications from the metadata.csv file.")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('cleaned_metadata.csv')

df = load_data()

# Sidebar for filters
st.sidebar.header("Filters")
min_year = st.sidebar.slider("Min Year", df['year'].min(), df['year'].max(), df['year'].min())
max_year = st.sidebar.slider("Max Year", min_year, df['year'].max(), df['year'].max())
filtered_df = df[(df['year'] >= min_year) & (df['year'] <= max_year)]

# Key Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Publications", len(df))
col2.metric("Publications in Range", len(filtered_df))
col3.metric("Year Range", f"{min_year}–{max_year}")

# Publications by Year Plot
st.subheader("Publications by Year")
fig, ax = plt.subplots(figsize=(10, 5))
year_counts = filtered_df['year'].value_counts().sort_index()
ax.bar(year_counts.index, year_counts.values, color='skyblue')
ax.set_title('Publications by Year (Filtered)')
ax.set_xlabel('Year')
ax.set_ylabel('Count')
st.pyplot(fig)

# Top Journals Plot
st.subheader("Top 10 Journals")
fig2, ax2 = plt.subplots(figsize=(10, 6))
top_journals = filtered_df['journal'].value_counts().head(10)
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax2, palette='viridis')
ax2.set_title('Top 10 Journals by Publication Count (Filtered)')
ax2.set_xlabel('Count')
st.pyplot(fig2)

# Sample Titles Table
st.subheader("Sample Paper Titles")
st.dataframe(filtered_df[['title', 'journal', 'year']].head(10), use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Built with Streamlit | Data from CORD-19 Dataset")