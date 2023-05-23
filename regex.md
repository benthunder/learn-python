Regular expressions (regex) are powerful tools for pattern matching and manipulation of strings in Python. The `re` module in Python provides functions and methods for working with regular expressions. Here's an example of using regular expressions in Python:

```python
import re

# Match a pattern in a string
text = "Hello, my name is John. Nice to meet you."
pattern = r"John"
result = re.search(pattern, text)
if result:
    print("Pattern found!")
else:
    print("Pattern not found.")

# Extract substrings using regex groups
text = "Date: 2023-05-23"
pattern = r"(\d{4})-(\d{2})-(\d{2})"
result = re.search(pattern, text)
if result:
    year = result.group(1)
    month = result.group(2)
    day = result.group(3)
    print(f"Year: {year}, Month: {month}, Day: {day}")

# Replace substrings using regex
text = "Hello, World!"
pattern = r"World"
new_text = re.sub(pattern, "Python", text)
print(new_text)
```

In the above examples:
1. The `re.search()` function is used to search for a specific pattern within a string. It returns a match object if the pattern is found, or `None` otherwise.

2. Regex groups are defined using parentheses `()`. They allow capturing and extracting specific parts of a matching string using the `group()` method.

3. The `re.sub()` function is used to replace occurrences of a pattern with a specified replacement string.

Regular expressions provide a wide range of features and syntax for matching and manipulating strings. The examples above illustrate just a few basic use cases. For more advanced patterns and techniques, you can refer to the Python documentation on the `re` module.