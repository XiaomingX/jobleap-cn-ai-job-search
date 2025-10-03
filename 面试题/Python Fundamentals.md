# 100 Python Fundamental Interview Questions and Answers

### 1. What are the key features of Python programming language?
**Answer:**  
Python is an interpreted, high-level, dynamically typed, and garbage-collected programming language. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

---

### 2. How do you create and initialize a list in Python?
**Answer:**  
A list in Python can be created using square brackets and can contain elements of different data types.
```python
my_list = [1, 2, 3, 'apple', 'banana']
```
---

### 3. How do you perform string formatting in Python?
**Answer:**  
Python provides multiple ways to format strings, including the `format()` method, f-strings (formatted string literals), and the `%` operator.
```python
name = "Ashish"
age = 25
formatted_string = "My name is {} and I am {} years old.".format(name, age)
formatted_string_f = f"My name is {name} and I am {age} years old."
```
---

### 4. What are the different ways to iterate over a list in Python?
**Answer:**  
You can iterate over a list using a `for` loop, `while` loop, list comprehension, or the `map()` function.
```python
my_list = [1, 2, 3, 4, 5]

# Using for loop
for item in my_list:
    print(item)

# Using while loop
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

# Using list comprehension
[print(item) for item in my_list]

# Using map function
list(map(print, my_list))
```
---

### 5. How do you handle exceptions in Python?
**Answer:**  
Exceptions in Python are handled using `try...except` blocks. You can also use `finally` and `else` clauses.
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always execute.")
```
---

### 6. What is the difference between a list and a tuple in Python?
**Answer:**  
Lists are mutable, meaning their elements can be changed, while tuples are immutable, meaning once created, their elements cannot be changed.
```python
# List example
my_list = [1, 2, 3]
my_list[0] = 0

# Tuple example
my_tuple = (1, 2, 3)
# my_tuple[0] = 0  # This will raise a TypeError
```
---

### 7. How do you create a dictionary in Python and access its elements?
**Answer:**  
A dictionary in Python is created using curly braces `{}` and key-value pairs. You can access its elements using keys.
```python
my_dict = {'name': 'Ashish', 'age': 25, 'location': 'Haryana'}

# Accessing elements
name = my_dict['name']
age = my_dict.get('age')
```
---

### 8. What is a set in Python and how is it different from a list?
**Answer:**  
A set is an unordered collection of unique elements. Unlike lists, sets do not allow duplicate elements and do not maintain order.
```python
my_set = {1, 2, 3, 4, 5}

# Adding an element
my_set.add(6)

# Removing an element
my_set.remove(3)
```
---

### 9. How do you define a function in Python?
**Answer:**  
A function in Python is defined using the `def` keyword, followed by the function name and parentheses. The function body is indented.
```python
def greet(name):
    return f"Hello, {name}!"

# Calling the function
print(greet('Ashish'))
```
---

### 10. What are list comprehensions in Python and how do you use them?
**Answer:**  
List comprehensions provide a concise way to create lists. They consist of brackets containing an expression followed by a `for` clause.
```python
# Creating a list of squares
squares = [x**2 for x in range(10)]
```
---

### 11. How do you read from and write to a file in Python?
**Answer:**  
You can read from and write to a file using the `open()` function with appropriate modes ('r' for read, 'w' for write, 'a' for append, etc.).
```python
# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, World!")

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```
---

### 12. How do you work with dates and times in Python?
**Answer:**  
You can work with dates and times using the `datetime` module.
```python
import datetime

# Getting the current date and time
now = datetime.datetime.now()

# Formatting dates
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)
```
---

### 13. What is a lambda function in Python?
**Answer:**  
A lambda function is a small anonymous function defined using the `lambda` keyword. It can have any number of arguments but only one expression.
```python
# Lambda function to add two numbers
add = lambda x, y: x + y
print(add(3, 5))
```
---

### 14. How do you sort a list in Python?
**Answer:**  
You can sort a list using the `sort()` method or the `sorted()` function.
```python
my_list = [3, 1, 4, 2, 5]

