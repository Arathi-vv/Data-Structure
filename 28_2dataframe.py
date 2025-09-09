import pandas as pd
# DataFrame 1: employee details
df1 = pd.DataFrame({
    'eid': [101, 102, 103],
    'ename': ['Alice', 'Bob', 'Charlie'],
    'stipend': [1000, 1500, 1200]
})
# DataFrame 2: employee designation
df2 = pd.DataFrame({
    'eid': [101, 102, 103],
    'designation': ['Manager', 'Developer', 'Analyst']
})
# Merge on 'eid'
merged_df = pd.merge(df1, df2, on='eid')# Rename 'designation' to 'position' if needed
merged_df.rename(columns={'designation': 'position'}, inplace=True)

print(merged_df)
