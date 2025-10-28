# 50 Python Conditional Questions and Answers

Below are 50 practical Python questions focusing on **if**, **nested if-else**, and multiple **elif**

Each question includes:
- A scenario or requirement
- A code snippet demonstrating one possible solution

---

### 1. Check if a number is even or odd.
**Answer:**  
Use the modulo operator `%` to determine if the number is divisible by 2.
```python
num = 10
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

### 2. Check if a number is positive, negative, or zero.
**Answer:**  
Use if-elif-else conditions to classify the number.
```python
num = -5
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

---

### 3. Determine if a character is a vowel or consonant (assume input is a single lowercase letter).
**Answer:**  
Use if-else to check membership in vowels.
```python
ch = 'e'
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print("Vowel")
else:
    print("Consonant")
```

---

### 4. Check if a year is a leap year.
**Answer:**  
A leap year is divisible by 400, or divisible by 4 but not by 100.
```python
year = 2020
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")
```

---

### 5. Determine a person's stage of life (child, teen, adult, senior) based on age.
**Answer:**  
Use multiple elif conditions for ranges.
```python
age = 45
if age < 13:
    print("Child")
elif age < 20:
    print("Teen")
elif age < 60:
    print("Adult")
else:
    print("Senior")
```

---

### 6. Check if a password meets length criteria (at least 8 characters).
**Answer:**  
Use if-else to check string length.
```python
password = "pass1234"
if len(password) >= 8:
    print("Strong password")
else:
    print("Weak password")
```

---

### 7. Nested if: Check if a number is positive, and if so, whether it's even or odd.
**Answer:**  
First check positivity, then even/odd inside another if.
```python
num = 9
if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Not Positive")
```

---

### 8. Check if two numbers are equal, or if not, determine which is larger.
**Answer:**  
Use if-elif-else to compare.
```python
a = 10
b = 15
if a == b:
    print("Equal")
elif a > b:
    print("a is larger")
else:
    print("b is larger")
```

---

### 9. Determine if a given letter is uppercase, lowercase, or neither.
**Answer:**  
Use str methods isupper() and islower().
```python
ch = 'H'
if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
else:
    print("Neither uppercase nor lowercase")
```

---

### 10. Check if a number is divisible by both 3 and 5.
**Answer:**  
Use multiple conditions with `and`.
```python
num = 30
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by 3 and 5")
else:
    print("Not divisible by both")
```

---

### 11. Determine grade based on score: A(>=90), B(>=80), C(>=70), else F.
**Answer:**  
Use multiple elif conditions.
```python
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

---

### 12. Check if a character is a digit.
**Answer:**  
Use str.isdigit().
```python
ch = '5'
if ch.isdigit():
    print("Digit")
else:
    print("Not a digit")
```

---

### 13. Nested if: If an integer is positive, check if greater than 100 or not.
**Answer:**  
Check positivity, then range.
```python
num = 150
if num > 0:
    if num > 100:
        print("Positive and greater than 100")
    else:
        print("Positive but 100 or less")
else:
    print("Not positive")
```

---

### 14. Determine if a temperature in Celsius is freezing (<0), cold (<15), warm (<25), or hot (else).
**Answer:**  
Use multiple elif for temperature ranges.
```python
temp = 10
if temp < 0:
    print("Freezing")
elif temp < 15:
    print("Cold")
elif temp < 25:
    print("Warm")
else:
    print("Hot")
```

---

### 15. Check if a given number ends with digit 5.
**Answer:**  
Convert to string and check last character.
```python
num = 75
num_str = str(num)
if num_str.endswith('5'):
    print("Ends with 5")
else:
    print("Does not end with 5")
```

---

### 16. Nested if: Check if a number is non-negative, then check if it's zero or positive.
**Answer:**  
Check >=0, then zero or positive inside another if.
```python
num = 0
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")
```

---

### 17. Determine if a character is a punctuation mark (only check . , ! ?).
**Answer:**  
Use if-elif-else with character comparisons.
```python
ch = '?'
if ch == '.' or ch == ',' or ch == '!' or ch == '?':
    print("Punctuation")
else:
    print("Not punctuation")
```

---

### 18. Check if a given name starts with a vowel.
**Answer:**  
Check first character for vowels.
```python
name = "Ashish"
first_char = name[0].lower()
if first_char == 'a' or first_char == 'e' or first_char == 'i' or first_char == 'o' or first_char == 'u':
    print("Starts with vowel")
else:
    print("Does not start with vowel")
```

---

### 19. Multi-elif: Determine time of day by hour (0-23):  
- <6: Early Morning  
- <12: Morning  
- <18: Afternoon  
- <24: Night  
**Answer:**  
Use multiple elif conditions.
```python
hour = 14
if hour < 6:
    print("Early Morning")
elif hour < 12:
    print("Morning")
elif hour < 18:
    print("Afternoon")
elif hour < 24:
    print("Night")
else:
    print("Invalid hour")
```

---

### 20. Check if a username length is valid (5 to 10 chars).
**Answer:**  
Use if-elif-else to check length ranges.
```python
username = "Ashish"
length = len(username)
if length < 5:
    print("Too short")
