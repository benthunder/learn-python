In Python, `async` and `await` are used to define and work with asynchronous code using the `asyncio` module. Asynchronous programming allows for concurrent execution of tasks without blocking the program's flow. Here's an example that demonstrates the usage of `async` and `await`:

```python
import asyncio

# Asynchronous function
async def greet(name):
    print(f"Hello, {name}!")
    await asyncio.sleep(1)  # Simulate some asynchronous operation
    print(f"Goodbye, {name}!")

# Synchronous function
def sync_greet(name):
    print(f"Hello, {name}!")
    print(f"Goodbye, {name}!")

# Asynchronous code
async def main():
    await greet("Alice")
    await greet("Bob")

# Synchronous code
def sync_main():
    sync_greet("Alice")
    sync_greet("Bob")

# Run asynchronous code
asyncio.run(main())

# Run synchronous code
sync_main()
```

In the example above, we define an asynchronous function `greet()` that prints a greeting message, waits for 1 second using `await asyncio.sleep(1)` to simulate an asynchronous operation, and then prints a farewell message. This function uses the `async` keyword to indicate that it is an asynchronous function.

We also have a synchronous function `sync_greet()` that performs the same task but without the use of `async` and `await`.

The `main()` function is an asynchronous code block that calls the `greet()` function using `await` to wait for each greeting to complete before proceeding to the next one.

To run the asynchronous code, we use `asyncio.run(main())`, which runs the `main()` function in an event loop.

The `sync_main()` function demonstrates the execution of synchronous code by calling the `sync_greet()` function directly.

When you run this code, you will see the greetings and farewells being printed asynchronously for "Alice" and "Bob", with a delay of 1 second between each message. The synchronous code will print the greetings and farewells one after the other without any delay.

Asynchronous programming is useful when dealing with I/O-bound operations, such as network requests or file operations, where the program can continue executing other tasks while waiting for the I/O operation to complete. It allows for better utilization of system resources and can lead to improved performance in such scenarios.