import pandas as pd
import numpy as np


df = pd.read_csv('adult.csv')

print(df)

mean_salary = np.mean(df['Income'])  
std_salary = np.std(df['Income'])   
median_salary = np.median(df['Income'])  
print("平均值：", mean_salary)
print("標準差：", std_salary)
print("中位數：", median_salary)
