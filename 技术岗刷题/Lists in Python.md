# 50 Python Lists Interview Questions and Answers

### 1. How do you reverse a list in Python?
**Answer:**  
You can reverse a list using the `reverse()` method or by slicing.
```python
def reverse_list(lst):
    return lst[::-1]

lst = [1, 2, 3, 4, 5]
reversed_lst = reverse_list(lst)
print(reversed_lst)  # Output: [5, 4, 3, 2, 1]
```
---

### 2. How do you remove duplicates from a list in Python?
**Answer:**  
You can remove duplicates by converting the list to a set and back to a list.
```python
def remove_duplicates(lst):
    return list(set(lst))

lst = [1, 2, 2, 3, 4, 4, 5]
unique_lst = remove_duplicates(lst)
print(unique_lst)  # Output: [1, 2, 3, 4, 5]
```
---

### 3. How do you flatten a nested list in Python?
**Answer:**  
You can flatten a nested list using a recursive function.
```python
def flatten_list(nested_lst):
    flat_list = []
    for item in nested_lst:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

nested_lst = [1, [2, [3, 4], 5], 6]
flat_lst = flatten_list(nested_lst)
print(flat_lst)  # Output: [1, 2, 3, 4, 5, 6]
```
---

### 4. How do you find the intersection of two lists in Python?
**Answer:**  
You can find the intersection of two lists using a set intersection.
```python
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]
common_elements = intersection(lst1, lst2)
print(common_elements)  # Output: [4, 5]
```
---

### 5. How do you find the difference between two lists in Python?
**Answer:**  
You can find the difference between two lists using a set difference.
```python
def list_difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]
difference = list_difference(lst1, lst2)
print(difference)  # Output: [1, 2, 3]
```
---

### 6. How do you rotate a list by n elements in Python?
**Answer:**  
You can rotate a list by slicing it at the n-th position and rejoining the slices.
```python
def rotate_list(lst, n):
    return lst[n:] + lst[:n]

lst = [1, 2, 3, 4, 5]
rotated_lst = rotate_list(lst, 2)
print(rotated_lst)  # Output: [3, 4, 5, 1, 2]
```
---

### 7. How do you generate all permutations of a list in Python?
**Answer:**  
You can generate all permutations of a list using a recursive function.
```python
def permutations(lst):
    if len(lst) == 1:
        return [lst]
    perm_list = []
    for i in range(len(lst)):
        for perm in permutations(lst[:i] + lst[i+1:]):
            perm_list.append([lst[i]] + perm)
    return perm_list

lst = [1, 2, 3]
perm_list = permutations(lst)
print(perm_list)  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```
---

### 8. How do you find the kth largest element in a list in Python?
**Answer:**  
You can find the kth largest element by sorting the list and accessing the k-th index from the end.
```python
def kth_largest(lst, k):
    return sorted(lst, reverse=True)[k-1]

lst = [1, 5, 2, 4, 3]
k = 2
kth_largest_element = kth_largest(lst, k)
print(kth_largest_element)  # Output: 4
```
---

### 9. How do you find all the subsets of a list in Python?
**Answer:**  
You can find all subsets of a list using a recursive function.
```python
def subsets(lst):
    if not lst:
        return [[]]
    subs = subsets(lst[1:])
    return subs + [[lst[0]] + sub for sub in subs]

lst = [1, 2, 3]
subsets_lst = subsets(lst)
print(subsets_lst)  # Output: [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
```
---

### 10. How do you merge two sorted lists in Python?
**Answer:**  
You can merge two sorted lists by iterating through both lists and comparing their elements.
```python
def merge_sorted_lists(lst1, lst2):
    merged_lst = []
    i = j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_lst.append(lst1[i])
            i += 1
        else:
            merged_lst.append(lst2[j])
            j += 1
    merged_lst.extend(lst1[i:])
    merged_lst.extend(lst2[j:])
    return merged_lst

lst1 = [1, 3, 5]
lst2 = [2, 4, 6]
merged_lst = merge_sorted_lists(lst1, lst2)
print(merged_lst)  # Output: [1, 2, 3, 4, 5, 6]
```
---

### 11. How do you find the median of a list in Python?
**Answer:**  
You can find the median of a list by sorting it and finding the middle element.
```python
def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 1:
        return sorted_lst[n // 2]
    else:
        mid1, mid2 = sorted_lst[n // 2 - 1], sorted_lst[n // 2]
        return (mid1 + mid2) / 2

lst = [3, 1, 2, 5, 4]
median = find_median(lst)
print(median)  # Output: 3
```
---