elif length > 10:
    print("Too long")
else:
    print("Valid length")
```

---

### 21. Nested if: If a number is even, check if it is also divisible by 4.
**Answer:**  
Check even first, then divisibility by 4.
```python
num = 8
if num % 2 == 0:
    if num % 4 == 0:
        print("Even and divisible by 4")
    else:
        print("Even but not divisible by 4")
else:
    print("Odd")
```

---

### 22. Determine if a letter is uppercase vowel, lowercase vowel, uppercase consonant, or lowercase consonant.
**Answer:**  
Use multiple if-elif conditions.
```python
ch = 'U'
vowels = 'aeiouAEIOU'
if ch in vowels:
    if ch.isupper():
        print("Uppercase vowel")
    else:
        print("Lowercase vowel")
else:
    if ch.isupper():
        print("Uppercase consonant")
    else:
        print("Lowercase consonant")
```

---

### 23. Check if a number is within a certain range (e.g., between 1 and 100).
**Answer:**  
Use if-else with range conditions.
```python
num = 50
if 1 <= num <= 100:
    print("Within range")
else:
    print("Out of range")
```

---

### 24. Multi-elif: Classify a number by digit count:  
- Single-digit (|num| < 10)  
- Two-digit (|num| < 100)  
- Three or more digits (|num| >= 100)
**Answer:**  
Use abs() and multiple elif.
```python
num = 999
abs_num = abs(num)
if abs_num < 10:
    print("Single-digit")
elif abs_num < 100:
    print("Two-digit")
else:
    print("Three or more digits")
```

---

### 25. Nested if: If a number is positive, check if it's prime or not by a simple method (just check divisibility by 2 and 3).
**Answer:**  
This is limited without loops or data structures, but let's just show conditions.
```python
num = 9
if num > 0:
    if num == 2 or num == 3:
        print("Prime")
    elif num % 2 != 0 and num % 3 != 0:
        print("Likely prime")
    else:
        print("Not prime")
else:
    print("Not positive")
```

---

### 26. Check if a given string is uppercase, lowercase, or mixed.
**Answer:**  
Use str.isupper() and str.islower().
```python
text = "HELLO"
if text.isupper():
    print("All uppercase")
elif text.islower():
    print("All lowercase")
else:
    print("Mixed case")
```

---

### 27. Multi-elif: BMI Categories:  
- <18.5: Underweight  
- <25: Normal  
- <30: Overweight  
- else: Obese
**Answer:**  
Use multiple elif for ranges.
```python
bmi = 22
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
```

---

### 28. Check if a character is a whitespace.
**Answer:**  
Check if char == ' '.
```python
ch = ' '
if ch == ' ':
    print("Whitespace")
else:
    print("Not whitespace")
```

---

### 29. Nested if: If a number is non-negative, check if it's an exact multiple of 10.
**Answer:**  
First check non-negative, then divisibility by 10.
```python
num = 40
if num >= 0:
    if num % 10 == 0:
        print("Non-negative multiple of 10")
    else:
        print("Non-negative but not multiple of 10")
else:
    print("Negative")
```

---

### 30. Multi-elif: Determine shipping cost by weight category:  
- <=1kg: $5  
- <=5kg: $10  
- <=20kg: $20  
- else: $50
**Answer:**  
Use multiple elif.
```python
weight = 6
if weight <= 1:
    print("$5")
elif weight <= 5:
    print("$10")
elif weight <= 20:
    print("$20")
else:
    print("$50")
```

---

### 31. Check if a given string starts with a capital letter.
**Answer:**  
Check first char using isupper().
```python
text = "Hello"
if text and text[0].isupper():
    print("Starts with capital letter")
else:
    print("Does not start with capital letter")
```

---

### 32. Nested if: If a number is positive, check if it is a perfect square of an integer (just check num==4 or num==9 for simplicity).
**Answer:**  
Restricted check without loops.
```python
num = 9
if num > 0:
    if num == 4 or num == 9:
        print("Positive perfect square (from limited check)")
    else:
        print("Positive but not perfect square (from limited check)")
else:
    print("Not positive")
```

---

### 33. Multi-elif: Classify an angle (in degrees):  
- <90: Acute  
- ==90: Right  
- <180: Obtuse  
- ==180: Straight  
- else: Reflex
**Answer:**  
Use multiple if-elif.
```python
angle = 120
if angle < 90:
    print("Acute")
elif angle == 90:
    print("Right")
elif angle < 180:
    print("Obtuse")
elif angle == 180:
    print("Straight")
else:
    print("Reflex")
```

---

### 34. Check if a number is close to 100 (within +/-10).
**Answer:**  
Use abs difference.
```python
num = 95
if abs(num - 100) <= 10:
    print("Close to 100")
else:
    print("Not close")
```

---

### 35. Nested if: Check if a given code is 'admin', if yes check if 'active' is True, else print restricted access.
**Answer:**  
Simulate user_role and active condition.
```python
user_role = 'admin'
active = True
if user_role == 'admin':
    if active:
        print("Full Access")
    else:
        print("Admin not active")
