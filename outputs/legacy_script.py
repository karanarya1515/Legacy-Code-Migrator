 Here is a modernized version of the given C-like Python code, using modern Python syntax and features:

```python
def main():
    for i in range(10):
        print(f"Number {i}")

if __name__ == "__main__":
    main()
```

Let's break down the changes step by step:

1. Removed the `#include <stdio.h>` as it is not Python code but a C preprocessor command.

2. Changed the function name from `main()` to `def main():`. In Python, we use the `def` keyword to define functions.

3. Replaced the for loop using `for i in range(10)`. This is a more idiomatic way of handling loops in Python.

4. Added an f-string (`f"Number {i}")`) for printing formatted strings, which is a modern way to format strings in Python.

5. Wrapped the code inside an `if __name__ == "__main__":` block. This ensures that the function defined within it will only be executed when the script is run directly (as opposed to being imported as a module).