# Using sort() method (in-place)
my_list.sort()

# Using sorted() function (returns a new list)
sorted_list = sorted(my_list)
```
---

### 15. How do you create a class and an object in Python?
**Answer:**  
A class in Python is created using the `class` keyword, and an object is created by instantiating the class.
```python
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

# Creating an object
obj = MyClass("Ashish")
print(obj.greet())
```
---

### 16. What are the key differences between Python 2 and Python 3?
**Answer:**  
Some key differences between Python 2 and Python 3 include:
- Print Statement: `print` is a statement in Python 2 but a function in Python 3.
- Division: `/` operator performs integer division in Python 2 and float division in Python 3.
- Unicode: Strings are ASCII by default in Python 2 and Unicode by default in Python 3.

---

### 17. How do you use the `map()` function in Python?
**Answer:**  
The `map()` function applies a given function to all items in an iterable (e.g., list) and returns a map object (an iterator).
```python
def square(x):
    return x**2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

# Converting the map object to a list
squared_numbers_list = list(squared_numbers)
print(squared_numbers_list)
```
---

### 18. How do you use the `filter()` function in Python?
**Answer:**  
The `filter()` function constructs an iterator from elements of an iterable for which a function returns true.
```python
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)

# Converting the filter object to a list
even_numbers_list = list(even_numbers)
print(even_numbers_list)
```
---

### 19. What are the different ways to concatenate strings in Python?
**Answer:**  
You can concatenate strings using the `+` operator, `join()` method, and f-strings.
```python
str1 = "Hello"
str2 = "World"

# Using + operator
result = str1 + " " + str2

# Using join() method
result = " ".join([str1, str2])

# Using f-strings
result = f"{str1} {str2}"
print(result)
```
---

### 20. What are the built-in data structures in Python?
**Answer:**  
Python has several built-in data structures, including lists, tuples, dictionaries, sets, and strings. Each of these data structures has unique properties and use cases.

---

### 21. How do you create and activate a virtual environment in Python?
**Answer:**  
A virtual environment in Python can be created using the `venv` module and activated with the appropriate command for your operating system.
```python
# Creating a virtual environment
python -m venv myenv

# Activating the virtual environment on Windows
myenv\Scripts\activate

# Activating the virtual environment on macOS/Linux
source myenv/bin/activate
```
---

### 22. How do you read and write JSON data in Python?
**Answer:**  
You can read and write JSON data using the `json` module.
```python
import json

# Writing JSON data
data = {'name': 'Ashish', 'age': 25}
with open('data.json', 'w') as file:
    json.dump(data, file)

# Reading JSON data
with open('data.json', 'r') as file:
    data = json.load(file)
print(data)
```
---

### 23. How do you perform list slicing in Python?
**Answer:**  
List slicing allows you to access a subset of elements from a list.
```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Slicing from index 2 to 5
subset = my_list[2:6]

# Slicing with a step of 2
step_slice = my_list[::2]

print(subset)
print(step_slice)
```
---

### 24. How do you remove duplicates from a list in Python?
**Answer:**  
You can remove duplicates from a list by converting it to a set and then back to a list.
```python
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print(unique_list)
```
---

### 25. How do you merge two dictionaries in Python?
**Answer:**  
You can merge two dictionaries using the `update()` method or the `**` unpacking operator.
```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Using update() method
dict1.update(dict2)
print(dict1)

# Using ** unpacking operator (Python 3.5+)
merged_dict = {**dict1, **dict2}
print(merged_dict)
```
---

### 26. How do you check if a key exists in a dictionary in Python?
**Answer:**  
You can check if a key exists in a dictionary using the `in` keyword.
```python
my_dict = {'name': 'Ashish', 'age': 25}

# Checking if key exists
if 'name' in my_dict:
    print("Key exists!")
else:
    print("Key does not exist!")
