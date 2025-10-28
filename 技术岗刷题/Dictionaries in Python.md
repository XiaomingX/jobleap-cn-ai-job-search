# 50 Python Dictionaries Interview Questions and Answers
### 1. How do you merge two dictionaries in Python?
**Answer:**  
You can merge two dictionaries using the `update()` method or the `{**dict1, **dict2}` syntax.
```python
def merge_dicts(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}
```
---
### 2. How do you invert a dictionary in Python?
**Answer:**  
You can invert a dictionary by swapping keys and values using a dictionary comprehension.
```python
def invert_dict(d):
    return {v: k for k, v in d.items()}
d = {'a': 1, 'b': 2, 'c': 3}
inverted_d = invert_dict(d)
print(inverted_d)  # Output: {1: 'a', 2: 'b', 3: 'c'}
```
---
### 3. How do you remove a key from a dictionary in Python?
**Answer:**  
You can remove a key from a dictionary using the `pop()` method.
```python
def remove_key(d, key):
    d.pop(key, None)
    return d
d = {'a': 1, 'b': 2, 'c': 3}
d = remove_key(d, 'b')
print(d)  # Output: {'a': 1, 'c': 3}
```
---
### 4. How do you create a dictionary from two lists in Python?
**Answer:**  
You can create a dictionary from two lists using the `zip()` function.
```python
def lists_to_dict(keys, values):
    return dict(zip(keys, values))
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = lists_to_dict(keys, values)
print(d)  # Output: {'a': 1, 'b': 2, 'c': 3}
```
---
### 5. How do you count the frequency of elements in a list using a dictionary in Python?
**Answer:**  
You can count the frequency of elements using a dictionary to keep track of counts.
```python
def count_frequency(lst):
    freq_dict = {}
    for item in lst:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict
lst = ['a', 'b', 'a', 'c', 'b', 'a']
frequency = count_frequency(lst)
print(frequency)  # Output: {'a': 3, 'b': 2, 'c': 1}
```
---
### 6. How do you sort a dictionary by its keys in Python?
**Answer:**  
You can sort a dictionary by its keys using the `sorted()` function.
```python
def sort_dict_by_keys(d):
    return dict(sorted(d.items()))
d = {'b': 2, 'a': 1, 'c': 3}
sorted_d = sort_dict_by_keys(d)
print(sorted_d)  # Output: {'a': 1, 'b': 2, 'c': 3}
```
---
### 7. How do you sort a dictionary by its values in Python?
**Answer:**  
You can sort a dictionary by its values using the `sorted()` function with a key argument.
```python
def sort_dict_by_values(d):
    return dict(sorted(d.items(), key=lambda item: item.value()))
d = {'a': 3, 'b': 1, 'c': 2}
sorted_d = sort_dict_by_values(d)
print(sorted_d)  # Output: {'b': 1, 'c': 2, 'a': 3}
```
---
### 8. How do you check if a key exists in a dictionary in Python?
**Answer:**  
You can check if a key exists in a dictionary using the `in` keyword.
```python
def key_exists(d, key):
    return key in d
d = {'a': 1, 'b': 2, 'c': 3}
print(key_exists(d, 'b'))  # Output: True
print(key_exists(d, 'd'))  # Output: False
```
---
### 9. How do you get a value from a dictionary with a default value if the key does not exist in Python?
**Answer:**  
You can get a value with a default using the `get()` method.
```python
def get_value_with_default(d, key, default):
    return d.get(key, default)
d = {'a': 1, 'b': 2, 'c': 3}
value = get_value_with_default(d, 'd', 0)
print(value)  # Output: 0
```
---
### 10. How do you find the maximum value in a dictionary in Python?
**Answer:**  
You can find the maximum value using the `max()` function.
```python
def max_value_in_dict(d):
    return max(d.values())
d = {'a': 1, 'b': 3, 'c': 2}
max_value = max_value_in_dict(d)
print(max_value)  # Output: 3
```
---
### 11. How do you find the key of the maximum value in a dictionary in Python?
**Answer:**  
You can find the key of the maximum value using the `max()` function with a key argument.
```python
def key_of_max_value(d):
    return max(d, key=d.get)
d = {'a': 1, 'b': 3, 'c': 2}
key = key_of_max_value(d)
print(key)  # Output: 'b'
```
---
### 12. How do you update multiple keys in a dictionary in Python?
**Answer:**  
You can update multiple keys using the `update()` method.
```python
def update_keys(d, updates):
    d.update(updates)
    return d
d = {'a': 1, 'b': 2, 'c': 3}
updates = {'b': 4, 'c': 5, 'd': 6}
updated_d = update_keys(d, updates)
print(updated_d)  # Output: {'a': 1, 'b': 4, 'c': 5, 'd': 6}
```
---
### 13. How do you remove keys with empty values from a dictionary in Python?
**Answer:**  
You can remove keys with empty values using a dictionary comprehension.
```python
def remove_empty_values(d):
    return {k: v for k, v in d.items() if v}
d = {'a': 1, 'b': '', 'c': 3, 'd': None}
cleaned_d = remove_empty_values(d)
print(cleaned_d)  # Output: {'a': 1, 'c': 3}
```
---
### 14. How do you create a dictionary with default values in Python?
**Answer:**  
You can create a dictionary with default values using the `fromkeys()` method.
```python
def create_dict_with_defaults(keys, default):
    return dict.fromkeys(keys, default)
keys = ['a', 'b', 'c']
default_value = 0
d = create_dict_with_defaults(keys, default_value)
print(d)  # Output: {'a': 0, 'b': 0, 'c': 0}
```
---
### 15. How do you group elements of a list based on a dictionary key in Python?
**Answer:**  
You can group elements using `defaultdict` from the `collections` module.
```python
from collections import defaultdict
def group_elements_by_key(lst, key_func):
    grouped = defaultdict(list)
    for item in lst:
        key = key_func(item)
        grouped[key].append(item)
    return grouped
lst = ['apple', 'banana', 'cherry', 'avocado']
grouped = group_elements_by_key(lst, lambda x: x[0])
print(grouped)  # Output: {'a': ['apple', 'avocado'], 'b': ['banana'], 'c': ['cherry']}
```
---
### 16. How do you increment values in a dictionary in Python?
**Answer:**  
You can increment values using the `defaultdict` from the `collections` module.
```python
from collections import defaultdict
def increment_dict_values(lst):
    counter = defaultdict(int)
    for item in lst:
        counter[item] += 1
    return counter
lst = ['a', 'b', 'a', 'c', 'b', 'a']
incremented_dict = increment_dict_values(lst)
print(incremented_dict)  # Output: {'a': 3, 'b': 2, 'c': 1}
```
---
### 17. How do you create a dictionary of lists in Python?
**Answer:**  
You can create a dictionary of lists using `defaultdict` from the `collections` module.
```python
from collections import defaultdict
def create_dict_of_lists(pairs):
    d = defaultdict(list)
    for key, value in pairs:
        d[key].append(value)
    return d
pairs = [('a', 1), ('b', 2), ('a', 
3), ('b', 4)]
dict_of_lists = create_dict_of_lists(pairs)
print(dict_of_lists)  # Output: {'a': [1, 3], 'b': [2, 4]}
```
---
### 18. How do you merge dictionaries with sum of values for common keys in Python?
**Answer:**  
You can merge dictionaries and sum the values for common keys using `Counter` from the `collections` module.
```python
from collections import Counter
def merge_dicts_with_sum(dict1, dict2):
    return dict(Counter(dict1) + Counter(dict2))
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merged_dict = merge_dicts_with_sum(dict1, dict2)
print(merged_dict)  # Output: {'a': 1, 'b': 5, 'c': 7, 'd': 5}
```
---
### 19. How do you count the frequency of characters in a string using a dictionary in Python?
**Answer:**  
You can count the frequency of characters using a dictionary to keep track of counts.
```python
def count_char_frequency(s):
    freq_dict = {}
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict
s = 'abracadabra'
frequency = count_char_frequency(s)
print(frequency)  # Output: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
```
---
### 20. How do you remove duplicate values from a dictionary in Python?
**Answer:**  
You can remove duplicate values using a dictionary comprehension.
```python
def remove_duplicate_values(d):
    reverse_dict = {}
    for k, v in d.items():
        if v not in reverse_dict.values():
            reverse_dict[k] = v
    return reverse_dict
d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
cleaned_d = remove_duplicate_values(d)
print(cleaned_d)  # Output: {'a': 1, 'b': 2, 'd': 3}
```
---
### 21. How do you flatten a nested dictionary in Python?
**Answer:**  
You can flatten a nested dictionary using a recursive function.
```python
def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
nested_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
flat_dict = flatten_dict(nested_dict)
print(flat_dict)  # Output: {'a': 1, 'b_c': 2, 'b_d_e': 3}
```
---
### 22. How do you create a dictionary with default values for missing keys in Python?
**Answer:**  
You can create a dictionary with default values for missing keys using `defaultdict` from the `collections` module.
```python
from collections import defaultdict
def create_dict_with_defaults():
    return defaultdict(lambda: 'default_value')
d = create_dict_with_defaults()
d['a'] = 1
print(d['a'])  # Output: 1
print(d['b'])  # Output: 'default_value'
```
---
### 23. How do you access nested dictionary keys safely in Python?
**Answer:**  
You can access nested dictionary keys safely using the `get()` method.
```python
def get_nested_key(d, keys):
    for key in keys:
        d = d.get(key, {})
        if not d:
            return None
    return d
nested_dict = {'a': {'b': {'c': 1}}}
value = get_nested_key(nested_dict, ['a', 'b', 'c'])
print(value)  # Output: 1
value = get_nested_key(nested_dict, ['a', 'x', 'c'])
print(value)  # Output: None
```
---
### 24. How do you find the intersection of two dictionaries in Python?
**Answer:**  
You can find the intersection of two dictionaries by keeping common keys and values.
```python
def dict_intersection(dict1, dict2):
    return {k: dict1[k] for k in dict1 if k in dict2 and dict1[k] == dict2[k]}
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}
intersection = dict_intersection(dict1, dict2)
print(intersection)  # Output: {'b': 2}
```
---
### 25. How do you find the difference between two dictionaries in Python?
**Answer:**  
You can find the difference between two dictionaries by keeping keys not common to both dictionaries.
```python
def dict_difference(dict1, dict2):
    return {k: v for k, v in dict1.items() if k not in dict2}
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}
difference = dict_difference(dict1, dict2)
print(difference)  # Output: {'a': 1}
```
---
### 26. How do you filter a dictionary by value in Python?
**Answer:**  
You can filter a dictionary by value using a dictionary comprehension.
```python
def filter_dict_by_value(d, threshold):
    return {k: v for k, v in d.items() if v > threshold}
d = {'a': 1, 'b': 2, 'c': 3}
filtered_d = filter_dict_by_value(d, 1)
print(filtered_d)  # Output: {'b': 2, 'c': 3}
```
---
### 27. How do you find the minimum value in a dictionary in Python?
**Answer:**  
You can find the minimum value using the `min()` function.
```python
def min_value_in_dict(d):
    return min(d.values())
d = {'a': 1, 'b': 3, 'c': 2}
min_value = min_value_in_dict(d)
print(min_value)  # Output: 1
```
---
### 28. How do you find the key of the minimum value in a dictionary in Python?
**Answer:**  
You can find the key of the minimum value using the `min()` function with a key argument.
```python
def key_of_min_value(d):
    return min(d, key=d.get)
d = {'a': 1, 'b': 3, 'c': 2}
key = key_of_min_value(d)
print(key)  # Output: 'a'
```
---
### 29. How do you iterate over dictionary keys and values in Python?
**Answer:**  
You can iterate over dictionary keys and values using a for loop.
```python
def iterate_dict(d):
    for key, value in d.items():
        print(f'{key}: {value}')
d = {'a': 1, 'b': 2, 'c': 3}
iterate_dict(d)
# Output:
# a: 1
# b: 2
# c: 3
```
---
### 30. How do you find the union of multiple dictionaries in Python?
**Answer:**  
You can find the union of multiple dictionaries using the `{**d1, **d2, **d3}` syntax.
```python
def union_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'d': 5}
union = union_dicts(dict1, dict2, dict3)
print(union)  # Output: {'a': 1, 'b': 3, 'c': 4, 'd': 5}
```
---
### 31. How do you replace dictionary values with the sum of same keys in Python?
**Answer:**  
You can replace dictionary values with the sum of same keys using `Counter` from the `collections` module.
```python
from collections import Counter
def replace_with_sum(*dicts):
    total = Counter()
    for d in dicts:
        total.update(d)
    return dict(total)
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'a': 2, 'c': 1}
result = replace_with_sum(dict1, dict2, dict3)
print(result)  # Output: {'a': 3, 'b': 5, 'c': 5}
```
---
### 32. How do you add a prefix or suffix to dictionary keys in Python?
**Answer:**  
You can add a prefix or suffix to dictionary keys using a dictionary comprehension.
```python
def add_prefix_suffix(d, prefix='', suffix=''):
    return {prefix + k + suffix: v for k, v in d.items()}
d
 = {'a': 1, 'b': 2, 'c': 3}
prefixed_d = add_prefix_suffix(d, prefix='pre_')
print(prefixed_d)  # Output: {'pre_a': 1, 'pre_b': 2, 'pre_c': 3}
suffixed_d = add_prefix_suffix(d, suffix='_suf')
print(suffixed_d)  # Output: {'a_suf': 1, 'b_suf': 2, 'c_suf': 3}
```
---
### 33. How do you extract a subset of a dictionary in Python?
**Answer:**  
You can extract a subset of a dictionary by specifying the keys of interest.
```python
def extract_subset(d, keys):
    return {k: d[k] for k in keys if k in d}
d = {'a': 1, 'b': 2, 'c': 3}
keys = ['a', 'c']
subset = extract_subset(d, keys)
print(subset)  # Output: {'a': 1, 'c': 3}
```
---
### 34. How do you map values of a dictionary to another dictionary in Python?
**Answer:**  
You can map values of a dictionary to another dictionary using a dictionary comprehension.
```python
def map_values(d, mapping):
    return {k: mapping.get(v, v) for k, v in d.items()}
d = {'a': 1, 'b': 2, 'c': 3}
mapping = {1: 'one', 2: 'two'}
mapped_d = map_values(d, mapping)
print(mapped_d)  # Output: {'a': 'one', 'b': 'two', 'c': 3}
```
---
### 35. How do you convert two lists into a dictionary with lists as values in Python?
**Answer:**  
You can convert two lists into a dictionary with lists as values using `defaultdict` from the `collections` module.
```python
from collections import defaultdict
def lists_to_dict_of_lists(keys, values):
    d = defaultdict(list)
    for k, v in zip(keys, values):
        d[k].append(v)
    return d
keys = ['a', 'b', 'a', 'c']
values = [1, 2, 3, 4]
dict_of_lists = lists_to_dict_of_lists(keys, values)
print(dict_of_lists)  # Output: {'a': [1, 3], 'b': [2], 'c': [4]}
```
---
### 36. How do you convert a dictionary to a list of key-value tuples in Python?
**Answer:**  
You can convert a dictionary to a list of key-value tuples using the `items()` method.
```python
def dict_to_list_of_tuples(d):
    return list(d.items())
d = {'a': 1, 'b': 2, 'c': 3}
list_of_tuples = dict_to_list_of_tuples(d)
print(list_of_tuples)  # Output: [('a', 1), ('b', 2), ('c', 3)]
```
---
### 37. How do you combine two dictionaries with a function applied to common keys in Python?
**Answer:**  
You can combine two dictionaries and apply a function to common keys using a dictionary comprehension.
```python
def combine_dicts_with_function(dict1, dict2, func):
    combined = {k: func(dict1[k], dict2[k]) for k in dict1 if k in dict2}
    combined.update({k: dict1[k] for k in dict1 if k not in dict2})
    combined.update({k: dict2[k] for k in dict2 if k not in dict1})
    return combined
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
combined_dict = combine_dicts_with_function(dict1, dict2, lambda x, y: x + y)
print(combined_dict)  # Output: {'a': 1, 'b': 5, 'c': 7, 'd': 5}
```
---
### 38. How do you find the symmetric difference of two dictionaries in Python?
**Answer:**  
You can find the symmetric difference of two dictionaries by keeping keys unique to each dictionary.
```python
def dict_symmetric_difference(dict1, dict2):
    return {k: v for k, v in {**dict1, **dict2}.items() if k not in dict1 or k not in dict2}
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}
sym_diff = dict_symmetric_difference(dict1, dict2)
print(sym_diff)  # Output: {'a': 1, 'c': 4, 'd': 5}
```
---
### 39. How do you flatten a dictionary with lists as values in Python?
**Answer:**  
You can flatten a dictionary with lists as values using a dictionary comprehension.
```python
def flatten_dict_with_lists(d):
    return {k: v for k, vals in d.items() for v in vals}
d = {'a': [1, 2], 'b': [3, 4]}
flat_dict = flatten_dict_with_lists(d)
print(flat_dict)  # Output: {'a': 2, 'b': 4}
```
---
### 40. How do you update a nested dictionary in Python?
**Answer:**  
You can update a nested dictionary using a recursive function.
```python
def update_nested_dict(d, updates):
    for k, v in updates.items():
        if isinstance(v, dict) and k in d and isinstance(d[k], dict):
            update_nested_dict(d[k], v)
        else:
            d[k] = v
d = {'a': {'b': 1, 'c': 2}, 'd': 3}
updates = {'a': {'b': 10, 'd': 20}, 'e': 4}
update_nested_dict(d, updates)
print(d)  # Output: {'a': {'b': 10, 'c': 2, 'd': 20}, 'd': 3, 'e': 4}
```
---
### 41. How do you find the most common value in a dictionary in Python?
**Answer:**  
You can find the most common value using the `Counter` from the `collections` module.
```python
from collections import Counter
def most_common_value(d):
    counter = Counter(d.values())
    return counter.most_common(1)[0][0]
d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
common_value = most_common_value(d)
print(common_value)  # Output: 1
```
---
### 42. How do you create a dictionary from a list of keys with the same value in Python?
**Answer:**  
You can create a dictionary from a list of keys with the same value using a dictionary comprehension.
```python
def create_dict_with_same_value(keys, value):
    return {k: value for k in keys}
keys = ['a', 'b', 'c']
value = 0
d = create_dict_with_same_value(keys, value)
print(d)  # Output: {'a': 0, 'b': 0, 'c': 0}
```
---
### 43. How do you remove keys with a specific value from a dictionary in Python?
**Answer:**  
You can remove keys with a specific value using a dictionary comprehension.
```python
def remove_keys_with_value(d, value):
    return {k: v for k, v in d.items() if v != value}
d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
cleaned_d = remove_keys_with_value(d, 1)
print(cleaned_d)  # Output: {'b': 2, 'd': 3}
```
---
### 44. How do you find the sum of all values in a dictionary in Python?
**Answer:**  
You can find the sum of all values using the `sum()` function.
```python
def sum_dict_values(d):
    return sum(d.values())
d = {'a': 1, 'b': 2, 'c': 3}
total = sum_dict_values(d)
print(total)  # Output: 6
```
---
### 45. How do you combine dictionaries by concatenating values in Python?
**Answer:**  
You can combine dictionaries by concatenating values using a dictionary comprehension.
```python
def combine_dicts_concatenate(dict1, dict2):
    return {k: dict1.get(k, '') + dict2.get(k, '') for k in set(dict1) | set(dict2)}
dict1 = {'a': 'hello', 'b': 'world'}
dict2 = {'b': '!', 'c': 'python'}
combined_dict = combine_dicts_concatenate(dict1, dict2)
print(combined_dict)  # Output: {'a': 'hello', 'b': 'world!', 'c': 'python'}
```
---
### 46. How do you create a dictionary from a list of tuples in Python?
**Answer:**  
You can create a dictionary from a list of tuples using the `dict()` constructor.
```python
def tuples_to_dict(tuples):
    return dict(tuples)
tuples = [('a', 1), ('b', 2
), ('c', 3)]
d = tuples_to_dict(tuples)
print(d)  # Output: {'a': 1, 'b': 2, 'c': 3}
```
---
### 47. How do you find the difference in values of common keys between two dictionaries in Python?
**Answer:**  
You can find the difference in values of common keys using a dictionary comprehension.
```python
def dict_value_difference(dict1, dict2):
    return {k: abs(dict1[k] - dict2[k]) for k in dict1 if k in dict2}
dict1 = {'a': 1, 'b': 3, 'c': 5}
dict2 = {'b': 1, 'c': 4, 'd': 7}
difference = dict_value_difference(dict1, dict2)
print(difference)  # Output: {'b': 2, 'c': 1}
```
---
### 48. How do you create a dictionary of sets in Python?
**Answer:**  
You can create a dictionary of sets using `defaultdict` from the `collections` module.
```python
from collections import defaultdict
def create_dict_of_sets(pairs):
    d = defaultdict(set)
    for k, v in pairs:
        d[k].add(v)
    return d
pairs = [('a', 1), ('b', 2), ('a', 3), ('b', 4)]
dict_of_sets = create_dict_of_sets(pairs)
print(dict_of_sets)  # Output: {'a': {1, 3}, 'b': {2, 4}}
```
---
### 49. How do you get the length of a dictionary in Python?
**Answer:**  
You can get the length of a dictionary using the `len()` function.
```python
def dict_length(d):
    return len(d)
d = {'a': 1, 'b': 2, 'c': 3}
length = dict_length(d)
print(length)  # Output: 3
```
---
### 50. How do you map a function over dictionary values in Python?
**Answer:**  
You can map a function over dictionary values using a dictionary comprehension.
```python
def map_function_over_values(d, func):
    return {k: func(v) for k, v in d.items()}
d = {'a': 1, 'b': 2, 'c': 3}
mapped_d = map_function_over_values(d, lambda x: x * 2)
print(mapped_d)  # Output: {'a': 2, 'b': 4, 'c': 6}
```

---
If you found this repository helpful, please give it a star!

Follow me on:
- [LinkedIn](https://www.linkedin.com/in/ashish-jangra/)
- [GitHub](https://github.com/AshishJangra27)
- [Kaggle](https://www.kaggle.com/ashishjangra27)

Stay updated with my latest content and projects!
