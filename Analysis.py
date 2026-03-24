# ============================================================
# Global Suicide Rates Analysis | By Country | 2000–2021
# ------------------------------------------------------------
# Author  : Anindya Adhikari
# Purpose : Exploratory data analysis of global suicide rates
#           across countries, years, age groups, and gender
# ============================================================


# ── Import Libraries ─────────────────────────────────────────
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8')


# ── Load Dataset ──────────────────────────────────────────────
df = pd.read_csv(
    r"C:\Users\anind\OneDrive\Desktop\PythonVSC\Project\Global Suicide Rates Analysis\data\global-suicide-rates-by-country-2000-2021.csv",
    encoding='latin-1'
)
print("Dataset Loaded Successfully!\n")


# ── Q1 : Load and Inspect the Dataset ────────────────────────
# Preview the first and last rows, column types, and dataset dimensions


print(df.head(51))
print(df.tail(51))
print(df.info())
print(df.shape)



# ── Q2 : Check for Missing Values and Duplicates ─────────────
# Identify any null entries and remove duplicate records


print(df.isnull().sum())
df.duplicated().sum()
df.drop_duplicates(inplace=True)



# ── Q3 : Verify Data Consistency ─────────────────────────────
# Confirm unique categories in key categorical columns
# and validate the year range of the dataset


print(df['sex'].unique())
print(df['age_group'].value_counts())
print(df['country'].value_counts())
print("Year Range:", df['year'].min(), "–", df['year'].max())



# ── Q4 : Filter Dataset for Aggregate Population ─────────────
# Retain records where age group is 'ALL' and sex is 'both'
# to work with the overall population-level data


df_aggregated = df[(df['age_group'] == 'ALL') & (df['sex'] == 'both')]
print(df_aggregated)



# ── Q5 : Compute Global Descriptive Statistics ───────────────
# Calculate mean, median, standard deviation, minimum,
# and maximum of the global suicide rate


print("\nGlobal Suicide Rate — Descriptive Statistics")
print("-" * 45)

global_mean   = df['suicide_rate'].mean()
global_median = df['suicide_rate'].median()
global_std    = df['suicide_rate'].std()
global_min    = df['suicide_rate'].min()
global_max    = df['suicide_rate'].max()

print(f"Mean              : {global_mean:.2f}")
print(f"Median            : {global_median:.2f}")
print(f"Standard Deviation: {global_std:.2f}")
print(f"Minimum           : {global_min:.2f}")
print(f"Maximum           : {global_max:.2f}")



# ── Q6 : Country-Level Suicide Rate Ranking ──────────────────
# Compute the average suicide rate per country
# and identify the top 10 highest and lowest countries


country_avg_rate = df.groupby('country')['suicide_rate'].mean().sort_values()

print("Top 10 Countries — Highest Average Suicide Rate:")
print(country_avg_rate.tail(10))

country_avg_rate.tail(10).plot(kind='barh', title='Top 10 Countries by Avg Suicide Rate')
plt.xlabel("Average Suicide Rate")
plt.tight_layout()
plt.show()



# ── Q7 : Yearly Global Trend — Average Suicide Rate ──────────
# Compute and display the worldwide average suicide rate
# for each year from 2000 to 2021


yearly_avg_rate = df.groupby('year')['suicide_rate'].mean()

print("Average Suicide Rate per Year:")
print(yearly_avg_rate)

yearly_avg_rate.tail(10).plot(kind='bar', title='Yearly Average Suicide Rate (Last 10 Years)')
plt.xlabel("Year")
plt.ylabel("Average Suicide Rate")
plt.tight_layout()
plt.show()



# ── Q9 : Global Trend Line Plot ──────────────────────────────
# Visualise the global average suicide rate over time
# using a continuous line graph


global_trend = df.groupby('year')['suicide_rate'].mean()

plt.figure(figsize=(10, 5))
plt.plot(global_trend.index, global_trend.values, marker='o', linewidth=2)
plt.title("Global Average Suicide Rate Over Time (2000–2021)")
plt.xlabel("Year")
plt.ylabel("Average Suicide Rate")
plt.tight_layout()
plt.show()



# ── Q10 : Suicide Rate Comparison by Sex ─────────────────────
# Compare the average suicide rate across male,
# female, and both categories using a bar chart


sex_avg_rate = df.groupby('sex')['suicide_rate'].mean()

plt.figure(figsize=(7, 5))
plt.bar(sex_avg_rate.index, sex_avg_rate.values, color=['steelblue', 'salmon', 'mediumseagreen'])
plt.title("Average Suicide Rate by Sex")
plt.xlabel("Sex")
plt.ylabel("Average Suicide Rate")
plt.tight_layout()
plt.show()



# ── Q11 : Multi-Country Trend Comparison ─────────────────────
# Plot suicide rate trends for five selected countries
# on the same graph to enable direct visual comparison


selected_countries = ['India', 'United States', 'Japan', 'Australia', 'Russia']
df_selected = df[df['country'].isin(selected_countries)]

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_selected, x='year', y='suicide_rate', hue='country')
plt.title("Suicide Rate Trends — Selected Countries (2000–2021)")
plt.xlabel("Year")
plt.ylabel("Suicide Rate")
plt.tight_layout()
plt.show()



