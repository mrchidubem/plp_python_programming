# Frameworks_Assignment: CORD-19 Analysis

## Overview
Analyzes CORD-19 metadata.csv with pandas, visualizations, and Streamlit.

## Workflow
1. Run `python analysis.py` for exploration, cleaning, and plots.
2. Run `streamlit run streamlit_app.py` for interactive app.

## Key Insights
- Publication spike in 2020.
- Top journals: medRxiv, etc.
- Cleaning: Handled ~5% missing core fields.

## Files
- `analysis.py`: Loads, cleans, prints stats, saves plots/CSV.
- `streamlit_app.py`: Interactive dashboard.
- `cleaned_metadata.csv`: Processed data.
- PNGs: Visualizations.

## Setup
pip install -r requirements.txt
Download metadata.csv from Kaggle.
Run analysis.py first.

## Visualizations
![Publications by Year](publications_by_year.png)
![Top Journals](top_journals.png)