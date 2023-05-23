In Python, the `yield` keyword is used in a function to create a generator. Generators are functions that can be paused and resumed, allowing for the iterative generation of values on-the-fly. When a function encounters a `yield` statement, it temporarily suspends its execution, returns a value, and remembers its state to resume execution later. Here's an example to illustrate the usage of `yield`:

```python
def count_up_to(n):
    i = 0
    while i <= n:
        yield i
        i += 1

# Using the generator function
counter = count_up_to(5)

print(next(counter))  # Output: 0
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
print(next(counter))  # Output: 3
print(next(counter))  # Output: 4
print(next(counter))  # Output: 5

# Iterating over the generator
for num in count_up_to(3):
    print(num)
```

In the example above, the `count_up_to()` function is a generator that yields numbers starting from 0 up to the specified value `n`. When calling `count_up_to(5)`, it returns a generator object. We can use the `next()` function to retrieve the next value from the generator. Each time `yield` is encountered, the function pauses and returns the current value.

In the first part, we manually call `next(counter)` to get each value. In the second part, we iterate over the generator using a `for` loop, which automatically calls `next()` behind the scenes until the generator is exhausted.

Generators are memory-efficient as they produce values on-the-fly, allowing you to work with large or infinite sequences without storing them entirely in memory. They are commonly used in scenarios where you need to iterate over a large dataset or generate values dynamically.

Note that the `yield` statement can be used multiple times in a generator function, and each time it will produce a new value when the generator is iterated.