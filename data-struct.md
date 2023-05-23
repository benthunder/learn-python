In Python, the `struct` module is used to work with binary data, allowing you to convert between binary data and Python objects. However, if you're looking for an overview of all data structures in Python, beyond just the `struct` module, here are some commonly used data structures with examples:

1. **List:** A list is a collection of items that can be of different types and is denoted by square brackets.

```python
# Creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list)  # [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])  # 1
print(my_list[2:4])  # [3, 4]

# Modifying elements
my_list[1] = 10
print(my_list)  # [1, 10, 3, 4, 5]

# List methods
my_list.append(6)
print(my_list)  # [1, 10, 3, 4, 5, 6]

my_list.remove(3)
print(my_list)  # [1, 10, 4, 5, 6]
```

2. **Tuple:** A tuple is an immutable collection of objects and is denoted by parentheses.

```python
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # (1, 2, 3, 4, 5)

# Accessing elements
print(my_tuple[0])  # 1
print(my_tuple[2:4])  # (3, 4)
```

3. **Set:** A set is an unordered collection of unique elements and is denoted by curly braces or the `set()` function.

```python
# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # {1, 2, 3, 4, 5}

# Modifying a set
my_set.add(6)
print(my_set)  # {1, 2, 3, 4, 5, 6}

my_set.remove(3)
print(my_set)  # {1, 2, 4, 5, 6}
```

4. **Dictionary:** A dictionary is an unordered collection of key-value pairs, where each key is unique and is denoted by curly braces or the `dict()` function.

```python
# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict)  # {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing values
print(my_dict['name'])  # 'John'

# Modifying values
my_dict['age'] = 35
print(my_dict)  # {'name': 'John', 'age': 35, 'city': 'New York'}

# Dictionary methods
my_dict.pop('city')
print(my_dict)  # {'name': 'John', 'age': 35}
```

5. **Deque:** A deque (double-ended queue) is a list-like sequence optimized for quick append and pop operations from both ends.

```python
from collections import deque

# Creating a deque
my_deque = deque([1, 2, 3, 4, 5])
print(my_deque)  # deque([1, 2, 3, 4, 5])

# Modifying

 a deque
my_deque.append(6)
print(my_deque)  # deque([1, 2, 3, 4, 5, 6])

my_deque.pop()
print(my_deque)  # deque([1, 2, 3, 4, 5])
```

These are just a few examples of commonly used data structures in Python. Python provides additional built-in data structures and libraries that offer more specialized data structures, such as `heapq`, `collections`, and `numpy`, depending on your specific needs.