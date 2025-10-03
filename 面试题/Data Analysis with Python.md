# 100 Data Analytics with Python Interview Questions and Answers

### 1. How do you read a CSV file into a DataFrame using pandas?
**Answer:**  
You can read a CSV file using the `pd.read_csv` function.
```python
import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())
```
---

### 2. How do you handle missing values in a DataFrame using pandas?
**Answer:**  
You can handle missing values using the `fillna` or `dropna` methods.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df.fillna(0, inplace=True)
# Or to drop missing values
df.dropna(inplace=True)
print(df.head())
```
---

### 3. How do you filter rows in a DataFrame based on a condition?
**Answer:**  
You can filter rows using boolean indexing.
```python
import pandas as pd

df = pd.read_csv('data.csv')
filtered_df = df[df['column'] > 10]
print(filtered_df)
```
---

### 4. How do you compute summary statistics for a DataFrame using pandas?
**Answer:**  
You can compute summary statistics using the `describe` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
summary_stats = df.describe()
print(summary_stats)
```
---

### 5. How do you group data in a DataFrame and compute aggregate statistics?
**Answer:**  
You can group data using the `groupby` method and compute aggregate statistics with `agg`.
```python
import pandas as pd

df = pd.read_csv('data.csv')
grouped_df = df.groupby('column').agg({'another_column': 'mean'})
print(grouped_df)
```
---

### 6. How do you merge two DataFrames in pandas?
**Answer:**  
You can merge DataFrames using the `merge` function.
```python
import pandas as pd

df1 = pd.read_csv('data1.csv')
df2 = pd.read_csv('data2.csv')
merged_df = pd.merge(df1, df2, on='common_column')
print(merged_df.head())
```
---

### 7. How do you concatenate multiple DataFrames in pandas?
**Answer:**  
You can concatenate DataFrames using the `pd.concat` function.
```python
import pandas as pd

df1 = pd.read_csv('data1.csv')
df2 = pd.read_csv('data2.csv')
concatenated_df = pd.concat([df1, df2], axis=0)
print(concatenated_df.head())
```
---

### 8. How do you pivot a DataFrame in pandas?
**Answer:**  
You can pivot a DataFrame using the `pivot_table` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
pivot_df = df.pivot_table(index='column1', columns='column2', values='value_column')
print(pivot_df)
```
---

### 9. How do you melt a DataFrame in pandas?
**Answer:**  
You can melt a DataFrame using the `melt` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
melted_df = df.melt(id_vars=['id'], value_vars=['column1', 'column2'])
print(melted_df)
```
---

### 10. How do you create a pivot table in pandas?
**Answer:**  
You can create a pivot table using the `pivot_table` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
pivot_table = df.pivot_table(index='column1', columns='column2', values='value_column', aggfunc='mean')
print(pivot_table)
```
---

### 11. How do you apply a function to a DataFrame column using pandas?
**Answer:**  
You can apply a function using the `apply` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df['new_column'] = df['column'].apply(lambda x: x * 2)
print(df.head())
```
---

### 12. How do you apply a function to a DataFrame row using pandas?
**Answer:**  
You can apply a function using the `apply` method with `axis=1`.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df['new_column'] = df.apply(lambda row: row['column1'] + row['column2'], axis=1)
print(df.head())
```
---

### 13. How do you apply a function to a group in a DataFrame using pandas?
**Answer:**  
You can apply a function to a group using the `groupby` and `apply` methods.
```python
import pandas as pd

df = pd.read_csv('data.csv')
grouped_df = df.groupby('column').apply(lambda x: x.mean())
print(grouped_df)
```
---

### 14. How do you create a new column based on conditions in pandas?
**Answer:**  
You can create a new column using `np.where` or `pd.Series.apply`.
```python
import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')
df['new_column'] = np.where(df['column'] > 10, 'high', 'low')
print(df.head())
```
---

### 15. How do you create a scatter plot using pandas?
**Answer:**  
You can create a scatter plot using the `plot.scatter` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df.plot.scatter(x='column1', y='column2')
```
---

