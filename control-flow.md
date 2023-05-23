# Control flow
Certainly! Here are examples of different control flow statements in Python, along with examples showcasing the usage of various data structures:

1. **if-else statement:** Executes a block of code if a certain condition is true, and another block if the condition is false.

```python
# if-else statement
num = 10
if num > 0:
    print("Positive number")
else:
    print("Non-positive number")
```

2. **for loop:** Iterates over a sequence (such as a list, tuple, or string) and executes a block of code for each element.

```python
# for loop with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# for loop with string
my_string = "Hello"
for char in my_string:
    print(char)
```

3. **while loop:** Executes a block of code repeatedly as long as a certain condition is true.

```python
# while loop
count = 0
while count < 5:
    print(count)
    count += 1
```

4. **break statement:** Terminates the innermost loop and moves to the next statement outside the loop.

```python
# break statement in for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)
```

5. **continue statement:** Skips the rest of the current iteration and moves to the next iteration of the loop.

```python
# continue statement in for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
```

6. **try-except statement:** Handles exceptions by catching and handling specific types of errors.

```python
# try-except statement
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero")
```

7. **data structure example (list) with control flow:**
Here's an example that combines a list and a for loop to find the sum of all numbers in the list:

```python
numbers = [1, 2, 3, 4, 5]
sum = 0
for num in numbers:
    sum += num
print("Sum:", sum)
```

8. **data structure example (dictionary) with control flow:**
Here's an example that uses a dictionary and an if-else statement to check if a given key is present:

```python
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
name = "Bob"
if name in student_grades:
    print(name, "has a grade of", student_grades[name])
else:
    print("No grade found for", name)
```

These examples demonstrate the usage of control flow statements in combination with various data structures such as lists, dictionaries, strings, and loops.

In Python, the `or` and `and` operators are used for boolean logic and combining conditional statements. Here are examples of how they work:

1. **`or` operator:**
The `or` operator returns `True` if at least one of the operands is `True`, and `False` otherwise. It evaluates the operands from left to right and short-circuits if a `True` value is found.

```python
x = 5
y = 10
z = 15

result = (x < y) or (z < y)
print(result)  # Output: True
```

In the example above, the condition `(x < y)` is `True`, so the entire expression `(x < y) or (z < y)` evaluates to `True`. The second condition `(z < y)` is not evaluated because the `or` operator short-circuits once a `True` value is found.

2. **`and` operator:**
The `and` operator returns `True` only if both operands are `True`, and `False` otherwise. It evaluates the operands from left to right and short-circuits if a `False` value is found.

```python
x = 5
y = 10
z = 15

result = (x < y) and (z < y)
print(result)  # Output: False
```

In this example, the condition `(x < y)` is `True`, but the second condition `(z < y)` is `False`. Therefore, the entire expression `(x < y) and (z < y)` evaluates to `False`.

The `or` and `and` operators can be used in conditional statements, such as `if` statements, to combine multiple conditions:

```python
x = 5
y = 10
z = 15

if (x < y) and (z < y):
    print("Both conditions are True")
else:
    print("At least one condition is False")
```

Output: `At least one condition is False`

In this example, the `if` statement checks if both conditions `(x < y)` and `(z < y)` are `True`. Since the second condition is `False`, the `else` block is executed.

These examples demonstrate how the `or` and `and` operators can be used to combine boolean conditions in Python for conditional statements and expressions.