else:
    print("Restricted Access")
```

---

### 36. Multi-elif: Classify speed (km/h):  
- <30: Slow  
- <60: Normal  
- <100: Fast  
- else: Very Fast
**Answer:**  
Use multiple elif.
```python
speed = 75
if speed < 30:
    print("Slow")
elif speed < 60:
    print("Normal")
elif speed < 100:
    print("Fast")
else:
    print("Very Fast")
```

---

### 37. Determine if a given character is uppercase vowel, uppercase consonant, or not an uppercase letter at all.
**Answer:**  
Nested logic on uppercase and vowels.
```python
ch = 'E'
if ch.isupper():
    if ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        print("Uppercase vowel")
    else:
        print("Uppercase consonant")
else:
    print("Not uppercase letter")
```

---

### 38. If a number is negative, print "Negative". If zero, print "Zero". Otherwise, print "Positive".
**Answer:**  
Simple if-elif-else.
```python
num = 0
if num < 0:
    print("Negative")
elif num == 0:
    print("Zero")
else:
    print("Positive")
```

---

### 39. Check if a string is a palindrome (only check first and last character for demonstration).
**Answer:**  
No data structures, just basic conditions.
```python
text = "madam"
if text and text[0] == text[-1]:
    print("Potential palindrome (first and last char match)")
else:
    print("Not palindrome based on first and last char")
```

---

### 40. Multi-elif: Assign a label based on salary:  
- >100000: "High earner"  
- >50000: "Mid earner"  
- >20000: "Low earner"  
- else: "Very low"
**Answer:**  
Use multiple elif.
```python
salary = 30000
if salary > 100000:
    print("High earner")
elif salary > 50000:
    print("Mid earner")
elif salary > 20000:
    print("Low earner")
else:
    print("Very low")
```

---

### 41. Nested if: If a character is a letter, check if it is uppercase or lowercase.
**Answer:**  
Check if letter using isalpha(), then case.
```python
ch = 'G'
if ch.isalpha():
    if ch.isupper():
        print("Uppercase letter")
    else:
        print("Lowercase letter")
else:
    print("Not a letter")
```

---

### 42. Check if a number is exactly divisible by 2, 3, or 5 (just print the first that applies).
**Answer:**  
Use multiple if/elif.
```python
num = 9
if num % 2 == 0:
    print("Divisible by 2")
elif num % 3 == 0:
    print("Divisible by 3")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 2, 3, or 5")
```

---

### 43. Determine if a string length is odd or even.
**Answer:**  
Use len() % 2.
```python
text = "Hello"
if len(text) % 2 == 0:
    print("Even length")
else:
    print("Odd length")
```

---

### 44. Nested if: If a number > 10, check if it's >50, else just print "Between 10 and 50".
**Answer:**  
Two-level check.
```python
num = 60
if num > 10:
    if num > 50:
        print("Greater than 50")
    else:
        print("Between 10 and 50")
else:
    print("10 or less")
```

---

### 45. Multi-elif: Classify a day number (1=Mon,...7=Sun):  
- 1-5: Weekday  
- 6: Saturday  
- 7: Sunday  
- else: Invalid
**Answer:**  
Use if-elif-else.
```python
day = 7
if day >= 1 and day <= 5:
    print("Weekday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid")
```

---

### 46. Check if a variable is None.
**Answer:**  
Use `is None`.
```python
var = None
if var is None:
    print("var is None")
else:
    print("var has a value")
```

---

### 47. Nested if: If a character is a digit, check if it's even or odd digit.
**Answer:**  
Check digit first, then numeric value.
```python
ch = '4'
if ch.isdigit():
    digit_value = int(ch)
    if digit_value % 2 == 0:
        print("Even digit")
    else:
        print("Odd digit")
else:
    print("Not a digit")
```

---

### 48. Multi-elif: Classify angle speed in degrees per second:  
- <1 deg/s: Very slow  
- <10 deg/s: Slow  
- <100 deg/s: Moderate  
- else: Fast
**Answer:**  
Use multiple elif.
```python
speed = 5
if speed < 1:
    print("Very slow")
elif speed < 10:
    print("Slow")
elif speed < 100:
    print("Moderate")
else:
    print("Fast")
```

---

### 49. Check if a string starts with 'A' and ends with 'Z'.
**Answer:**  
Use conditions on first and last char.
```python
text = "ABCZ"
if text and text[0] == 'A' and text[-1] == 'Z':
    print("Starts with A and ends with Z")
else:
    print("Condition not met")
```

---

### 50. Nested if: If year is divisible by 4, check if also divisible by 100. If yes, then must be divisible by 400 for leap year.
**Answer:**  
Detailed leap year check.
```python
year = 2000
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")
```

---

If you found this helpful, please consider following or starring the repository!

Follow me on:
- [LinkedIn](https://www.linkedin.com/in/ashish-jangra/)
- [GitHub](https://github.com/AshishJangra27)
- [Kaggle](https://www.kaggle.com/ashishjangra27)

Stay updated with my latest content and projects!