### 12. How do you find the longest increasing subsequence in a list in Python?
**Answer:**  
You can find the longest increasing subsequence using dynamic programming.
```python
def longest_increasing_subsequence(lst):
    n = len(lst)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

lst = [10, 22, 9, 33, 21, 50, 41, 60, 80]
lis_length = longest_increasing_subsequence(lst)
print(lis_length)  # Output: 6
```
---

### 13. How do you find the longest common subsequence of two lists in Python?
**Answer:**  
You can find the longest common subsequence using dynamic programming.
```python
def longest_common_subsequence(lst1, lst2):
    m, n = len(lst1), len(lst2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if lst1[i - 1] == lst2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

lst1 = [1, 2, 3, 4, 1]
lst2 = [3, 4, 1, 2, 1, 3]
lcs_length = longest_common_subsequence(lst1, lst2)
print(lcs_length)  # Output: 3
```
---

### 14. How do you find the minimum number of operations to convert one list to another in Python?
**Answer:**  
You can find the minimum number of operations (edit distance) using dynamic programming.
```python
def edit_distance(lst1, lst2):
    m, n = len(lst1), len(lst2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif lst1[i - 1] == lst2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]

lst1 = [1, 2, 3]
lst2 = [2, 3, 4]
distance = edit_distance(lst1, lst2)
print(distance)  # Output: 2
```
---

### 15. How do you partition a list into k equal sum subsets in Python?
**Answer:**  
You can partition a list into k equal sum subsets using backtracking.
```python
def can_partition_k_subsets(nums, k):
    target, rem = divmod(sum(nums), k)
    if rem or max(nums) > target:
        return False
    used = [0] * len(nums)

    def backtrack(i, k, curr_sum):
        if k == 0:
            return True
        if curr_sum == target:
            return backtrack(0, k - 1, 0)
        for j in range(i, len(nums)):
            if not used[j] and curr_sum + nums[j] <= target:
                used[j] = 1
                if backtrack(j + 1, k, curr_sum + nums[j]):
                    return True
                used[j] = 0
        return False

    nums.sort(reverse=True)
    return backtrack(0, k, 0)

nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
can_partition = can_partition_k_subsets(nums, k)
print(can_partition)  # Output: True
```
---

### 16. How do you find the maximum product subarray in a list in Python?
**Answer:**  
You can find the maximum product subarray using dynamic programming.
```python
def max_product_subarray(nums):
    if not nums:
        return 0
    max_product = min_product = result = nums[0]
    for num in nums[1:]:
        candidates = (num, max_product * num, min_product * num)
        max_product = max(candidates)
        min_product = min(candidates)
        result = max(result, max_product)
    return result

nums = [2, 3, -2, 4]
max_product = max_product_subarray(nums)
print(max_product)  # Output: 6
```
---

### 17. How do you find the contiguous subarray with the maximum sum in Python?
**Answer:**  
You can find the contiguous subarray with the maximum sum using Kadane's algorithm.
```python
def max_subarray_sum(nums):
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = max_subarray_sum(nums)
print(max_sum)  # Output: 6
```
---

### 18. How do you find the majority element in a list in Python?
**Answer:**  
You can find the majority element using the Boyer-Moore voting algorithm.
```python
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate

nums = [2, 2, 1, 1, 1, 2, 2]
majority = majority_element(nums)
print(majority)  # Output: 2
```
---

### 19. How do you check if a list contains a cycle in Python?
**Answer:**  
You can check if a list contains a cycle using Floyd's cycle-finding algorithm (tortoise and hare).
```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Example usage
head = ListNode(3)
node2 = ListNode(2)
node0 = ListNode(0)
node4 = ListNode(-4)

head.next = node2
node2.next = node0
node0.next = node4
node4.next = node2

print(has_cycle(head))  # Output: True
```
---

### 20. How do you find the maximum difference between two elements in a list in Python?
**Answer:**  
You can find the maximum difference by iterating through the list and keeping track of the minimum element encountered so far.
```python
def max_difference(nums):
    if len(nums) < 2:
        return 0
    min_element = nums[0]
    max_diff = 0
    for num in nums[1:]:
        if num - min_element > max_diff:
            max_diff = num - min_element
        if num < min_element:
            min_element = num
    return max_diff

nums = [7, 1, 5, 3, 6, 4]
max_diff = max_difference(nums)
print(max_diff)  # Output: 5
```
---

