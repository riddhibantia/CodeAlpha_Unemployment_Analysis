# Unemployment Analysis with Python

This project was built for the CodeAlpha Data Science Internship. It analyzes unemployment trends across Indian states with a focus on understanding the economic impact of the 2020 COVID-19 lockdown.

## Dataset
The dataset tracks monthly unemployment data across Indian states up to November 2020.
Key columns include:
- `State`: State/UT name
- `Date`: Monthly observation date
- `Unemployment_Rate`: Estimated unemployment rate (%)
- `Employed`: Estimated employed population
- `Labour_Participation_Rate`: Labour participation rate (%)
- `Zone`: Region (North, South, East, West, North East)

## Analysis Highlights
1. **Trend Analysis**: Studied how unemployment numbers changed before and during lockdown restrictions.
2. **State Comparisons**: Compared states by average unemployment rate throughout 2020.
3. **Regional Distribution**: Looked at variations across different geographic zones.
4. **Correlation**: Checked relationships between unemployment, employment counts, and labor participation.

## Observations
- National average unemployment hovered around **9.76%** pre-lockdown and climbed to **18.75%** during the initial lockdown months, peaking in **May 2020 at 23.24%**.
- Northern and Eastern states showed higher spikes compared to Southern and Western states.
- Plots are saved in the `plots/` folder:
  - `covid_impact_trend.png`: Monthly trend showing the lockdown spike.
  - `statewise_unemployment.png`: States ranked by average unemployment.
  - `zonewise_distribution.png`: Boxplot across geographic regions.
  - `pre_vs_post_lockdown.png`: Before vs. during lockdown comparison.
  - `correlation_heatmap.png`: Feature correlation matrix.

## Project Structure
```
├── plots/
│   ├── covid_impact_trend.png
│   ├── statewise_unemployment.png
│   ├── zonewise_distribution.png
│   ├── pre_vs_post_lockdown.png
│   └── correlation_heatmap.png
├── unemployment_analysis.py
├── Unemployment_Analysis.ipynb
├── Unemployment_Rate_upto_11_2020.csv
├── requirements.txt
└── README.md
```

## How to Run
```bash
pip install -r requirements.txt
python unemployment_analysis.py
```
Or open `Unemployment_Analysis.ipynb` in Jupyter Notebook or Google Colab.