```
---

### 27. What is the difference between `append()` and `extend()` methods in a list?
**Answer:**  
- `append()` adds its argument as a single element to the end of a list. The length of the list increases by one.
- `extend()` iterates over its argument, adding each element to the list, extending the list.
```python
lst = [1, 2, 3]
lst.append([4, 5])
# lst is now [1, 2, 3, [4, 5]]

lst.extend([4, 5])
# lst is now [1, 2, 3, 4, 5]
```
---

### 28. How do you reverse a list in Python?
**Answer:**  
You can reverse a list using the `reverse()` method or the slicing technique.
```python
my_list = [1, 2, 3, 4, 5]

# Using reverse() method
my_list.reverse()

# Using slicing technique
reversed_list = my_list[::-1]

print(my_list)
print(reversed_list)
```
---

### 29. How do you sort a dictionary by values in Python?
**Answer:**  
You can sort a dictionary by values using the `sorted()` function with a custom key function.
```python
my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict)
```
---

### 30. How do you convert a string to a list of characters in Python?
**Answer:**  
You can convert a string to a list of characters using the `list()` function.
```python
my_string = "hello"
char_list = list(my_string)
print(char_list)
```
---

### 31. How do you check the data type of a variable in Python?
**Answer:**  
You can check the data type of a variable using the `type()` function.
```python
x = 10
print(type(x))

y = "hello"
print(type(y))
```
---

### 32. How do you create a new Python file and run it?
**Answer:**  
You can create a new Python file with a `.py` extension and run it using the `python` command in the terminal or command prompt.
```bash
# Creating a new Python file
echo "print('Hello, World!')" > hello.py

# Running the Python file
python hello.py
```
---

### 33. How do you find the length of a list, string, or dictionary in Python?
**Answer:**  
You can find the length of a list, string, or dictionary using the `len()` function.
```python
my_list = [1, 2, 3]
my_string = "hello"
my_dict = {'a': 1, 'b': 2}

print(len(my_list))
print(len(my_string))
print(len(my_dict))
```
---

### 34. How do you find the maximum and minimum values in a list in Python?
**Answer:**  
You can find the maximum and minimum values in a list using the `max()` and `min()` functions.
```python
my_list = [1, 2, 3, 4, 5]

max_value = max(my_list)
min_value = min(my_list)

print(max_value)
print(min_value)
```
---

### 35. How do you generate random numbers in Python?
**Answer:**  
You can generate random numbers using the `random` module.
```python
import random

# Generate a random integer between 1 and 10
rand_int = random.randint(1, 10)

# Generate a random float between 0 and 1
rand_float = random.random()

print(rand_int)
print(rand_float)
```
---

### 36. How do you remove an element from a list by index in Python?
**Answer:**  
You can remove an element from a list by index using the `pop()` method.
```python
my_list = [1, 2, 3, 4, 5]

# Remove element at index 2
removed_element = my_list.pop(2)

print(removed_element)
print(my_list)
```
---

### 37. How do you remove an element from a list by value in Python?
**Answer:**  
You can remove an element from a list by value using the `remove()` method.
```python
my_list = [1, 2, 3, 4, 5]

# Remove element with value 3
my_list.remove(3)

print(my_list)
```
---

### 38. How do you create a list of even numbers using list comprehension?
**Answer:**  
You can create a list of even numbers using list comprehension with a conditional statement.
```python
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)
```
---

### 39. How do you check if a string contains a substring in Python?
**Answer:**  
You can check if a string contains a substring using the `in` keyword.
```python
my_string = "Hello, World!"
substring = "World"

if substring in my_string:
    print("Substring found!")
else:
    print("Substring not found!")
```
---

### 40. How do you convert a list of strings to a single string in Python?
**Answer:**  
You can convert a list of strings to a single string using the `join()` method.
```python
str_list = ["Hello", "World", "!"]
result_string = " ".join(str_list)
print(result_string)
```
---

### 41. How do you check if a number is even or odd in Python?
**Answer:**  
You can check if a number is even or odd using the modulus operator `%`.
```python
number = 10

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```
---

### 42. How do you find the index of an element in a list in Python?
**Answer:**  
You can find the index of an element in a list using the `index()` method.
```python
my_list = [1, 2, 3, 4, 5]