### 16. How do you create a line plot using pandas?
**Answer:**  
You can create a line plot using the `plot.line` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df.plot.line(x='column1', y='column2')
```
---

### 17. How do you create a histogram using pandas?
**Answer:**  
You can create a histogram using the `plot.hist` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df['column'].plot.hist()
```
---

### 18. How do you create a box plot using pandas?
**Answer:**  
You can create a box plot using the `plot.box` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df.plot.box()
```
---

### 19. How do you create a bar plot using pandas?
**Answer:**  
You can create a bar plot using the `plot.bar` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df.plot.bar(x='column1', y='column2')
```
---

### 20. How do you create a pie chart using pandas?
**Answer:**  
You can create a pie chart using the `plot.pie` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df['column'].value_counts().plot.pie()
```
---

### 21. How do you save a DataFrame to a CSV file using pandas?
**Answer:**  
You can save a DataFrame using the `to_csv` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df.to_csv('output.csv', index=False)
```
---

### 22. How do you save a DataFrame to an Excel file using pandas?
**Answer:**  
You can save a DataFrame using the `to_excel` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df.to_excel('output.xlsx', index=False)
```
---

### 23. How do you load an Excel file into a DataFrame using pandas?
**Answer:**  
You can load an Excel file using the `pd.read_excel` function.
```python
import pandas as pd

df = pd.read_excel('data.xlsx')
print(df.head())
```
---

### 24. How do you read specific columns from a CSV file using pandas?
**Answer:**  
You can read specific columns using the `usecols` parameter in `pd.read_csv`.
```python
import pandas as pd

df = pd.read_csv('data.csv', usecols=['column1', 'column2'])
print(df.head())
```
---

### 25. How do you rename columns in a DataFrame using pandas?
**Answer:**  
You can rename columns using the `rename` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df.rename(columns={'old_name': 'new_name'}, inplace=True)
print(df.head())
```
---

### 26. How do you drop columns from a DataFrame using pandas?
**Answer:**  
You can drop columns using the `drop` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df.drop(columns=['column_to_drop'], inplace=True)
print(df.head())
```
---

### 27. How do you drop duplicate rows in a DataFrame using pandas?
**Answer:**  
You can drop duplicate rows using the `drop_duplicates` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df.drop_duplicates(inplace=True)
print(df.head())
```
---

### 28. How do you sort a DataFrame by a column in ascending order using pandas?
**Answer:**  
You can sort a DataFrame using the `sort_values` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df.sort_values(by='column', ascending=True, inplace=True)
print(df.head())
```
---

### 29.

 How do you sort a DataFrame by multiple columns using pandas?
**Answer:**  
You can sort a DataFrame by multiple columns using the `sort_values` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df.sort_values(by=['column1', 'column2'], ascending=[True, False], inplace=True)
print(df.head())
```
---

### 30. How do you set a column as the index of a DataFrame using pandas?
**Answer:**  
You can set a column as the index using the `set_index` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df.set_index('column', inplace=True)
print(df.head())
```
---

### 31. How do you reset the index of a DataFrame using pandas?
**Answer:**  
You can reset the index using the `reset_index` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df.reset_index(inplace=True)
print(df.head())
```
---

### 32. How do you calculate the correlation matrix of a DataFrame using pandas?
**Answer:**  
You can calculate the correlation matrix using the `corr` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
correlation_matrix = df.corr()
print(correlation_matrix)
```
---

### 33. How do you calculate the covariance matrix of a DataFrame using pandas?
**Answer:**  
You can calculate the covariance matrix using the `cov` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
covariance_matrix = df.cov()
print(covariance_matrix)
```
---