### 21. How do you find the missing number in a list in Python?
**Answer:**  
You can find the missing number using the sum formula for the first n natural numbers.
```python
def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

nums = [3, 0, 1]
missing = missing_number(nums)
print(missing)  # Output: 2
```
---

### 22. How do you find the duplicate number in a list in Python?
**Answer:**  
You can find the duplicate number using the Floyd's cycle-finding algorithm.
```python
def find_duplicate(nums):
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

nums = [1, 3, 4, 2, 2]
duplicate = find_duplicate(nums)
print(duplicate)  # Output: 2
```
---

### 23. How do you find the minimum window substring in a list in Python?
**Answer:**  
You can find the minimum window substring using the sliding window technique.
```python
from collections import Counter

def min_window_substring(s, t):
    if not s or not t:
        return ""
    t_count = Counter(t)
    current_count = Counter()
    start = left = right = 0
    min_len = float("inf")
    required = len(t_count)
    formed = 0
    while right < len(s):
        char = s[right]
        current_count[char] += 1
        if char in t_count and current_count[char] == t_count[char]:
            formed += 1
        while left <= right and formed == required:
            char = s[left]
            if right - left + 1 < min_len:
                start = left
                min_len = right - left + 1
            current_count[char] -= 1
            if char in t_count and current_count[char] < t_count[char]:
                formed -= 1
            left += 1
        right += 1
    return s[start:start + min_len] if min_len != float("inf") else ""

s = "ADOBECODEBANC"
t = "ABC"
min_window = min_window_substring(s, t)
print(min_window)  # Output: BANC
```
---

### 24. How do you merge intervals in a list in Python?
**Answer:**  
You can merge intervals by sorting them and then iterating through the list to combine overlapping intervals.
```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merged_intervals = merge_intervals(intervals)
print(merged_intervals)  # Output: [[1, 6], [8, 10], [15, 18]]
```
---

### 25. How do you find the kth smallest element in a list in Python?
**Answer:**  
You can find the kth smallest element using a min-heap.
```python
import heapq

def kth_smallest(lst, k):
    return heapq.nsmallest(k, lst)[-1]

lst = [7, 10, 4, 3, 20, 15]
k = 3
kth_smallest_element = kth_smallest(lst, k)
print(kth_smallest_element)  # Output: 7
```
---

### 26. How do you find the largest rectangle in a histogram in Python?
**Answer:**  
You can find the largest rectangle in a histogram using a stack.
```python
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    heights.pop()
    return max_area

heights = [2, 1, 5, 6, 2, 3]
max_area = largest_rectangle_area(heights)
print(max_area)  # Output: 10
```
---

### 27. How do you find the product of all elements except self in Python?
**Answer:**  
You can find the product of all elements except self using two auxiliary arrays.
```python
def product_except_self(nums):
    n = len(nums)
    left = [1] * n
    right = [1] * n
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]
    return [left[i] * right[i] for i in range(n)]

nums = [1, 2, 3, 4]
product = product_except_self(nums)
print(product)  # Output: [24, 12, 8, 6]
```
---

### 28. How do you find the sliding window maximum in a list in Python?
**Answer:**  
You can find the sliding window maximum using a deque.
```python
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()
    result = []
    for i, num in enumerate(nums):
        while dq and nums[dq[-1]] <= num:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
sliding_max = max_sliding_window(nums, k)
print(sliding_max)  # Output: [3, 3, 5, 5, 6, 7]
```
---

### 29. How do you find the subarray with the maximum product in Python?
**Answer:**  
You can find the subarray with the maximum product using dynamic programming.
```python
def max_product_subarray(nums):
    if not nums:
        return 0
    max_product = min_product = result = nums[0]
    for num in nums[1:]:
        candidates = (num, max_product * num, min_product * num)
        max_product = max(candidates)
        min_product = min(candidates)
        result = max(result, max_product)
    return result

nums = [2, 3, -2, 4]
max_product = max_product_subarray(nums)
print(max_product)  # Output: 6
```
---

### 30. How do you find the length of the longest valid parentheses substring in Python?
**Answer:**  
You can find the length of the longest valid parentheses substring using a stack.
```python
def longest_valid_parentheses(s):
    stack = []
    max_len = 0
    last_invalid = -1
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    max_len = max(max_len, i - last_invalid)
            else:
                last_invalid = i
    return max_len

s = "(()"
max_len = longest_valid_parentheses(s)
print(max_len)  # Output: 2
```
---

