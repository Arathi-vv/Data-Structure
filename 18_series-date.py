import pandas as pd
start_date = '2021-05-01'
end_date = '2021-05-12'
date_series = pd.date_range(start=start_date, end=end_date)
date_series = pd.Series(date_series)
print("Date Series from 1st May 2021 to 12th May 2021:")
print(date_series)
