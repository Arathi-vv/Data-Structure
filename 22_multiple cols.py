import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Bob', 'Alice'],
    'Age': [25, 30, 35, 22, 25],
    'Score': [85, 90, 95, 80, 85]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
sorted_df = df.sort_values(by=['Name', 'Age'], ascending=[True, False])
print("\nDataFrame sorted by 'Name' ascending and 'Age' descending:")
print(sorted_df)