### 31. How do you find the maximum length of a concatenated string with unique characters in Python?
**Answer:**  
You can find the maximum length of a concatenated string with unique characters using backtracking.
```python
def max_length_concatenated_unique(arr):
    def backtrack(idx, curr):
        if len(curr) != len(set(curr)):
            return 0
        max_len = len(curr)
        for i in range(idx, len(arr)):
            max_len = max(max_len, backtrack(i + 1, curr + arr[i]))
        return max_len

    return backtrack(0, "")

arr = ["un", "iq", "ue"]
max_len = max_length_concatenated_unique(arr)
print(max_len)  # Output: 4
```
---

### 32. How do you find the minimum path sum in a grid in Python?
**Answer:**  
You can find the minimum path sum in a grid using dynamic programming.
```python
def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[m - 1][n - 1]

grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
min_sum = min_path_sum(grid)
print(min_sum)  # Output: 7
```
---

### 33. How do you find the longest mountain in a list in Python?
**Answer:**  
You can find the longest mountain using a two-pointer approach.
```python
def longest_mountain(arr):
    n = len(arr)
    if n < 3:
        return 0
    max_len = 0
    i = 1
    while i < n - 1:
        if arr[i - 1] < arr[i] > arr[i + 1]:
            left = right = i
            while left > 0 and arr[left - 1] < arr[left]:
                left -= 1
            while right < n - 1 and arr[right] > arr[right + 1]:
                right += 1
            max_len = max(max_len, right - left + 1)
            i = right
        else:
            i += 1
    return max_len

arr = [2, 1, 4, 7, 3, 2, 5]
max_len = longest_mountain(arr)
print(max_len)  # Output: 5
```
---

### 34. How do you find the longest subarray with sum zero in Python?
**Answer:**  
You can find the longest subarray with sum zero using a hashmap.
```python
def longest_subarray_sum_zero(nums):
    prefix_sum = 0
    max_len = 0
    prefix_sum_map = {}
    for i, num in enumerate(nums):
        prefix_sum += num
        if prefix_sum == 0:
            max_len = i + 1
        elif prefix_sum in prefix_sum_map:
            max_len = max(max_len, i - prefix_sum_map[prefix_sum])
        else:
            prefix_sum_map[prefix_sum] = i
    return max_len

nums = [1, 2, -2, 4, -4]
max_len = longest_subarray_sum_zero(nums)
print(max_len)  # Output: 4
```
---

### 35. How do you find the longest substring without repeating characters in Python?
**Answer:**  
You can find the longest substring without repeating characters using a sliding window.
```python
def longest_substring_without_repeating(s):
    start = max_len = 0
    used_chars = {}
    for i, char in enumerate(s):
        if char in used_chars and start <= used_chars[char]:
            start = used_chars[char] + 1
        max_len = max(max_len, i - start + 1)
        used_chars[char] = i
    return max_len

s = "abcabcbb"
max_len = longest_substring_without_repeating(s)
print(max_len)  # Output: 3
```
---

### 36. How do you find the longest common prefix in a list of strings in Python?
**Answer:**  
You can find the longest common prefix by comparing characters of each string in the list.
```python
def longest_common_prefix(strings):
    if not strings:
        return ""
    prefix = strings[0]
    for string in strings[1:]:
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:len(prefix)-1]
    return prefix

strings = ["flower", "flow", "flight"]
prefix = longest_common_prefix(strings)
print(prefix)  # Output: fl
```
---

### 37. How do you find the maximum sum subarray with at most k elements in Python?
**Answer:**  
You can find the maximum sum subarray with at most k elements using a sliding window.
```python
def max_sum_subarray_with_k_elements(nums, k):
    max_sum = float('-inf')
    current_sum = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        if i >= k:
            current_sum -= nums[i - k]
        max_sum = max(max_sum, current_sum)
    return max_sum

nums = [2, 1, 5, 1, 3, 2]
k = 3
max_sum = max_sum_subarray_with_k_elements(nums, k)
print(max_sum)  # Output: 9
```
---

### 38. How do you find the maximum sum of a subarray with at most two distinct elements in Python?
**Answer:**  
You can find the maximum sum of a subarray with at most two distinct elements using a sliding window.
```python
def max_sum_subarray_with_two_distinct(nums):
    start = max_sum = 0
    current_sum = 0
    count = {}
    for end, num in enumerate(nums):
        count[num] = count.get(num, 0) + 1
        current_sum += num
        while len(count) > 2:
            count[nums[start]] -= 1
            current_sum -= nums[start]
            if count[nums[start]] == 0:
                del count[nums[start]]
            start += 1
        max_sum = max(max_sum, current_sum)
    return max_sum

nums = [1, 2, 1, 2, 3]
max_sum = max_sum_subarray_with_two_distinct(nums)
print(max_sum)  # Output: 6
```
---

