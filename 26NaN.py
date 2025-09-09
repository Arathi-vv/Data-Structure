import pandas as pd
import numpy as np
# Sample DataFrame with NaN values
data = {
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 2, 3, 4],
    'C': [1, np.nan, np.nan, 4]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Fill NaN values with 0
df_filled = df.fillna(0)
print("\nDataFrame after filling NaN with 0:")
print(df_filled)
