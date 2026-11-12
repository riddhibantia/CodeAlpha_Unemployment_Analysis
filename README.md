# CodeAlpha Data Science Internship - Task 2: Unemployment Analysis with Python

## 📌 Project Overview
This project analyzes unemployment rate trends across Indian states and geographical zones using Python. Special focus is placed on assessing the economic impact of the **COVID-19 pandemic and national lockdown in 2020**, evaluating seasonal trends, and providing insights for economic policy.

---

## 🛠️ Tech Stack & Libraries
- **Language:** Python
- **Data Preprocessing & Manipulation:** `pandas`, `numpy`
- **Data Visualization:** `matplotlib`, `seaborn`

---

## 🔬 Dataset Overview
The dataset contains monthly economic observations across Indian states:
- **`State`**: Indian states and Union Territories.
- **`Date`**: Monthly observation dates (Jan 2020 – Oct 2020).
- **`Unemployment_Rate`**: Percentage of unemployed individuals in the labor force.
- **`Employed`**: Estimated count of actively employed people.
- **`Labour_Participation_Rate`**: Percentage of working-age population active in the labor market.
- **`Zone`**: Geographic regions (North, South, East, West, North East).

---

## 📊 Key Visualizations & Plots
Saved in the [`plots/`](./plots) directory:
1. **`covid_impact_trend.png`**: Monthly national unemployment trend showing the drastic spike following the March 2020 lockdown.
2. **`statewise_unemployment.png`**: Ranking of Indian states by their average unemployment rate in 2020.
3. **`zonewise_distribution.png`**: Boxplot showing distribution and regional disparities across geographic zones.
4. **`pre_vs_post_lockdown.png`**: Side-by-side bar chart evaluating unemployment pre-lockdown (Jan-Mar) versus lockdown (Apr-Oct).
5. **`correlation_heatmap.png`**: Correlation analysis among unemployment, employment numbers, and labor participation.

---

## 💡 Key Economic Findings & Insights
- **COVID-19 Impact:** Pre-lockdown unemployment averaged **~9.76%**, which surged to **18.75%** during peak lockdown restrictions, peaking at **23.24% in May 2020**.
- **Most Impacted States:** Haryana (27.48%), Tripura (25.05%), Jharkhand (19.54%), Bihar (19.47%), Delhi (18.41%).
- **Most Resilient States:** Meghalaya (3.87%), Assam (4.86%), Gujarat (6.38%), Odisha (6.46%).
- **Policy Recommendations:** State-targeted employment stimulus programs, focus on urban informal sector protections, and regional diversification of industries.

---

## 🚀 How to Run
```bash
# 1. Navigate to the task directory
cd Task_2_Unemployment_Analysis

# 2. Run the analysis script
python unemployment_analysis.py
```