### 34. How do you calculate the rolling mean of a DataFrame column using pandas?
**Answer:**  
You can calculate the rolling mean using the `rolling` and `mean` methods.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df['rolling_mean'] = df['column'].rolling(window=3).mean()
print(df.head())
```
---

### 35. How do you calculate the exponential moving average of a DataFrame column using pandas?
**Answer:**  
You can calculate the exponential moving average using the `ewm` and `mean` methods.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df['ema'] = df['column'].ewm(span=3, adjust=False).mean()
print(df.head())
```
---

### 36. How do you calculate the cumulative sum of a DataFrame column using pandas?
**Answer:**  
You can calculate the cumulative sum using the `cumsum` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df['cumsum'] = df['column'].cumsum()
print(df.head())
```
---

### 37. How do you calculate the cumulative product of a DataFrame column using pandas?
**Answer:**  
You can calculate the cumulative product using the `cumprod` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df['cumprod'] = df['column'].cumprod()
print(df.head())
```
---

### 38. How do you calculate the cumulative minimum of a DataFrame column using pandas?
**Answer:**  
You can calculate the cumulative minimum using the `cummin` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df['cummin'] = df['column'].cummin()
print(df.head())
```
---

### 39. How do you calculate the cumulative maximum of a DataFrame column using pandas?
**Answer:**  
You can calculate the cumulative maximum using the `cummax` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df['cummax'] = df['column'].cummax()
print(df.head())
```
---

### 40. How do you resample a time series DataFrame using pandas?
**Answer:**  
You can resample a time series using the `resample` method.
```python
import pandas as pd

df = pd.read_csv('time_series_data.csv', parse_dates=['date'], index_col='date')
resampled_df = df.resample('M').mean()
print(resampled_df.head())
```
---

### 41. How do you interpolate missing values in a DataFrame using pandas?
**Answer:**  
You can interpolate missing values using the `interpolate` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df['column'].interpolate(method='linear', inplace=True)
print(df.head())
```
---

### 42. How do you calculate the rank of a DataFrame column using pandas?
**Answer:**  
You can calculate the rank using the `rank` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df['rank'] = df['column'].rank()
print(df.head())
```
---

### 43. How do you perform a rolling window correlation between two DataFrame columns using pandas?
**Answer:**  
You can perform a rolling window correlation using the `rolling` and `corr` methods.
```python
import pandas as pd

df = pd.read_csv('data.csv')
rolling_corr = df['column1'].rolling(window=5).corr(df['column2'])
print(rolling_corr.head())
```
---

### 44. How do you shift the values of a DataFrame column using pandas?
**Answer:**  
You can shift the values using the `shift` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df['shifted_column'] = df['column'].shift(1)
print(df.head())
```
---

### 45. How do you calculate the difference between successive rows of a DataFrame column using pandas?
**Answer:**  
You can calculate the difference using the `diff` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df['diff'] = df['column'].diff()
print(df.head())
```
---

### 46. How do you calculate the percentage change between successive rows of a DataFrame column using pandas?
**Answer:**  
You can calculate the percentage change using the `pct_change` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df['pct_change'] = df['column'].pct_change()
print(df.head())
```
---

### 47. How do you apply a lambda function to each row of a DataFrame using pandas?
**Answer:**  
You can apply a lambda function to each row using the `apply` method with `axis=1`.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df['new_column'] = df.apply(lambda row: row['column1'] + row['column2'], axis=1)
print(df.head())
```
---

### 48. How do you apply a lambda function to each element of a DataFrame column using pandas?
**Answer:**  
You can apply a lambda function to each element using the `apply` method.
```python
import pandas as pd

df = pd.read_csv('data.csv')
df['new_column'] = df['column'].apply(lambda x: x * 2)
print(df.head())
```
---

### 49. How do you filter a DataFrame based on a string condition in a column using pandas?
**Answer:**  
You can filter based on a string condition using boolean indexing.
```python
import pandas as pd

df = pd.read_csv('data.csv')
filtered_df = df[df['column'].str.contains('pattern')]
print(filtered_df.head())
```
---

