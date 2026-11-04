import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("🚀 Starting Data Analysis Pipeline...\n")

# 1. LOAD THE DATA
df = pd.read_csv('sales_data.csv')
print("--- Raw Data Outline ---")
print(df.info(), "\n")

# 2. DATA CLEANING
# Fill missing Units_Sold with the median value
df['Units_Sold'] = df['Units_Sold'].fillna(df['Units_Sold'].median())
# Fill missing Unit_Price with the average price for its category
df['Unit_Price'] = df['Unit_Price'].fillna(df.groupby('Product_Category')['Unit_Price'].transform('mean'))

# 3. FEATURE ENGINEERING (Calculating Key Business Metrics)
df['Total_Revenue'] = df['Units_Sold'] * df['Unit_Price']
df['Total_Cost'] = df['Units_Sold'] * df['Unit_Cost']
df['Total_Profit'] = df['Total_Revenue'] - df['Total_Cost']
df['Profit_Margin_%'] = (df['Total_Profit'] / df['Total_Revenue']) * 100

print("--- Cleaned Data with Metrics ---")
print(df[['Product_Category', 'Total_Revenue', 'Total_Profit', 'Profit_Margin_%']], "\n")

# 4. DATA AGGREGATION (Answering Business Questions)
print("--- Total Profit by Product Category ---")
category_perf = df.groupby('Product_Category')['Total_Profit'].sum().reset_index()
print(category_perf, "\n")

print("--- Regional Revenue Breakdown ---")
region_perf = df.groupby('Region')['Total_Revenue'].sum().reset_index()
print(region_perf, "\n")

# 5. DATA VISUALISATION
plt.figure(figsize=(8, 5))
plt.bar(category_perf['Product_Category'], category_perf['Total_Profit'], color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.title('Total Profit by Product Category (2026)')
plt.xlabel('Product Category')
plt.ylabel('Total Profit ($)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save chart as an image file for GitHub documentation
plt.savefig('profit_by_category.png')
print("📊 Visualisation saved successfully as 'profit_by_category.png'!")
print("\n✅ Pipeline complete, code executed perfectly.")
