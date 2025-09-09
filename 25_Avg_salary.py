import pandas as pd
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'occupation': ['Engineer', 'Doctor', 'Engineer', 'Doctor', 'Artist'],
    'salary': [70000, 120000, 75000, 115000, 50000]
}
df = pd.DataFrame(data)
avg= df.groupby('occupation')['salary'].mean()
print(avg)
