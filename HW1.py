import pandas as pd

# 讀取CSV檔
df = pd.read_csv('social_media.csv')

# 聯集
union_set = set()
for continent in df.columns:
    union_set.update(df[continent])

print("聯集:", union_set)

# 交集
intersection_set = set(df[df.columns[0]])
for continent in df.columns[1:]:
    intersection_set.intersection_update(set(df[continent]))

print("交集:", intersection_set)

# 差集
difference_set = set(df[df.columns[0]])
for continent in df.columns[1:]:
    difference_set.difference_update(set(df[continent]))

print("差集:", difference_set)