index = my_list.index(3)
print(index)
```
---

### 43. How do you count the occurrences of an element in a list in Python?
**Answer:**  
You can count the occurrences of an element in a list using the `count()` method.
```python
my_list = [1, 2, 2, 3, 3, 3, 4, 5]

count = my_list.count(3)
print(count)
```
---

### 44. How do you reverse a string in Python?
**Answer:**  
You can reverse a string using slicing.
```python
my_string = "Hello, World!"
reversed_string = my_string[::-1]
print(reversed_string)
```
---

### 45. How do you find the factorial of a number in Python?
**Answer:**  
You can find the factorial of a number using a recursive function or the `math.factorial()` function.
```python
import math

# Using math.factorial()
result = math.factorial(5)
print(result)

# Using recursive function
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result)
```
---

### 46. How do you merge two lists in Python?
**Answer:**  
You can merge two lists using the `+` operator or the `extend()` method.
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using + operator
merged_list = list1 + list2

# Using extend() method
list1.extend(list2)
print(merged_list)
print(list1)
```
---

### 47. How do you create a nested dictionary in Python?
**Answer:**  
You can create a nested dictionary by including dictionaries within a dictionary.
```python
nested_dict = {
    'person1': {'name': 'Ashish', 'age': 25},
    'person2': {'name': 'John', 'age': 30}
}

print(nested_dict)
```
---

### 48. How do you find the intersection of two sets in Python?
**Answer:**  
You can find the intersection of two sets using the `&` operator or the `intersection()` method.
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using & operator
intersection = set1 & set2

# Using intersection() method
intersection = set1.intersection(set2)
print(intersection)
```
---

### 49. How do you convert a list to a tuple in Python?
**Answer:**  
You can convert a list to a tuple using the `tuple()` function.
```python
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)
```
---

### 50. How do you create a list of squares using list comprehension?
**Answer:**  
You can create a list of squares using list comprehension.
```python
squares = [x**2 for x in range(10)]
print(squares)
```
---

### 51. How do you check if a variable is None in Python?
**Answer:**  
You can check if a variable is `None` using the `is` keyword.
```python
x = None

if x is None:
    print("x is None")
else:
    print("x is not None")
```
---

### 52. How do you iterate over a dictionary in Python?
**Answer:**  
You can iterate over a dictionary using a `for` loop to access its keys and values.
```python
my_dict = {'name': 'Ashish', 'age': 25, 'location': 'Haryana'}

# Iterating over keys
for key in my_dict:
    print(key, my_dict[key])

# Iterating over keys and values
for key, value in my_dict.items():
    print(key, value)
```
---

### 53. How do you check if a string is a palindrome in Python?
**Answer:**  
You can check if a string is a palindrome by comparing it with its reverse.
```python
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madonna"))
print(is_palindrome("madam"))
```
---

### 54. How do you check if a number is prime in Python?
**Answer:**  
You can check if a number is prime by verifying that it is only divisible by 1 and itself.
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11))
print(is_prime(4))
```
---

### 55. How do you find the greatest common divisor (GCD) of two numbers in Python?
**Answer:**  
You can find the GCD of two numbers using the `math.gcd()` function.
```python
import math

gcd = math.gcd(48, 18)
print(gcd)
```
---

### 56. How do you create an infinite loop in Python?
**Answer:**  
You can create an infinite loop using the `while` loop with a condition that always evaluates to `True`.
```python
while True:
    print("This is an infinite loop")
```
---