# ── Q12 : Gender Gap Analysis by Country ─────────────────────
# Compute the difference between male and female suicide rates
# for each country and identify those with the largest gender gap


df_pivot_sex = df[df['age_group'] == 'ALL'].pivot_table(
    index=['country', 'year'],
    columns='sex',
    values='suicide_rate'
)
df_pivot_sex['gender_gap'] = df_pivot_sex['male'] - df_pivot_sex['female']

country_gender_gap = df_pivot_sex.groupby('country')['gender_gap'].mean()

print("Top 10 Countries — Largest Gender Gap in Suicide Rate:")
print(country_gender_gap.sort_values(ascending=False).head(10))



# ── Q13 : Age Group Analysis — Global Average ────────────────
# Identify which age group carries the highest average
# suicide rate worldwide, excluding the aggregate 'ALL' category


df_by_age = df[df['age_group'] != 'ALL']
age_group_avg_rate = df_by_age.groupby('age_group')['suicide_rate'].mean()

print("Average Suicide Rate by Age Group:")
print(age_group_avg_rate.sort_values(ascending=False))



# ── Q14 : Global Suicide Rate Trend by Year (Bar Chart) ──────
# Visualise how the global average suicide rate has changed
# year over year from 2000 to 2021


yearly_global_trend = df.groupby('year')['suicide_rate'].mean()

plt.figure(figsize=(12, 5))
plt.bar(yearly_global_trend.index, yearly_global_trend.values, color='steelblue')
plt.title("Global Average Suicide Rate by Year (2000–2021)")
plt.xlabel("Year")
plt.ylabel("Average Suicide Rate")
plt.tight_layout()
plt.show()



# ── Q17 : Distribution of Suicide Rates — Histogram + KDE ───
# Plot the distribution of all suicide rate values globally
# using a histogram overlaid with a kernel density estimate


plt.figure(figsize=(10, 5))
sns.histplot(df['suicide_rate'], kde=True, color='steelblue', bins=40)
plt.title("Distribution of Global Suicide Rates")
plt.xlabel("Suicide Rate")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()



# ── Q18 : Correlation Between Male and Female Suicide Rates ──
# Pivot the dataset to place male and female rates in separate
# columns and compute their pairwise correlation coefficient


df_pivot_corr = df[df['age_group'] == 'ALL'].pivot_table(
    index=['country', 'year'],
    columns='sex',
    values='suicide_rate'
)
correlation_matrix = df_pivot_corr[['male', 'female']].corr()

print("Correlation Matrix — Male vs Female Suicide Rate:")
print(correlation_matrix)



# ── Q19 : Top 5 High-Risk Countries in Recent Years ──────────
# Filter data for the last 5 available years
# and rank countries by their average suicide rate


df_recent_filter = df[
    (df['age_group'] == 'ALL') &
    (df['sex'].isin(['male', 'female', 'transgender']))
]

latest_year        = df_recent_filter['year'].max()
df_recent_5yr      = df_recent_filter[df_recent_filter['year'] >= latest_year - 4]

top5_high_risk = (
    df_recent_5yr.groupby('country')['suicide_rate']
                 .mean()
                 .sort_values(ascending=False)
                 .head(5)
)

print("Top 5 High-Risk Countries (Last 5 Years):")
print(top5_high_risk)

plt.figure(figsize=(8, 5))
top5_high_risk.plot(kind='bar', color='tomato')
plt.title("Top 5 High-Risk Countries (Recent 5 Years)")
plt.ylabel("Average Suicide Rate")
plt.xlabel("Country")
plt.tight_layout()
plt.show()



# ── Q20 : Countries That Improved the Most ───────────────────
# Compare early-period (first 5 years) vs recent-period (last 5 years)
# average suicide rates per country and rank by the greatest decline

df_improvement_filter = df[
    (df['age_group'] == 'ALL') &
    (df['sex'].isin(['male', 'female', 'transgender']))
]

# Define the early and recent time windows
earliest_year = df_improvement_filter['year'].min()
latest_year   = df_improvement_filter['year'].max()

df_early_period  = df_improvement_filter[df_improvement_filter['year'] <= earliest_year + 4]
df_recent_period = df_improvement_filter[df_improvement_filter['year'] >= latest_year - 4]

# Compute the per-country average for each period
early_period_avg  = df_early_period.groupby('country')['suicide_rate'].mean()
recent_period_avg = df_recent_period.groupby('country')['suicide_rate'].mean()

# Improvement score = reduction in suicide rate over the two periods
rate_improvement = early_period_avg - recent_period_avg
top10_most_improved = rate_improvement.sort_values(ascending=False).head(10)

print("Top 10 Countries — Largest Decrease in Suicide Rate (2000–2021):")
print(top10_most_improved)

plt.figure(figsize=(10, 6))
top10_most_improved.plot(kind='bar', color='mediumseagreen')
plt.title("Countries That Improved the Most (2000–2021)")
plt.ylabel("Decrease in Suicide Rate")
plt.xlabel("Country")
plt.tight_layout()
plt.show()