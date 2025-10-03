# 50 Pandas Interview Questions and Answers

Below are 50 practical Pandas questions and answers focusing on common operations, data manipulation, and analysis techniques using Pandas DataFrames and Series in Python.

Each question includes:
- A scenario or requirement
- A code snippet demonstrating one possible solution

**Note:** For all examples, assume you have already imported Pandas as follows:
```python
import pandas as pd
```

---

### 1. How do you create a Pandas DataFrame from a dictionary?
**Answer:**  
Use `pd.DataFrame()` with a dictionary of lists or values.
```python
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
print(df)
```

---

### 2. How do you read a CSV file into a DataFrame?
**Answer:**  
Use `pd.read_csv()` with the file path.
```python
df = pd.read_csv('data.csv')
print(df.head())
```

---

### 3. How do you write a DataFrame to a CSV file?
**Answer:**  
Use `df.to_csv()` with a file path.
```python
df.to_csv('output.csv', index=False)
```

---

### 4. How do you get the first 5 rows of a DataFrame?
**Answer:**  
Use `df.head()`.
```python
print(df.head())
```

---

### 5. How do you get the shape (rows, columns) of a DataFrame?
**Answer:**  
Use `df.shape`.
```python
print(df.shape)
```

---

### 6. How do you select a single column from a DataFrame?
**Answer:**  
Use `df['column_name']`.
```python
ages = df['Age']
print(ages)
```

---

### 7. How do you select multiple columns from a DataFrame?
**Answer:**  
Use a list of column names.
```python
subset = df[['Name', 'Age']]
print(subset)
```

---

### 8. How do you select rows by index range?
**Answer:**  
Use slicing with `df.iloc`.
```python
rows = df.iloc[0:3]  # first 3 rows
print(rows)
```

---

### 9. How do you select rows based on a condition?
**Answer:**  
Use boolean indexing.
```python
adults = df[df['Age'] > 18]
print(adults)
```

---

### 10. How do you filter rows based on multiple conditions?
**Answer:**  
Use `&` or `|` operators with parentheses.
```python
older_males = df[(df['Age'] > 25) & (df['Gender'] == 'Male')]
print(older_males)
```

---

### 11. How do you reset the index of a DataFrame?
**Answer:**  
Use `df.reset_index()`.
```python
df_reset = df.reset_index(drop=True)
print(df_reset)
```

---

### 12. How do you sort a DataFrame by a column?
**Answer:**  
Use `df.sort_values()`.
```python
df_sorted = df.sort_values('Age')
print(df_sorted)
```

---

### 13. How do you sort by multiple columns?
**Answer:**  
Pass a list of column names to `sort_values()`.
```python
df_sorted = df.sort_values(['Gender', 'Age'], ascending=[True, False])
print(df_sorted)
```

---

### 14. How do you drop a column from a DataFrame?
**Answer:**  
Use `df.drop()` with `axis=1`.
```python
df_dropped = df.drop('Age', axis=1)
print(df_dropped)
```

---

### 15. How do you drop rows with missing values?
**Answer:**  
Use `df.dropna()`.
```python
df_clean = df.dropna()
print(df_clean)
```

---

### 16. How do you fill missing values with a constant?
**Answer:**  
Use `df.fillna(value)`.
```python
df_filled = df.fillna(0)
print(df_filled)
```

---

### 17. How do you fill missing values with the mean of a column?
**Answer:**  
Calculate mean and then use `fillna()`.
```python
mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)
print(df)
```

---

### 18. How do you group a DataFrame by a column and compute an aggregation?
**Answer:**  
Use `df.groupby('column').agg('function')`.
```python
avg_age = df.groupby('Gender')['Age'].mean()
print(avg_age)
```

---

### 19. How do you get the unique values of a column?
**Answer:**  
Use `df['column'].unique()`.
```python
unique_names = df['Name'].unique()
print(unique_names)
```

---

### 20. How do you count the number of unique values in a column?
**Answer:**  
Use `df['column'].nunique()`.
```python
count_unique = df['Name'].nunique()
print(count_unique)
```

---

### 21. How do you rename a column in a DataFrame?
**Answer:**  
Use `df.rename(columns={'old':'new'})`.
```python
df = df.rename(columns={'Name': 'FullName'})
print(df.head())
```

---

### 22. How do you apply a function to every element of a column?
**Answer:**  
Use `df['column'].apply(function)`.
```python
df['AgePlusOne'] = df['Age'].apply(lambda x: x + 1)
print(df.head())
```

---

### 23. How do you create a new column based on a condition?
**Answer:**  
Use `np.where` or apply a function.
```python
import numpy as np
df['Adult'] = np.where(df['Age'] >= 18, 'Yes', 'No')
print(df.head())
```

---

### 24. How do you combine two DataFrames vertically (append rows)?
**Answer:**  
Use `pd.concat([df1, df2])`.
```python
df_combined = pd.concat([df1, df2], ignore_index=True)
print(df_combined)
```

---

### 25. How do you merge two DataFrames on a common column?
**Answer:**  
Use `pd.merge(df1, df2, on='column')`.
```python
merged = pd.merge(df1, df2, on='ID')
print(merged.head())
```

