import pandas as pd

# 讀取CSV檔
df = pd.read_csv('social_media.csv')

# 聯集
union_set = set()
for continent in df.columns:
    union_set.update(df[continent])

print("各洲所有常用社群媒體(聯集):", union_set)

# 交集
intersection_set = set(df[df.columns[0]])
for continent in df.columns[1:]:
    intersection_set.intersection_update(set(df[continent]))

print("各洲都在用的社群媒體(交集):", intersection_set)

# 差集
difference_set = set(df[df.columns[0]])
for continent in df.columns[1:]:
    difference_set.difference_update(set(df[continent]))

print("只有部分洲使用的社群媒體(差集):", difference_set)
