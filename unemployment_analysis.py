import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    print("=" * 70)
    print("CodeAlpha Data Science Internship - Task 2: Unemployment Analysis")
    print("=" * 70)

    # 1. Load Data
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(base_dir, "Unemployment_Rate_upto_11_2020.csv")

    df = pd.read_csv(csv_file)
    print(f"\n[+] Loaded Dataset: {csv_file}")
    print(f"Shape: {df.shape}")

    # 2. Data Cleaning & Standardization
    # Strip whitespace from column headers
    df.columns = df.columns.str.strip()
    
    # Rename columns for ease of use
    df.rename(columns={
        'Region': 'State',
        'Region.1': 'Zone',
        'Estimated Unemployment Rate (%)': 'Unemployment_Rate',
        'Estimated Employed': 'Employed',
        'Estimated Labour Participation Rate (%)': 'Labour_Participation_Rate'
    }, inplace=True)

    # Parse Dates and extract Month/Year
    df['Date'] = pd.to_datetime(df['Date'].str.strip(), format='%d-%m-%Y')
    df['Month'] = df['Date'].dt.month_name()
    df['Month_Num'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year

    print("\nCleaned Column Names:")
    print(df.columns.tolist())

    print("\nMissing values check:")
    print(df.isnull().sum())

    print("\nStatistical Summary:")
    print(df[['Unemployment_Rate', 'Employed', 'Labour_Participation_Rate']].describe().T)

    # 3. Create Plots Directory
    plots_dir = os.path.join(base_dir, "plots")
    os.makedirs(plots_dir, exist_ok=True)
    sns.set_theme(style="whitegrid")

    # ----------------------------------------------------
    # Plot 1: Overall Monthly Unemployment Trend (COVID Impact)
    # ----------------------------------------------------
    monthly_trend = df.groupby('Date')['Unemployment_Rate'].mean().reset_index()

    plt.figure(figsize=(10, 5))
    plt.plot(monthly_trend['Date'], monthly_trend['Unemployment_Rate'], marker='o', color='firebrick', linewidth=2.5)
    plt.axvline(pd.to_datetime('2020-03-25'), color='black', linestyle='--', label='COVID-19 Lockdown (March 2020)')
    plt.title('Monthly Average Unemployment Rate in India (2020) - COVID-19 Impact', fontsize=14, fontweight='bold')
    plt.xlabel('Date')
    plt.ylabel('Unemployment Rate (%)')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "covid_impact_trend.png"), dpi=300)
    plt.close()

    # ----------------------------------------------------
    # Plot 2: State-wise Average Unemployment Rate
    # ----------------------------------------------------
    state_avg = df.groupby('State')['Unemployment_Rate'].mean().sort_values(ascending=False).reset_index()

    plt.figure(figsize=(12, 8))
    sns.barplot(data=state_avg, x='Unemployment_Rate', y='State', hue='State', palette='rocket', legend=False)
    plt.title('Average Unemployment Rate by State (2020)', fontsize=14, fontweight='bold')
    plt.xlabel('Average Unemployment Rate (%)')
    plt.ylabel('State')
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "statewise_unemployment.png"), dpi=300)
    plt.close()

    # ----------------------------------------------------
    # Plot 3: Zone-wise Comparison
    # ----------------------------------------------------
    plt.figure(figsize=(9, 5))
    sns.boxplot(data=df, x='Zone', y='Unemployment_Rate', hue='Zone', palette='Set2', legend=False)
    plt.title('Unemployment Rate Distribution across Geographic Zones', fontsize=14, fontweight='bold')
    plt.xlabel('Geographic Zone')
    plt.ylabel('Unemployment Rate (%)')
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "zonewise_distribution.png"), dpi=300)
    plt.close()

    # ----------------------------------------------------
    # Plot 4: Correlation Matrix Heatmap
    # ----------------------------------------------------
    numeric_cols = ['Unemployment_Rate', 'Employed', 'Labour_Participation_Rate', 'longitude', 'latitude']
    plt.figure(figsize=(8, 6))
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Heatmap of Economic Indicators', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "correlation_heatmap.png"), dpi=300)
    plt.close()

    # ----------------------------------------------------
    # Plot 5: Pre-Lockdown vs. Lockdown Period Comparison
    # ----------------------------------------------------
    # Lockdown declared late March 2020 (Month >= 4 April, May, June vs Jan-Mar)
    df['Period'] = np.where(df['Date'] < '2020-04-01', 'Pre-Lockdown (Jan-Mar)', 'Post/During Lockdown (Apr-Oct)')

    period_comp = df.groupby(['Zone', 'Period'])['Unemployment_Rate'].mean().unstack()

    plt.figure(figsize=(10, 6))
    period_comp.plot(kind='bar', figsize=(10, 6), colormap='viridis', edgecolor='black')
    plt.title('Unemployment Rate: Pre-Lockdown vs. During Lockdown across Zones', fontsize=13, fontweight='bold')
    plt.ylabel('Average Unemployment Rate (%)')
    plt.xlabel('Zone')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "pre_vs_post_lockdown.png"), dpi=300)
    plt.close()

    print(f"\n[+] All visual plots generated and saved in: {plots_dir}")

    # 4. Key Insights Summary
    top_affected_states = state_avg.head(5)
    least_affected_states = state_avg.tail(5)

    peak_month = monthly_trend.loc[monthly_trend['Unemployment_Rate'].idxmax()]
    pre_lockdown_mean = df[df['Date'] < '2020-04-01']['Unemployment_Rate'].mean()
    lockdown_mean = df[(df['Date'] >= '2020-04-01') & (df['Date'] <= '2020-06-30')]['Unemployment_Rate'].mean()

    print("\n" + "=" * 70)
    print("KEY ECONOMIC FINDINGS & INSIGHTS")
    print("=" * 70)
    print(f"1. Pre-Lockdown National Average Unemployment: {pre_lockdown_mean:.2f}%")
    print(f"2. Peak Lockdown National Average Unemployment (Apr-Jun): {lockdown_mean:.2f}%")
    print(f"   -> An alarming increase of +{lockdown_mean - pre_lockdown_mean:.2f}% during peak COVID restrictions.")
    print(f"3. National Peak Month: {peak_month['Date'].strftime('%B %Y')} with average {peak_month['Unemployment_Rate']:.2f}%")
    print("\nTop 5 Most Impacted States (Highest Average Unemployment):")
    for idx, row in top_affected_states.iterrows():
        print(f"   - {row['State']}: {row['Unemployment_Rate']:.2f}%")

    print("\nTop 5 Least Impacted States (Lowest Average Unemployment):")
    for idx, row in least_affected_states.iterrows():
        print(f"   - {row['State']}: {row['Unemployment_Rate']:.2f}%")

    print("\n" + "=" * 70)
    print("[OK] Task 2: Unemployment Analysis executed successfully!")
    print("=" * 70)

if __name__ == "__main__":
    main()