### 50. How do you create dummy variables from a categorical column in a DataFrame using pandas?
**Answer:**  
You can create dummy variables using the `pd.get_dummies` function.
```python
import pandas as pd

df = pd.read_csv('data.csv')
dummies = pd.get_dummies(df['categorical_column'])
print(dummies.head())
```
---

### 51. How do you merge DataFrames with different keys using pandas?
**Answer:**  
You can merge DataFrames with different keys using the `pd.merge` function and specifying the `left_on` and `right_on` parameters.
```python
import pandas as pd

df1 = pd.DataFrame({'key1': [1, 2, 3], 'value1': ['a', 'b', 'c']})
df2 = pd.DataFrame({'key2': [1, 2, 3], 'value2': ['x', 'y', 'z']})
merged_df = pd.merge(df1, df2, left_on='key1', right_on='key2')
print(merged_df)
```
---

### 52. How do you apply a function to multiple columns of a DataFrame using pandas?
**Answer:**  
You can apply a function to multiple columns using the `apply` method with `axis=1`.
```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df['C'] = df.apply(lambda row: row['A'] + row['B'], axis=1)
print(df)
```
---

### 53. How do you compute the moving average of a DataFrame column using pandas?
**Answer:**  
You can compute the moving average using the `rolling` and `mean` methods.
```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
df['moving_avg'] = df['A'].rolling(window=3).mean()
print(df)
```
---

### 54. How do you merge multiple DataFrames on a common key using pandas?
**Answer:**  
You can merge multiple

 DataFrames using the `pd.merge` function in a loop or reduce.
```python
import pandas as pd
from functools import reduce

dfs = [pd.DataFrame({'key': [1, 2, 3], 'value': ['a', 'b', 'c']}), 
       pd.DataFrame({'key': [1, 2, 3], 'value': ['x', 'y', 'z']}), 
       pd.DataFrame({'key': [1, 2, 3], 'value': ['u', 'v', 'w']})]
merged_df = reduce(lambda left, right: pd.merge(left, right, on='key'), dfs)
print(merged_df)
```
---

### 55. How do you remove outliers from a DataFrame using pandas?
**Answer:**  
You can remove outliers by filtering based on a condition.
```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 100]})
q1 = df['A'].quantile(0.25)
q3 = df['A'].quantile(0.75)
iqr = q3 - q1
filtered_df = df[(df['A'] >= (q1 - 1.5 * iqr)) & (df['A'] <= (q3 + 1.5 * iqr))]
print(filtered_df)
```
---

### 56. How do you reshape a DataFrame from long to wide format using pandas?
**Answer:**  
You can reshape using the `pivot` method.
```python
import pandas as pd

df = pd.DataFrame({'date': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
                   'variable': ['A', 'B', 'A', 'B'], 'value': [1, 2, 3, 4]})
wide_df = df.pivot(index='date', columns='variable', values='value')
print(wide_df)
```
---

### 57. How do you stack a DataFrame from wide to long format using pandas?
**Answer:**  
You can stack using the `melt` method.
```python
import pandas as pd

df = pd.DataFrame({'date': ['2021-01-01', '2021-01-02'],
                   'A': [1, 3], 'B': [2, 4]})
long_df = df.melt(id_vars='date', value_vars=['A', 'B'])
print(long_df)
```
---

### 58. How do you impute missing values with the mean of a column using pandas?
**Answer:**  
You can impute missing values using the `fillna` method.
```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, None, 4, 5]})
df['A'].fillna(df['A'].mean(), inplace=True)
print(df)
```
---

### 59. How do you group by multiple columns and apply a function using pandas?
**Answer:**  
You can group by multiple columns using the `groupby` method and apply a function with `apply`.
```python
import pandas as pd

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar'], 'B': ['one', 'one', 'two', 'two'], 'C': [1, 2, 3, 4]})
grouped_df = df.groupby(['A', 'B']).apply(lambda x: x.sum())
print(grouped_df)
```
---

