# 50 NumPy Interview Questions and Answers

### 1. How do you create a structured array in NumPy?
**Answer:**  
You can create a structured array using the `np.array` function with a list of tuples and a structured data type.
```python
import numpy as np

data = [(1, 'Alice', 25), (2, 'Bob', 30), (3, 'Charlie', 35)]
dtype = [('id', 'i4'), ('name', 'U10'), ('age', 'i4')]
structured_array = np.array(data, dtype=dtype)
print(structured_array)
# Output: [(1, 'Alice', 25) (2, 'Bob', 30) (3, 'Charlie', 35)]
```
---

### 2. How do you create a boolean mask for an array based on a condition in NumPy?
**Answer:**  
You can create a boolean mask by applying a condition directly to the array.
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
mask = arr > 3
print(mask)
# Output: [False False False  True  True]
```
---

### 3. How do you use the boolean mask to filter an array in NumPy?
**Answer:**  
You can use the boolean mask to filter the array by indexing it with the mask.
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
mask = arr > 3
filtered_arr = arr[mask]
print(filtered_arr)
# Output: [4 5]
```
---

### 4. How do you compute the dot product of two arrays in NumPy?
**Answer:**  
You can compute the dot product using the `np.dot` function.
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
dot_product = np.dot(a, b)
print(dot_product)
# Output: 32
```
---

### 5. How do you compute the cross product of two arrays in NumPy?
**Answer:**  
You can compute the cross product using the `np.cross` function.
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
cross_product = np.cross(a, b)
print(cross_product)
# Output: [-3  6 -3]
```
---

### 6. How do you find the indices of the maximum value in a NumPy array?
**Answer:**  
You can find the indices of the maximum value using the `np.argmax` function.
```python
import numpy as np

arr = np.array([1, 3, 7, 1, 2])
max_index = np.argmax(arr)
print(max_index)
# Output: 2
```
---

### 7. How do you find the indices of the minimum value in a NumPy array?
**Answer:**  
You can find the indices of the minimum value using the `np.argmin` function.
```python
import numpy as np

arr = np.array([1, 3, 7, 1, 2])
min_index = np.argmin(arr)
print(min_index)
# Output: 0
```
---

### 8. How do you calculate the cumulative sum of elements along a given axis in NumPy?
**Answer:**  
You can calculate the cumulative sum using the `np.cumsum` function.
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
cumsum = np.cumsum(arr)
print(cumsum)
# Output: [ 1  3  6 10 15]
```
---

### 9. How do you calculate the cumulative product of elements along a given axis in NumPy?
**Answer:**  
You can calculate the cumulative product using the `np.cumprod` function.
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
cumprod = np.cumprod(arr)
print(cumprod)
# Output: [ 1  2  6 24 120]
```
---

### 10. How do you compute the eigenvalues and eigenvectors of a matrix in NumPy?
**Answer:**  
You can compute the eigenvalues and eigenvectors using the `np.linalg.eig` function.
```python
import numpy as np

matrix = np.array([[4, -2], [1, 1]])
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print(eigenvalues)
# Output: [3. 2.]
print(eigenvectors)
# Output: [[ 0.89442719  0.70710678]
#          [ 0.4472136  -0.70710678]]
```
---

### 11. How do you compute the inverse of a matrix in NumPy?
**Answer:**  
You can compute the inverse using the `np.linalg.inv` function.
```python
import numpy as np

matrix = np.array([[1, 2], [3, 4]])
inverse_matrix = np.linalg.inv(matrix)
print(inverse_matrix)
# Output: [[-2.   1. ]
#          [ 1.5 -0.5]]
```
---

### 12. How do you compute the determinant of a matrix in NumPy?
**Answer:**  
You can compute the determinant using the `np.linalg.det` function.
```python
import numpy as np

matrix = np.array([[1, 2], [3, 4]])
determinant = np.linalg.det(matrix)
print(determinant)
# Output: -2.0000000000000004
```
---

### 13. How do you solve a system of linear equations using NumPy?
**Answer:**  
You can solve a system of linear equations using the `np.linalg.solve` function.
```python
import numpy as np

A = np.array([[3, 1], [1, 2]])
B = np.array([9, 8])
solution = np.linalg.solve(A, B)
print(solution)
# Output: [2. 3.]
```
---

