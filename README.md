Fibonacci Number Calculator
===========================

This Python module calculates and prints Fibonacci numbers. It provides a function to calculate the n-th Fibonacci number and another function to print a range of Fibonacci numbers. The module also measures the execution time for the calculations.

Usage
-----
```python
from fibonacci import print_fibonacci_range

# Calculate and print the Fibonacci numbers in a given range
print_fibonacci_range(number_range)
```

Functionality
-------------
The module contains the following functions:

- `fib(k)`: This function calculates and returns the n-th Fibonacci number.
  - Input: `k` - The index of the Fibonacci number to calculate.
  - Output: Returns the n-th Fibonacci number.

- `print_fibonacci_range(number_range)`: This function calculates and prints a range of Fibonacci numbers.
  - Input: `number_range` - The range of Fibonacci numbers to calculate and print.
  - Output: Prints the Fibonacci numbers in the specified range.

Example
-------
```python
from fibonacci import print_fibonacci_range

# Print the Fibonacci numbers in the range [0, 20)
print_fibonacci_range(range(20))
```

This will calculate and print the Fibonacci numbers from 0 to 19.

CLI Options
-----------

The following command-line options are available:

- `n` (optional): The ending number of the range. Defaults to 20.
- `-v` or `--verbose` (optional): Enable verbose mode.

Example usage:

```shell
python fibonacci.py 10 -v
```

Execution Time
--------------
The execution time for the Fibonacci calculations is measured and displayed at the end of the program.