### 60. How do you concatenate DataFrames with different indices using pandas?
**Answer:**  
You can concatenate DataFrames with different indices using the `pd.concat` function.
```python
import pandas as pd

df1 = pd.DataFrame({'A': [1, 2, 3]}, index=[0, 1, 2])
df2 = pd.DataFrame({'B': [4, 5, 6]}, index=[2, 3, 4])
concatenated_df = pd.concat([df1, df2], axis=1)
print(concatenated_df)
```
---

### 61. How do you convert a column to datetime in pandas?
**Answer:**  
You can convert a column to datetime using the `pd.to_datetime` function.
```python
import pandas as pd

df = pd.DataFrame({'date': ['2021-01-01', '2021-01-02']})
df['date'] = pd.to_datetime(df['date'])
print(df)
```
---

### 62. How do you extract the year from a datetime column in pandas?
**Answer:**  
You can extract the year using the `.dt` accessor.
```python
import pandas as pd

df = pd.DataFrame({'date': pd.to_datetime(['2021-01-01', '2021-01-02'])})
df['year'] = df['date'].dt.year
print(df)
```
---

### 63. How do you extract the month from a datetime column in pandas?
**Answer:**  
You can extract the month using the `.dt` accessor.
```python
import pandas as pd

df = pd.DataFrame({'date': pd.to_datetime(['2021-01-01', '2021-02-01'])})
df['month'] = df['date'].dt.month
print(df)
```
---

### 64. How do you extract the day from a datetime column in pandas?
**Answer:**  
You can extract the day using the `.dt` accessor.
```python
import pandas as pd

df = pd.DataFrame({'date': pd.to_datetime(['2021-01-01', '2021-01-02'])})
df['day'] = df['date'].dt.day
print(df)
```
---

### 65. How do you calculate the time difference between two datetime columns in pandas?
**Answer:**  
You can calculate the time difference using subtraction.
```python
import pandas as pd

df = pd.DataFrame({'start': pd.to_datetime(['2021-01-01', '2021-01-02']), 'end': pd.to_datetime(['2021-01-02', '2021-01-03'])})
df['diff'] = df['end'] - df['start']
print(df)
```
---

### 66. How do you round a datetime column to the nearest hour in pandas?
**Answer:**  
You can round a datetime column using the `round` method.
```python
import pandas as pd

df = pd.DataFrame({'date': pd.to_datetime(['2021-01-01 12:30:00', '2021-01-01 12:45:00'])})
df['rounded_date'] = df['date'].dt.round('H')
print(df)
```
---

### 67. How do you round a datetime column to the nearest day in pandas?
**Answer:**  
You can round a datetime column using the `round` method.
```python
import pandas as pd

df = pd.DataFrame({'date': pd.to_datetime(['2021-01-01 12:30:00', '2021-01-01 23:45:00'])})
df['rounded_date'] = df['date'].dt.round('D')
print(df)
```
---

### 68. How do you round a datetime column to the nearest minute in pandas?
**Answer:**  
You can round a datetime column using the `round` method.
```python
import pandas as pd

df = pd.DataFrame({'date': pd.to_datetime(['2021-01-01 12:30:30', '2021-01-01 12:45:45'])})
df['rounded_date'] = df['date'].dt.round('min')
print(df)
```
---

### 69. How do you set a datetime column as the index of a DataFrame in pandas?
**Answer:**  
You can set a datetime column as the index using the `set_index` method.
```python
import pandas as pd

df = pd.DataFrame({'date': pd.to_datetime(['2021-01-01', '2021-01-02']), 'value': [1, 2]})
df.set_index('date', inplace=True)
print(df)
```
---

### 70. How do you create a time series plot using pandas?
**Answer:**  
You can create a time series plot using the `plot` method.
```python
import pandas as pd

df = pd.DataFrame({'date': pd.to_datetime(['2021-01-01', '2021-01-02']), 'value': [1, 2]})
df.set_index('date', inplace=True)
df.plot()
```
---