### 14. How do you perform element-wise multiplication of two arrays in NumPy?
**Answer:**  
You can perform element-wise multiplication using the `*` operator.
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = a * b
print(result)
# Output: [ 4 10 18]
```
---

### 15. How do you perform matrix multiplication of two arrays in NumPy?
**Answer:**  
You can perform matrix multiplication using the `np.matmul` function.
```python
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
result = np.matmul(a, b)
print(result)
# Output: [[19 22]
#          [43 50]]
```
---

### 16. How do you compute the QR decomposition of a matrix in NumPy?
**Answer:**  
You can compute the QR decomposition using the `np.linalg.qr` function.
```python
import numpy as np

matrix = np.array([[1, 2], [3, 4]])
Q, R = np.linalg.qr(matrix)
print(Q)
# Output: [[-0.31622777 -0.9486833 ]
#          [-0.9486833   0.31622777]]
print(R)
# Output: [[-3.16227766 -4.42718872]
#          [ 0.          0.63245553]]
```
---

### 17. How do you compute the singular value decomposition (SVD) of a matrix in NumPy?
**Answer:**  
You can compute the SVD using the `np.linalg.svd` function.
```python
import numpy as np

matrix = np.array([[1, 2], [3, 4], [5, 6]])
U, S, V = np.linalg.svd(matrix)
print(U)
# Output: [[-0.2298477   0.88346102  0.40824829]
#          [-0.52474482  0.24078249 -0.81649658]
#          [-0.81964194 -0.40189603  0.40824829]]
print(S)
# Output: [9.52551809 0.51430058]
print(V)
# Output: [[-0.61962948 -0.78489445]
#          [-0.78489445  0.61962948]]
```
---

### 18. How do you generate a random matrix with values drawn from a normal distribution in NumPy?
**Answer:**  
You can generate a random matrix using the `np.random.randn` function.
```python
import numpy as np

random_matrix = np.random.randn(3, 3)
print(random_matrix)
# Output: Random 3x3 matrix with values from normal distribution
```
---

### 19. How do you shuffle the elements of a NumPy array?
**Answer:**  
You can shuffle the elements using the `np.random.shuffle` function.
```python
import numpy as np

arr = np.array([1, 2, 3, 4,

 5])
np.random.shuffle(arr)
print(arr)
# Output: Shuffled array, e.g., [3 1 4 5 2]
```
---

### 20. How do you create a random permutation of a sequence in NumPy?
**Answer:**  
You can create a random permutation using the `np.random.permutation` function.
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
permuted_arr = np.random.permutation(arr)
print(permuted_arr)
# Output: Permuted array, e.g., [3 1 4 5 2]
```
---

### 21. How do you generate random integers within a specified range in NumPy?
**Answer:**  
You can generate random integers using the `np.random.randint` function.
```python
import numpy as np

random_integers = np.random.randint(0, 10, size=5)
print(random_integers)
# Output: Random integers within range [0, 10)
```
---

### 22. How do you create an array with a given shape and all elements set to zero in NumPy?
**Answer:**  
You can create such an array using the `np.zeros` function.
```python
import numpy as np

zero_array = np.zeros((3, 4))
print(zero_array)
# Output: 3x4 array of zeros
```
---

### 23. How do you create an array with a given shape and all elements set to one in NumPy?
**Answer:**  
You can create such an array using the `np.ones` function.
```python
import numpy as np

one_array = np.ones((2, 3))
print(one_array)
# Output: 2x3 array of ones
```
---

### 24. How do you create an identity matrix of a given size in NumPy?
**Answer:**  
You can create an identity matrix using the `np.eye` function.
```python
import numpy as np

identity_matrix = np.eye(3)
print(identity_matrix)
# Output: 3x3 identity matrix
```
---

### 25. How do you create an array with a range of values in NumPy?
**Answer:**  
You can create an array with a range of values using the `np.arange` function.
```python
import numpy as np

range_array = np.arange(0, 10, 2)
print(range_array)
# Output: [0 2 4 6 8]
```
---

### 26. How do you create an array with values evenly spaced between two given values in NumPy?
**Answer:**  
You can create such an array using the `np.linspace` function.
```python
import numpy as np

linspace_array = np.linspace(0, 1, 5)
print(linspace_array)
# Output: [0.   0.25 0.5  0.75 1.  ]
```
---