---

### 26. How do you get the summary statistics of a DataFrame?
**Answer:**  
Use `df.describe()`.
```python
stats = df.describe()
print(stats)
```

---

### 27. How do you check the data types of each column?
**Answer:**  
Use `df.dtypes`.
```python
print(df.dtypes)
```

---

### 28. How do you change the data type of a column?
**Answer:**  
Use `df['column'].astype(dtype)`.
```python
df['Age'] = df['Age'].astype(int)
```

---

### 29. How do you set a column as the index of the DataFrame?
**Answer:**  
Use `df.set_index('column')`.
```python
df_indexed = df.set_index('ID')
print(df_indexed.head())
```

---

### 30. How do you reset the index and drop the old index?
**Answer:**  
Use `df.reset_index(drop=True)`.
```python
df_reset = df.reset_index(drop=True)
```

---

### 31. How do you count the number of missing values in each column?
**Answer:**  
Use `df.isna().sum()`.
```python
missing_counts = df.isna().sum()
print(missing_counts)
```

---

### 32. How do you select rows by label using `.loc`?
**Answer:**  
Use `df.loc[label]` for index labels.
```python
row_data = df.loc[0]  # if 0 is an index label
print(row_data)
```

---

### 33. How do you select rows by integer position using `.iloc`?
**Answer:**  
Use `df.iloc[index_position]`.
```python
row_data = df.iloc[0]
print(row_data)
```

---

### 34. How do you remove duplicate rows?
**Answer:**  
Use `df.drop_duplicates()`.
```python
df_unique = df.drop_duplicates()
```

---

### 35. How do you find correlation between columns?
**Answer:**  
Use `df.corr()`.
```python
correlation = df.corr()
print(correlation)
```

---

### 36. How do you create a pivot table?
**Answer:**  
Use `pd.pivot_table()`.
```python
pivot = pd.pivot_table(df, values='Sales', index='Region', columns='Product', aggfunc='sum')
print(pivot)
```

---

### 37. How do you replace values in a column based on a condition?
**Answer:**  
Use `df.loc[condition, 'column'] = new_value`.
```python
df.loc[df['Age'] < 0, 'Age'] = 0
```

---

### 38. How do you extract a substring from a column of strings?
**Answer:**  
Use `str` accessor.
```python
df['Initial'] = df['Name'].str[0]
print(df.head())
```

---

### 39. How do you convert a column to datetime?
**Answer:**  
Use `pd.to_datetime()`.
```python
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
```

---

### 40. How do you filter rows based on a substring in a column?
**Answer:**  
Use `df['column'].str.contains('pattern')`.
```python
filtered = df[df['Name'].str.contains('A')]
print(filtered)
```

---

### 41. How do you change column names to lowercase?
**Answer:**  
Use a list comprehension on `df.columns`.
```python
df.columns = [col.lower() for col in df.columns]
```

---

### 42. How do you find the index of the maximum value in a column?
**Answer:**  
Use `df['column'].idxmax()`.
```python
max_index = df['Age'].idxmax()
print(max_index)
```

---

### 43. How do you sample random rows from a DataFrame?
**Answer:**  
Use `df.sample(n=number)`.
```python
sampled = df.sample(n=5)
print(sampled)
```

---

### 44. How do you apply a custom function to a DataFrame row-wise?
**Answer:**  
Use `df.apply(function, axis=1)`.
```python
def sum_age(row):
    return row['Age'] + 10

df['Age_plus_10'] = df.apply(sum_age, axis=1)
```

---

### 45. How do you create dummy variables for categorical columns?
**Answer:**  
Use `pd.get_dummies()`.
```python
df_dummies = pd.get_dummies(df, columns=['Gender'])
print(df_dummies.head())
```

---

### 46. How do you combine text columns into one column?
**Answer:**  
Use string concatenation.
```python
df['FullInfo'] = df['Name'] + ' - ' + df['City']
```

---

### 47. How do you find rows with any missing values?
**Answer:**  
Use `df[df.isna().any(axis=1)]`.
```python
missing_rows = df[df.isna().any(axis=1)]
print(missing_rows)
```

---

### 48. How do you find rows where all values are missing?
**Answer:**  
Use `df[df.isna().all(axis=1)]`.
```python
all_missing = df[df.isna().all(axis=1)]
print(all_missing)
```

---

### 49. How do you remove rows based on a condition?
**Answer:**  
Filter out the condition.
```python
df_filtered = df[df['Age'] >= 18]
print(df_filtered)
```

---

### 50. How do you assign values to a column conditionally using `.loc`?
**Answer:**  
Use `df.loc[condition, 'column'] = value`.
```python
df.loc[df['Age'] > 30, 'Category'] = 'Senior'
print(df.head())
```

---


If you found this repository helpful, please give it a star!

Follow me on:
- [LinkedIn](https://www.linkedin.com/in/ashish-jangra/)
- [GitHub](https://github.com/AshishJangra27)
- [Kaggle](https://www.kaggle.com/ashishjangra27)

Stay updated with my latest content and projects!