### 71. How do you calculate the year-to-date (YTD) sum of a DataFrame column using pandas?
**Answer:**  
You can calculate the YTD sum using the `cumsum` method.
```python
import pandas as pd

df = pd.DataFrame({'date': pd.to_datetime(['2021-01-01', '2021-01-02', '2021-01-03']), 'value': [1, 2, 3]})
df['ytd_sum'] = df['value'].cumsum()
print(df)
```
---

### 72. How do you calculate the month-to-date (MTD) sum of a DataFrame column using pandas?
**Answer:**  
You can calculate the MTD sum using the `groupby` and `cumsum` methods.
```python
import pandas as pd

df = pd.DataFrame({'date': pd.to_datetime(['2021-01-01', '2021-01-02', '202

1-02-01', '2021-02-02']), 'value': [1, 2, 3, 4]})
df['month'] = df['date'].dt.to_period('M')
df['mtd_sum'] = df.groupby('month')['value'].cumsum()
print(df)
```
---

### 73. How do you calculate the week-to-date (WTD) sum of a DataFrame column using pandas?
**Answer:**  
You can calculate the WTD sum using the `groupby` and `cumsum` methods.
```python
import pandas as pd

df = pd.DataFrame({'date': pd.to_datetime(['2021-01-01', '2021-01-02', '2021-01-04', '2021-01-05']), 'value': [1, 2, 3, 4]})
df['week'] = df['date'].dt.to_period('W')
df['wtd_sum'] = df.groupby('week')['value'].cumsum()
print(df)
```
---

### 74. How do you calculate the quarter-to-date (QTD) sum of a DataFrame column using pandas?
**Answer:**  
You can calculate the QTD sum using the `groupby` and `cumsum` methods.
```python
import pandas as pd

df = pd.DataFrame({'date': pd.to_datetime(['2021-01-01', '2021-01-02', '2021-04-01', '2021-04-02']), 'value': [1, 2, 3, 4]})
df['quarter'] = df['date'].dt.to_period('Q')
df['qtd_sum'] = df.groupby('quarter')['value'].cumsum()
print(df)
```
---

### 75. How do you calculate the rolling sum of a DataFrame column using pandas?
**Answer:**  
You can calculate the rolling sum using the `rolling` and `sum` methods.
```python
import pandas as pd

df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
df['rolling_sum'] = df['value'].rolling(window=3).sum()
print(df)
```
---

### 76. How do you calculate the rolling average of a DataFrame column using pandas?
**Answer:**  
You can calculate the rolling average using the `rolling` and `mean` methods.
```python
import pandas as pd

df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
df['rolling_avg'] = df['value'].rolling(window=3).mean()
print(df)
```
---

### 77. How do you calculate the rolling standard deviation of a DataFrame column using pandas?
**Answer:**  
You can calculate the rolling standard deviation using the `rolling` and `std` methods.
```python
import pandas as pd

df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
df['rolling_std'] = df['value'].rolling(window=3).std()
print(df)
```
---

### 78. How do you calculate the exponentially weighted mean of a DataFrame column using pandas?
**Answer:**  
You can calculate the exponentially weighted mean using the `ewm` and `mean` methods.
```python
import pandas as pd

df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
df['ewm_mean'] = df['value'].ewm(span=3, adjust=False).mean()
print(df)
```
---

### 79. How do you calculate the exponentially weighted standard deviation of a DataFrame column using pandas?
**Answer:**  
You can calculate the exponentially weighted standard deviation using the `ewm` and `std` methods.
```python
import pandas as pd

df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
df['ewm_std'] = df['value'].ewm(span=3, adjust=False).std()
print(df)
```
---

### 80. How do you calculate the lagged difference of a DataFrame column using pandas?
**Answer:**  
You can calculate the lagged difference using the `shift` and `diff` methods.
```python
import pandas as pd

df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
df['lagged_diff'] = df['value'].shift(1).diff()
print(df)
```
---

