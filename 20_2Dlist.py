import pandas as pd
data = [
    [1, 'Alice', 25],
    [2, 'Bob', 30],
    [3, 'Charlie', 35]
]
columns = ['ID', 'Name', 'Age']
df = pd.DataFrame(data, columns=columns)
print("DataFrame created from 2D list:")
print(df)