### 57. How do you break out of a loop in Python?
**Answer:**  
You can break out of a loop using the `break` statement.
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```
---

### 58. How do you continue to the next iteration of a loop in Python?
**Answer:**  
You can continue to the next iteration of a loop using the `continue` statement.
```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```
---

### 59. How do you find the sum of all elements in a list in Python?
**Answer:**  
You can find the sum of all elements in a list using the `sum()` function.
```python
my_list = [1, 2, 3, 4, 5]
total_sum = sum(my_list)
print(total_sum)
```
---

### 60. How do you multiply all elements in a list in Python?
**Answer:**  
You can multiply all elements in a list using a loop or the `reduce()` function from the `functools` module.
```python
from functools import reduce

my_list = [1, 2, 3, 4, 5]

# Using a loop
result = 1
for x in my_list:
    result *= x
print(result)

# Using reduce() function
result = reduce(lambda x, y: x * y, my_list)
print(result)
```
---

### 61. How do you find the length of a string in Python?
**Answer:**  
You can find the length of a string using the `len()` function.
```python
my_string = "Hello, World!"
length = len(my_string)
print(length)
```
---

### 62. How do you convert a string to lowercase in Python?
**Answer:**  
You can convert a string to lowercase using the `lower()` method.
```python
my_string = "HELLO, WORLD!"
lowercase_string = my_string.lower()
print(lowercase_string)
```
---

### 63. How do you convert a string to uppercase in Python?
**Answer:**  
You can convert a string to uppercase using the `upper()` method.
```python
my_string = "hello, world!"
uppercase_string = my_string.upper()
print(uppercase_string)
```
---

### 64. How do you remove whitespace from the beginning and end of a string in Python?
**Answer:**  
You can remove whitespace from the beginning and end of a string using the `strip()` method.
```python
my_string = "  Hello, World!  "
stripped_string = my_string.strip()
print(stripped_string)
```
---

### 65. How do you replace a substring in a string in Python?
**Answer:**  
You can replace a substring in a string using the `replace()` method.
```python
my_string = "Hello, World!"
new_string = my_string.replace("World", "Python")
print(new_string)
```
---

### 66. How do you check if a string starts with a specific substring in Python?
**Answer:**  
You can check if a string starts with a specific substring using the `startswith()` method.
```python
my_string = "Hello, World!"
if my_string.startswith("Hello"):
    print("String starts with 'Hello'")
```
---

### 67. How do you check if a string ends with a specific substring in Python?
**Answer:**  
You can check if a string ends with a specific substring using the `endswith()` method.
```python
my_string = "Hello, World!"
if my_string.endswith("World!"):
    print("String ends with 'World!'")
```
---

### 68. How do you split a string into a list of substrings in Python?
**Answer:**  
You can split a string into a list of substrings using the `split()` method.
```python
my_string = "Hello, World!"
substring_list = my_string.split(", ")
print(substring_list)
```
---

### 69. How do you join a list of strings into a single string in Python?
**Answer:**  
You can join a list of strings into a single string using the `join()` method.
```python
str_list = ["Hello", "World", "!"]
result_string = " ".join(str_list)
print(result_string)
```
---

### 70. How do you find the index of a substring in a string in Python?
**Answer:**  
You can find the index of a substring in a string using the `find()` method.
```python
my_string = "Hello, World!"
index = my_string.find("World")
print(index)
```
---

### 71. How do you convert a list of integers to a single integer in Python?
**Answer:**  
You can convert a list of integers to a single integer by converting each element to a string and then joining them.
```python
int_list = [1, 2, 3, 4, 5]
single_integer = int("".join(map(str, int_list)))
print(single_integer)
```
---

### 72. How do you generate a list of random integers in Python?
**Answer:**  
You can generate a list of random integers using the `random` module.
```python
import random

random_integers = [random.randint(1, 100) for _ in range(10)]
print(random_integers)
```
---

### 73. How do you shuffle a list in Python?
**Answer:**  
You can shuffle a list using the `shuffle()` method from the `random` module.
```python
import random

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)
```
---

### 74. How do you find the difference between two sets in Python?
**Answer:**  
You can find the difference between two sets using the `-` operator or the `difference()` method.
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using - operator
difference = set1 - set2

# Using difference() method
difference = set1.difference(set2)
print(difference)
```
---