### 39. How do you find the maximum sum of a subarray with at most one element replaced in Python?
**Answer:**  
You can find the maximum sum of a subarray with at most one element replaced using dynamic programming.
```python
def max_sum_subarray_with_one_replacement(nums):
    max_end_here = max_so_far = nums[0]
    max_end_here_with_replacement = max_so_far_with_replacement = float('-inf')
    for i in range(1, len(nums)):
        max_end_here_with_replacement = max(max_end_here, max_end_here_with_replacement + nums[i], nums[i])
        max_end_here = max(max_end_here + nums[i], nums[i])
        max_so_far_with_replacement = max(max_so_far_with_replacement, max_end_here_with_replacement)
        max_so_far = max(max_so_far, max_end_here)
    return max(max_so_far, max_so_far_with_replacement)

nums = [2, 1, -1, 5, -1, 3]
max_sum = max_sum_subarray_with_one_replacement(nums)
print(max_sum)  # Output: 9
```
---

### 40. How do you find the minimum number of steps to make an array non-decreasing in Python?
**Answer:**  
You can find the minimum number of steps to make an array non-decreasing using dynamic programming.
```python
def min_steps_to_non_decreasing(nums):
    n = len(nums)
    dp = [0] * n
    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            dp[i] = dp[i - 1] + 1
    return dp[-1]

nums = [3, 2, 1, 4, 5]
min_steps = min_steps_to_non_decreasing(nums)
print(min_steps)  # Output: 2
```
---

### 41. How do you find the maximum sum of a subarray with at most k changes in Python?
**Answer:**  
You can find the maximum sum of a subarray with at most k changes using dynamic programming.
```python
def max_sum_subarray_with_k_changes(nums, k):
    n = len(nums)
    max_sum = [0] * (k + 1)
    for i in range(n):
        for j in range(k, 0, -1):
            max_sum[j] = max(max_sum[j], max_sum[j - 1] + nums[i])
        max_sum[0] += nums[i]
    return max(max_sum)

nums = [1, -2, 3, 5, -1, 2]
k = 2
max_sum = max_sum_subarray_with_k_changes(nums, k)
print(max_sum)  # Output: 11
```
---

### 42. How do you find the longest subarray with sum at most k in Python?
**Answer:**  
You can find the longest subarray with sum at most k using a sliding window.
```python
def longest_subarray_with_sum_at_most_k(nums, k):
    start = max_len = 0
    current_sum = 0
    for end in range(len(nums)):
        current_sum += nums[end]
        while current_sum > k:
            current_sum -= nums[start]
            start += 1
        max_len = max(max_len, end - start + 1)
    return max_len

nums = [1, 2, 1, 0, 1, 1, 0]
k = 4
max_len = longest_subarray_with_sum_at_most_k(nums, k)
print(max_len)  # Output: 6
```
---

### 43. How do you find the number of subarrays with sum exactly equal to k in Python?
**Answer:**  
You can find the number of subarrays with sum exactly equal to k using a hashmap.
```python
def subarray_sum_equals_k(nums, k):
    prefix_sum = 0
    count = 0
    prefix_sum_map = {0: 1}
    for num in nums:
        prefix_sum += num
        if prefix_sum - k in prefix_sum_map:
            count += prefix_sum_map[prefix_sum - k]
        prefix_sum_map[prefix_sum] = prefix_sum_map.get(prefix_sum, 0) + 1
    return count

nums = [1, 1, 1]
k = 2
num_subarrays = subarray_sum_equals_k(nums, k)
print(num_subarrays)  # Output: 2
```
---

### 44. How do you find the maximum sum of a circular subarray in Python?
**Answer:**  
You can find the maximum sum of a circular subarray using Kadane's algorithm.
```python
def max_subarray_sum_circular(nums):
    def kadane(nums):
        max_current = max_global = nums[0]
        for num in nums[1:]:
            max_current = max(num, max_current + num)
            if max_current > max_global:
                max_global = max_current
        return max_global

    max_kadane = kadane(nums)
    max_wrap = sum(nums) - kadane([-num for num in nums])
    return max(max_kadane, max_wrap)

nums = [1, -2, 3, -2]
max_sum = max_subarray_sum_circular(nums)
print(max_sum)  # Output: 3
```
---

