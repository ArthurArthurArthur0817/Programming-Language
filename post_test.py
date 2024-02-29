import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('adult.csv')

print(df)

mean_salary = np.mean(df['Income'])  
std_salary = np.std(df['Income'])   
median_salary = np.median(df['Income'])  
print("平均值：", mean_salary)
print("標準差：", std_salary)
print("中位數：", median_salary)


income_bins = [0, 50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000]


df['Income_Group'] = pd.cut(df['Income'], bins=income_bins)


income_counts = df['Income_Group'].value_counts().sort_index()


plt.bar(income_counts.index.astype(str), income_counts.values, color='skyblue', edgecolor='black')
plt.xlabel('Income Range')
plt.ylabel('Number of Individuals')
plt.title('Income Distribution')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.subplots_adjust(bottom=0.25)
plt.show()