### 81. How do you calculate the autocorrelation of a DataFrame column using pandas?
**Answer:**  
You can calculate the autocorrelation using the `autocorr` method.
```python
import pandas as pd

df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
autocorrelation = df['value'].autocorr()
print(autocorrelation)
```
---

### 82. How do you create a time-lagged feature in a DataFrame using pandas?
**Answer:**  
You can create a time-lagged feature using the `shift` method.
```python
import pandas as pd

df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
df['lagged_value'] = df['value'].shift(1)
print(df)
```
---

### 83. How do you calculate the rank of values within each group of a DataFrame column using pandas?
**Answer:**  
You can calculate the rank within each group using the `groupby` and `rank` methods.
```python
import pandas as pd

df = pd.DataFrame({'group': ['A', 'A', 'B', 'B'], 'value': [1, 2, 3, 4]})
df['rank_within_group'] = df.groupby('group')['value'].rank()
print(df)
```
---

### 84. How do you calculate the z-score of a DataFrame column using pandas?
**Answer:**  
You can calculate the z-score using the `mean` and `std` methods.
```python
import pandas as pd

df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
df['z_score'] = (df['value'] - df['value'].mean()) / df['value'].std()
print(df)
```
---

### 85. How do you calculate the rolling z-score of a DataFrame column using pandas?
**Answer:**  
You can calculate the rolling z-score using the `rolling`, `mean`, and `std` methods.
```python
import pandas as pd

df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
rolling_mean = df['value'].rolling(window=3).mean()
rolling_std = df['value'].rolling(window=3).std()
df['rolling_z_score'] = (df['value'] - rolling_mean) / rolling_std
print(df)
```
---

### 86. How do you create a lagged feature for multiple time steps in a DataFrame using pandas?
**Answer:**  
You can create multiple lagged features using the `shift` method in a loop.
```python
import pandas as pd

df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
for lag in range(1, 4):
    df[f'lag_{lag}'] = df['value'].shift(lag)
print(df)
```
---

### 87. How do you calculate the cumulative sum of values within each group of a DataFrame column using pandas?
**Answer:**  
You can calculate the cumulative sum within each group using the `groupby` and `cumsum` methods.
```python
import pandas as pd

df = pd.DataFrame({'group': ['A', 'A', 'B', 'B'], 'value': [1, 2, 3, 4]})
df['cumsum_within_group'] = df.groupby('group')['value'].cumsum()
print(df)
```
---

### 88. How do you normalize a DataFrame column to a 0-1 range using pandas?
**Answer:**  
You can normalize a column using the min-max normalization formula.
```python
import pandas as pd

df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
df['normalized'] = (df['value'] - df['value'].min()) / (df['value'].max() - df['value'].min())
print(df)
```
---

### 89. How do you standardize a DataFrame column to have a mean of 0 and a standard deviation of 1 using pandas?
**Answer:**  
You can standardize a column using the z-score formula.
```python
import pandas as pd

df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
df['standardized'] = (df['value'] - df['value'].mean()) / df['value'].std()
print(df)
```
---

### 90. How do you apply a custom function to a rolling window in a DataFrame using pandas?
**Answer:**  
You can apply a custom function using the `rolling` and `apply` methods.
```python
import pandas as pd

df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
df['custom_rolling'] = df['value'].rolling(window=3).apply(lambda x: x.max() - x.min())
print(df)
```
---

### 91. How do you calculate the exponentially weighted variance

 of a DataFrame column using pandas?
**Answer:**  
You can calculate the exponentially weighted variance using the `ewm` and `var` methods.
```python
import pandas as pd

df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
df['ewm_var'] = df['value'].ewm(span=3, adjust=False).var()
print(df)
```
---