### 45. How do you find the smallest subarray with sum at least k in Python?
**Answer:**  
You can find the smallest subarray with sum at least k using a sliding window.
```python
def smallest_subarray_with_sum_at_least_k(nums, k):
    start = 0
    current_sum = 0
    min_len = float('inf')
    for end in range(len(nums)):
        current_sum += nums[end]
        while current_sum >= k:
            min_len = min(min_len, end - start + 1)
            current_sum -= nums[start]
            start += 1
    return min_len if min_len != float('inf') else 0

nums = [2, 3, 1, 2, 4, 3]
k = 7
min_len = smallest_subarray_with_sum_at_least_k(nums, k)
print(min_len)  # Output: 2
```
---

### 46. How do you find the minimum number of jumps to reach the end of the array in Python?
**Answer:**  
You can find the minimum number of jumps using dynamic programming.
```python
def min_jumps_to_reach_end(nums):
    if len(nums) <= 1:
        return 0
    if nums[0] == 0:
        return -1
    max_reach = nums[0]
    step = nums[0]
    jump = 1
    for i in range(1, len(nums)):
        if i == len(nums) - 1:
            return jump
        max_reach = max(max_reach, i + nums[i])
        step -= 1
        if step == 0:
            jump += 1
            if i >= max_reach:
                return -1
            step = max_reach - i
    return -1

nums = [2, 3, 1, 1, 4]
min_jumps = min_jumps_to_reach_end(nums)
print(min_jumps)  # Output: 2
```
---

### 47. How do you find the number of islands in a 2D grid in Python?
**Answer:**  
You can find the number of islands using depth-first search (DFS).
```python
def num_islands(grid):
    if not grid:
        return 0
    def dfs(grid, r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        dfs(grid, r - 1, c)
        dfs(grid, r + 1, c)
        dfs(grid, r, c - 1)
        dfs(grid, r, c + 1)
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                count += 1
                dfs(grid, r, c)
    return count

grid = [['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']]
num_islands_count = num_islands(grid)
print(num_islands_count)  # Output: 3
```
---

### 48. How do you find the largest connected component in a graph in Python?
**Answer:**  
You can find the largest connected component using depth-first search (DFS).
```python
def largest_connected_component(graph):
    def dfs(node, visited):
        stack = [node]
        component_size = 0
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                component_size += 1
                stack.extend(graph[curr])
        return component_size

    visited = set()
    max_size = 0
    for node in graph:
        if node not in visited:
            max_size = max(max_size, dfs(node, visited))
    return max_size

graph = {1: [2, 3], 2: [1, 4], 3: [1], 4: [2, 5], 5: [4]}
largest_component_size = largest_connected_component(graph)
print(largest_component_size)  # Output: 5
```
---

### 49. How do you find the length of the longest path in a tree in Python?
**Answer:**  
You can find the length of the longest path (diameter) in a tree using depth-first search (DFS).
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def diameter_of_binary_tree(root):
    def dfs(node):
        nonlocal diameter
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        diameter = max(diameter, left + right)
        return max(left, right) + 1

    diameter = 0
    dfs(root)
    return diameter

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(diameter_of_binary_tree(root))  # Output: 3
```
---

### 50. How do you find the longest increasing path in a matrix in Python?
**Answer:**  
You can find the longest increasing path using dynamic programming and depth-first search (DFS).
```python
def longest_increasing_path(matrix):
    if not matrix or not matrix[0]:
        return 0

    def dfs(x, y):
        if dp[x][y] != -1:
            return dp[x][y]
        max_len = 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] > matrix[x][y]:
                max_len = max(max_len, 1 + dfs(nx, ny))
        dp[x][y] = max_len
        return max_len

    rows, cols = len(matrix), len(matrix[0])
    dp = [[-1] * cols for _ in range(rows)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_path = 0
    for i in range(rows):
        for j in range(cols):
            max_path = max(max_path, dfs(i, j))
    return max_path

matrix = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]
longest_path = longest_increasing_path(matrix)
print(longest_path)  # Output: 4
```
---

If you found this repository helpful, please give it a star!

Follow me on:
- [LinkedIn](https://www.linkedin.com/in/ashish-jangra/)
- [GitHub](https://github.com/AshishJangra27)
- [Kaggle](https://www.kaggle.com/ashishjangra27)

Stay updated with my latest content and projects!
