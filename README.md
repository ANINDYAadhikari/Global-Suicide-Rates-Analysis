
**Author:** Anindya Adhikari

---

## 📌 Project Overview

This project performs an in-depth **Explatory Data Analysis (EDA)** on global suicide rates across multiple countries from **2000 to 2021**.

The goal is to uncover meaningful patterns, trends, and disparities based on:

* 🌎 Country
* 📅 Year
* 👥 Age Group
* 🚻 Gender

The analysis combines **statistical summaries** with **data visualizations** to provide insights into global mental health trends.



## 🎯 Objectives

* Understand global suicide rate patterns over time
* Identify **high-risk countries**
* Analyze **gender disparities** in suicide rates
* Compare trends across selected countries
* Discover which **age groups are most affected**
* Measure **improvements or declines** over time



## 🗂️ Dataset

* **Source:** Global Suicide Rates by Country (2000–2021)
* **Format:** CSV
* **Encoding:** Latin-1

### Key Features:

* `country`
* `year`
* `sex`
* `age_group`
* `suicide_rate`



## ⚙️ Technologies Used

* **Python 🐍**
* **Pandas** – Data manipulation
* **NumPy** – Numerical operations
* **Matplotlib** – Visualization
* **Seaborn** – Statistical plotting



## 🔍 Analysis Workflow

### 1️⃣ Data Loading & Inspection

* Loaded dataset using Pandas
* Checked structure, data types, and dimensions
* Previewed head & tail



### 2️⃣ Data Cleaning

* Checked for **missing values**
* Removed **duplicate records**



### 3️⃣ Data Validation

* Verified:

  * Unique genders
  * Age groups
  * Country distribution
* Confirmed year range (2000–2021)



### 4️⃣ Aggregated Dataset

Filtered data for:

* `age_group = ALL`
* `sex = both`

➡️ Used for population-level analysis



## 📈 Key Insights & Analysis

### 🌍 Global Statistics

* Mean, Median, Standard Deviation
* Minimum & Maximum suicide rates



### 🏆 Country Rankings

* Top 10 countries with **highest suicide rates**
* Visualized using horizontal bar charts



### 📅 Yearly Trends

* Global suicide rate trends over time
* Line plots and bar charts for trend visualization



### 🚻 Gender Analysis

* Compared suicide rates:

  * Male
  * Female
  * Combined

➡️ Highlighted significant gender gaps



### 🌎 Multi-Country Comparison

Compared trends for:

* India 🇮🇳
* United States 🇺🇸
* Japan 🇯🇵
* Australia 🇦🇺
* Russia 🇷🇺



### ⚖️ Gender Gap Analysis

* Calculated difference:
  `Male Rate - Female Rate`
* Identified countries with **largest disparities**



### 👥 Age Group Insights

* Determined most vulnerable age groups
* Excluded aggregated data for precision



### 📊 Distribution Analysis

* Histogram + KDE plot
* Showed overall distribution of suicide rates



### 🔗 Correlation Study

* Measured correlation between:

  * Male vs Female suicide rates



### 🚨 High-Risk Countries (Recent Years)

* Identified top 5 countries (last 5 years)
* Focus on recent trends



### 📉 Improvement Analysis

* Compared:

  * Early period (first 5 years)
  * Recent period (last 5 years)

➡️ Highlighted countries with **greatest improvement**



## 📊 Visualizations Included

* 📉 Line plots (trend analysis)
* 📊 Bar charts (comparisons & rankings)
* 📦 Histograms with KDE
* 🌐 Multi-line country comparisons



## 📂 Project Structure

ecommerce-sales-analysis/
│
├── Code/
│   └── Analysis.py
│
├── Data/
│   └── global-suicide-rates-by-country-2000-2021.csv
│
├── Images/
│   ├── code/
│   └── plots/
│
└── README.md