### 27. How do you concatenate two arrays along a specified axis in NumPy?
**Answer:**  
You can concatenate two arrays using the `np.concatenate` function.
```python
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
concatenated_array = np.concatenate((a, b), axis=0)
print(concatenated_array)
# Output: [[1 2]
#          [3 4]
#          [5 6]]
```
---

### 28. How do you stack arrays vertically in NumPy?
**Answer:**  
You can stack arrays vertically using the `np.vstack` function.
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
stacked_array = np.vstack((a, b))
print(stacked_array)
# Output: [[1 2 3]
#          [4 5 6]]
```
---

### 29. How do you stack arrays horizontally in NumPy?
**Answer:**  
You can stack arrays horizontally using the `np.hstack` function.
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
stacked_array = np.hstack((a, b))
print(stacked_array)
# Output: [1 2 3 4 5 6]
```
---

### 30. How do you split an array into multiple sub-arrays along a specified axis in NumPy?
**Answer:**  
You can split an array using the `np.split` function.
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
split_array = np.split(arr, 3)
print(split_array)
# Output: [array([1, 2]), array([3, 4]), array([5, 6])]
```
---

### 31. How do you compute the outer product of two vectors in NumPy?
**Answer:**  
You can compute the outer product using the `np.outer` function.
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
outer_product = np.outer(a, b)
print(outer_product)
# Output: [[ 4  5  6]
#          [ 8 10 12]
#          [12 15 18]]
```
---

### 32. How do you compute the inner product of two vectors in NumPy?
**Answer:**  
You can compute the inner product using the `np.inner` function.
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
inner_product = np.inner(a, b)
print(inner_product)
# Output: 32
```
---

### 33. How do you compute the Kronecker product of two arrays in NumPy?
**Answer:**  
You can compute the Kronecker product using the `np.kron` function.
```python
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[0, 5], [6, 7]])
kronecker_product = np.kron(a, b)
print(kronecker_product)
# Output: [[ 0  5  0 10]
#          [ 6  7 12 14]
#          [ 0 15  0 20]
#          [18 21 24 28]]
```
---

### 34. How do you compute the matrix rank of an array in NumPy?
**Answer:**  
You can compute the matrix rank using the `np.linalg.matrix_rank` function.
```python
import numpy as np

matrix = np.array([[1, 2], [3, 4]])
rank = np.linalg.matrix_rank(matrix)
print(rank)
# Output: 2
```
---

### 35. How do you compute the Frobenius norm of a matrix in NumPy?
**Answer:**  
You can compute the Frobenius norm using the `np.linalg.norm` function with the `ord='fro'` argument.
```python
import numpy as np

matrix = np.array([[1, 2], [3, 4]])
frobenius_norm = np.linalg.norm(matrix, ord='fro')
print(frobenius_norm)
# Output: 5.477225575051661
```
---

### 36. How do you compute the condition number of a matrix in NumPy?
**Answer:**  
You can compute the condition number using the `np.linalg.cond` function.
```python
import numpy as np

matrix = np.array([[1, 2], [3, 4]])
condition_number = np.linalg.cond(matrix)
print(condition_number)
# Output: 14.933034373659268
```
---

### 37. How do you compute the Moore-Penrose pseudoinverse of a matrix in NumPy?
**Answer:**  
You can compute the pseudoinverse using the `np.linalg.pinv` function.
```python
import numpy as np

matrix = np.array([[1, 2], [3, 4]])
pseudoinverse = np.linalg.pinv(matrix)
print(pseudoinverse)
# Output: [[-2.   1. ]
#          [ 1.5 -0.5]]
```
---

### 38. How do you compute the covariance matrix of an array in NumPy?
**Answer:**  
You can compute the covariance matrix using the `np.cov` function.
```python
import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
cov_matrix = np.cov(data, rowvar=False)
print(cov_matrix)
# Output: [[9.  9.  9. ]
#          [9.  9.  9. ]
#          [9.  9.  9. ]]
```
---

### 39. How do you compute the correlation matrix of an array in NumPy?
**Answer:**  
You can compute the correlation matrix using the `np.corrcoef` function.
```python
import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
corr_matrix = np.corrcoef(data, rowvar=False)
print(corr_matrix)
# Output: [[1