### 75. How do you find the union of two sets in Python?
**Answer:**  
You can find the union of two sets using the `|` operator or the `union()` method.
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using | operator
union = set1 | set2

# Using union() method
union = set1.union(set2)
print(union)
```
---

### 76. How do you find the symmetric difference between two sets in Python?
**Answer:**  
You can find the symmetric difference between two sets using the `^` operator or the `symmetric_difference()` method.
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using ^ operator
sym_diff = set1 ^ set2

# Using symmetric_difference() method
sym_diff = set1.symmetric_difference(set2)
print(sym_diff)
```
---

### 77. How do you create a frozen set in Python?
**Answer:**  
You can create a frozen set using the `frozenset()` function.
```python
my_set = {1, 2, 3, 4, 5}
frozen_set = frozenset(my_set)
print(frozen_set)
```
---

### 78. How do you create a range of numbers in Python?
**Answer:**  
You can create a range of numbers using the `range()` function.
```python
numbers = range(1, 11)
for number in numbers:
    print(number)
```
---

### 79. How do you iterate over a string in Python?
**Answer:**  
You can iterate over a string using a `for` loop.
```python
my_string = "Hello, World!"
for char in my_string:
    print(char)
```
---

### 80. How do you create a list of tuples in Python?
**Answer:**  
You can create a list of tuples by including tuples within a list.
```python
list_of_tuples = [(1, 'one'), (2, 'two'), (3, 'three')]
print(list_of_tuples)
```
---

### 81. How do you convert a list of tuples to a dictionary in Python?
**Answer:**  
You can convert a list of tuples to a dictionary using the `dict()` function.
```python
list_of_tuples = [(1, 'one'), (2, 'two'), (3, 'three')]
my_dict = dict(list_of_tuples)
print(my_dict)
```
---

### 82. How do you swap the values of two variables in Python?
**Answer:**  
You can swap the values of two variables using tuple unpacking.
```python
a = 1
b = 2

# Swapping values
a, b = b, a
print(a, b)
```
---

### 83. How do you check if a list is empty in Python?
**Answer:**  
You can check if a list is empty by comparing it to an empty list or using the `not` operator.
```python
my_list = []

if not my_list:
    print("List is empty")
else:
    print("List is not empty")
```
---

### 84. How do you find the index of the first occurrence of an element in a list in Python?
**Answer:**  
You can find the index of the first occurrence of an element in a list using the `index()` method.
```python
my_list = [1, 2, 3, 4, 2, 5]
index = my_list.index(2)
print(index)
```
---

### 85. How do you remove the last element from a list in Python?
**Answer:**  
You can remove the last element from a list using the `pop()` method without an argument.
```python
my_list = [1, 2, 3, 4, 5]
last_element = my_list.pop()
print(last_element)
print(my_list)
```
---

### 86. How do you find the sum of digits of an integer in Python?
**Answer:**  
You can find the sum of digits of an integer by converting it to a string, iterating over each character, and summing their integer values.
```python
number = 12345
digit_sum = sum(int(digit) for digit in str(number))
print(digit_sum)
```
---

### 87. How do you flatten a list of lists in Python?
**Answer:**  
You can flatten a list of lists using a list comprehension or the `itertools.chain` method.
```python
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Using list comprehension
flattened_list = [item for sublist in list_of_lists for item in sublist]
print(flattened_list)

# Using itertools.chain
import itertools
flattened_list = list(itertools.chain(*list_of_lists))
print(flattened_list)
```
---

### 88. How do you find the most common element in a list in Python?
**Answer:**  
You can find the most common element in a list using the `collections.Counter` class.
```python
from collections import Counter

my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
most_common_element = Counter(my_list).most_common(1)[0][0]
print(most_common_element)
```
---

