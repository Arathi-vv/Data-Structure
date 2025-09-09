import pandas as pd
from io import StringIO
csv_data = """name,mark
a,1
b,2
c,3
"""
df = pd.read_csv(StringIO(csv_data))
print("DataFrame loaded from CSV string:")
print(df)
