import pandas as pd
# Sample DataFrame
data = {
    'cname': ['Company A', 'Company B', 'Company C', 'Company D'],
    'profit': [1000, -500, 0, 200]
}
df = pd.DataFrame(data)
# Convert 'profit' to True if > 0, else False
df['profit'] = df['profit'] > 0
print(df)