### 89. How do you generate a list of squares of even numbers in Python?
**Answer:**  
You can generate a list of squares of even numbers using list comprehension.
```python
squares_of_even_numbers = [x**2 for x in range(20) if x % 2 == 0]
print(squares_of_even_numbers)
```
---

### 90. How do you transpose a matrix in Python?
**Answer:**  
You can transpose a matrix using a nested list comprehension.
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Transposing the matrix
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed_matrix)
```
---

### 91. How do you remove all occurrences of an element from a list in Python?
**Answer:**  
You can remove all occurrences of an element from a list using a list comprehension.
```python
my_list = [1, 2, 2, 3, 4, 4, 5]
element_to_remove = 2

filtered_list = [x for x in my_list if x != element_to_remove]
print(filtered_list)
```
---

### 92. How do you generate a list of random floating-point numbers in Python?
**Answer:**  
You can generate a list of random floating-point numbers using the `random` module.
```python
import random

random_floats = [random.uniform(0, 1) for _ in range(10)]
print(random_floats)
```
---

### 93. How do you find the longest word in a list of words in Python?
**Answer:**  
You can find the longest word in a list of words using the `max()` function with a custom key function.
```python
words = ["apple", "banana", "cherry", "date"]
longest_word = max(words, key=len)
print(longest_word)
```
---

### 94. How do you remove duplicates from a string in Python?
**Answer:**  
You can remove duplicates from a string by converting it to a set and then back to a string.
```python
my_string = "hello"
unique_chars = ''.join(set(my_string))
print(unique_chars)
```
---

### 95. How do you convert a list of strings to a list of integers in Python?
**Answer:**  
You can convert a list of strings to a list of integers using the `map()` function or a list comprehension.
```python
str_list = ["1", "2", "3", "4", "5"]

# Using map() function
int_list = list(map(int, str_list))
print(int_list)

# Using list comprehension
int_list = [int(x) for x in str_list]
print(int_list)
```
---

### 96. How do you count the number of vowels in a string in Python?
**Answer:**  
You can count the number of vowels in a string using a loop or list comprehension.
```python
my_string = "hello world"
vowels = "aeiou"

# Using loop
vowel_count = 0
for char in my_string:
    if char in vowels:
        vowel_count += 1
print(vowel_count)

# Using list comprehension
vowel_count = sum(1 for char in my_string if char in vowels)
print(vowel_count)
```
---

### 97. How do you merge two lists of dictionaries in Python?
**Answer:**  
You can merge two lists of dictionaries using the `+` operator or the `extend()` method.
```python
list1 = [{"a": 1}, {"b": 2}]
list2 = [{"c": 3}, {"d": 4}]

# Using + operator
merged_list = list1 + list2
print(merged_list)

# Using extend() method
list1.extend(list2)
print(list1)
```
---

### 98. How do you find the intersection of multiple sets in Python?
**Answer:**  
You can find the intersection of multiple sets using the `intersection()` method.
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {4, 5, 6, 7}

# Finding intersection of multiple sets
intersection = set1.intersection(set2, set3)
print(intersection)
```
---

### 99. How do you create a dictionary with default values in Python?
**Answer:**  
You can create a dictionary with default values using the `defaultdict` class from the `collections` module.
```python
from collections import defaultdict

# Creating a defaultdict with default value 0
my_dict = defaultdict(lambda: 0)
my_dict['a'] += 1
my_dict['b'] += 2
print(dict(my_dict))
```
---

### 100. How do you calculate the square root of a number in Python?
**Answer:**  
You can calculate the square root of a number using the `math.sqrt()` function or the exponentiation operator `**`.
```python
import math

# Using math.sqrt() function
result = math.sqrt(16)
print(result)

# Using exponentiation operator
result = 16 ** 0.5
print(result)
```
---

If you found this repository helpful, please give it a star!

Follow me on:
- [LinkedIn](https://www.linkedin.com/in/ashish-jangra/)
- [GitHub](https://github.com/AshishJangra27)
- [Kaggle](https://www.kaggle.com/ashishjangra27)

Stay updated with my latest content and projects!