### 92. How do you calculate the rolling correlation between two DataFrame columns using pandas?
**Answer:**  
You can calculate the rolling correlation using the `rolling` and `corr` methods.
```python
import pandas as pd

df = pd.DataFrame({'value1': [1, 2, 3, 4, 5], 'value2': [5, 4, 3, 2, 1]})
df['rolling_corr'] = df['value1'].rolling(window=3).corr(df['value2'])
print(df)
```
---

### 93. How do you calculate the cumulative product within each group of a DataFrame column using pandas?
**Answer:**  
You can calculate the cumulative product within each group using the `groupby` and `cumprod` methods.
```python
import pandas as pd

df = pd.DataFrame({'group': ['A', 'A', 'B', 'B'], 'value': [1, 2, 3, 4]})
df['cumprod_within_group'] = df.groupby('group')['value'].cumprod()
print(df)
```
---

### 94. How do you create a pivot table with multiple aggregation functions using pandas?
**Answer:**  
You can create a pivot table with multiple aggregation functions using the `pivot_table` method.
```python
import pandas as pd

df = pd.DataFrame({'date': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'], 'variable': ['A', 'B', 'A', 'B'], 'value': [1, 2, 3, 4]})
pivot_table = df.pivot_table(index='date', columns='variable', values='value', aggfunc=['mean', 'sum'])
print(pivot_table)
```
---

### 95. How do you calculate the expanding mean of a DataFrame column using pandas?
**Answer:**  
You can calculate the expanding mean using the `expanding` and `mean` methods.
```python
import pandas as pd

df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
df['expanding_mean'] = df['value'].expanding().mean()
print(df)
```
---

### 96. How do you calculate the expanding sum of a DataFrame column using pandas?
**Answer:**  
You can calculate the expanding sum using the `expanding` and `sum` methods.
```python
import pandas as pd

df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
df['expanding_sum'] = df['value'].expanding().sum()
print(df)
```
---

### 97. How do you calculate the expanding standard deviation of a DataFrame column using pandas?
**Answer:**  
You can calculate the expanding standard deviation using the `expanding` and `std` methods.
```python
import pandas as pd

df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
df['expanding_std'] = df['value'].expanding().std()
print(df)
```
---

### 98. How do you create a pivot table with multiple index levels using pandas?
**Answer:**  
You can create a pivot table with multiple index levels using the `pivot_table` method.
```python
import pandas as pd

df = pd.DataFrame({'date': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'], 'variable': ['A', 'B', 'A', 'B'], 'value': [1, 2, 3, 4]})
pivot_table = df.pivot_table(index=['date', 'variable'], values='value', aggfunc='mean')
print(pivot_table)
```
---

### 99. How do you create a pivot table with multiple value columns using pandas?
**Answer:**  
You can create a pivot table with multiple value columns using the `pivot_table` method.
```python
import pandas as pd

df = pd.DataFrame({'date': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'], 'variable': ['A', 'B', 'A', 'B'], 'value1': [1, 2, 3, 4], 'value2': [5, 6, 7, 8]})
pivot_table = df.pivot_table(index='date', columns='variable', values=['value1', 'value2'], aggfunc='mean')
print(pivot_table)
```
---

### 100. How do you create a pivot table with multiple aggregation functions for multiple value columns using pandas?
**Answer:**  
You can create a pivot table with multiple aggregation functions for multiple value columns using the `pivot_table` method.
```python
import pandas as pd

df = pd.DataFrame({'date': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'], 'variable': ['A', 'B', 'A', 'B'], 'value1': [1, 2, 3, 4], 'value2': [5, 6, 7, 8]})
pivot_table = df.pivot_table(index='date', columns='variable', values=['value1', 'value2'], aggfunc={'value1': 'mean', 'value2': 'sum'})
print(pivot_table)
```

If you found this repository helpful, please give it a star!

Follow me on:
- [LinkedIn](https://www.linkedin.com/in/ashish-jangra/)
- [GitHub](https://github.com/AshishJangra27)
- [Kaggle](https://www.kaggle.com/ashishjangra27)

Stay updated with my latest content and projects!
```