. 1. 1.]
#          [1. 1. 1.]
#          [1. 1. 1.]]
```
---

### 40. How do you compute the standard deviation along a specified axis in NumPy?
**Answer:**  
You can compute the standard deviation using the `np.std` function.
```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
std_dev = np.std(arr, axis=0)
print(std_dev)
# Output: [2.44948974 2.44948974 2.44948974]
```
---

### 41. How do you compute the variance along a specified axis in NumPy?
**Answer:**  
You can compute the variance using the `np.var` function.
```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
variance = np.var(arr, axis=0)
print(variance)
# Output: [6. 6. 6.]
```
---

### 42. How do you compute the median of an array along a specified axis in NumPy?
**Answer:**  
You can compute the median using the `np.median` function.
```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
median = np.median(arr, axis=0)
print(median)
# Output: [4. 5. 6.]
```
---

### 43. How do you compute the mode of an array in NumPy?
**Answer:**  
You can compute the mode using the `stats.mode` function from the `scipy` library.
```python
import numpy as np
from scipy import stats

arr = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
mode = stats.mode(arr)
print(mode)
# Output: ModeResult(mode=array([4]), count=array([4]))
```
---

### 44. How do you generate a 2D grid of coordinates in NumPy?
**Answer:**  
You can generate a 2D grid of coordinates using the `np.meshgrid` function.
```python
import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5])
X, Y = np.meshgrid(x, y)
print(X)
# Output: [[1 2 3]
#          [1 2 3]]
print(Y)
# Output: [[4 4 4]
#          [5 5 5]]
```
---

### 45. How do you interpolate missing values in a NumPy array?
**Answer:**  
You can interpolate missing values using the `np.interp` function.
```python
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, np.nan, 4, np.nan, 16, 25])
nans, x_ = np.isnan(y), lambda z: z.nonzero()[0]
y[nans] = np.interp(x(nans), x_(~nans), y[~nans])
print(y)
# Output: [ 0.  2.  4. 10. 16. 25.]
```
---

### 46. How do you perform linear regression using NumPy?
**Answer:**  
You can perform linear regression using the `np.polyfit` function.
```python
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 2, 4, 6, 8, 10])
coefficients = np.polyfit(x, y, 1)
print(coefficients)
# Output: [2.00000000e+00 4.02163285e-15]
```
---

### 47. How do you create a sliding window view of an array in NumPy?
**Answer:**  
You can create a sliding window view using the `np.lib.stride_tricks.sliding_window_view` function.
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
window_size = 3
sliding_windows = np.lib.stride_tricks.sliding_window_view(arr, window_size)
print(sliding_windows)
# Output: [[1 2 3]
#          [2 3 4]
#          [3 4 5]]
```
---

### 48. How do you find the unique rows in a 2D array in NumPy?
**Answer:**  
You can find the unique rows using the `np.unique` function with the `axis=0` argument.
```python
import numpy as np

arr = np.array([[1, 2], [3, 4], [1, 2], [5, 6]])
unique_rows = np.unique(arr, axis=0)
print(unique_rows)
# Output: [[1 2]
#          [3 4]
#          [5 6]]
```
---

### 49. How do you sort a 2D array by a specific column in NumPy?
**Answer:**  
You can sort a 2D array by a specific column using the `np.argsort` function.
```python
import numpy as np

arr = np.array([[3, 2], [1, 4], [2, 1]])
sorted_arr = arr[arr[:, 0].argsort()]
print(sorted_arr)
# Output: [[1 4]
#          [2 1]
#          [3 2]]
```
---

### 50. How do you create a boolean array where a condition is met in NumPy?
**Answer:**  
You can create a boolean array by applying a condition directly to the array.
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
bool_arr = arr > 3
print(bool_arr)
# Output: [False False False  True  True]
```

If you found this repository helpful, please give it a star!

Follow me on:
- [LinkedIn](https://www.linkedin.com/in/ashish-jangra/)
- [GitHub](https://github.com/AshishJangra27)
- [Kaggle](https://www.kaggle.com/ashishjangra27)

Stay updated with my latest content and projects!
