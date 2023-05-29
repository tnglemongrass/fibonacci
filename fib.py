#!/usr/bin/env python

"""
This module calculates and prints Fibonacci numbers.
"""

import time

def fib(k):
    """Calculate the n-th Fibonacci number."""
    if k <= 0:
        return 0
    if k <= 2:
        return 1
    return fib(k - 1) + fib(k - 2)

def print_fibonacci_range(number_range):
    """Calculate and print the Fibonacci numbers in a range."""
    for number in number_range:
        print(f"{number} -> {fib(number)}")

if __name__ == "__main__":
    start_time = time.time()
    print_fibonacci_range(range(20))
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Total execution time: {execution_time} seconds")
