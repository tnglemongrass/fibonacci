#!/usr/bin/env python

"""
This module calculates and prints Fibonacci numbers.
"""

import time
import argparse

def fib(k):
    """Calculate the n-th Fibonacci number."""
    if k <= 0:
        return 0
    if k <= 2:
        return 1
    return fib(k - 1) + fib(k - 2)

def get_fibonacci_range(number_range):
    """Calculate and return the Fibonacci numbers in a range."""
    fibonacci_numbers = []
    for number in number_range:
        fibonacci_numbers.append(fib(number))
    return fibonacci_numbers

def print_fibonacci_range(number_range, verbose=False):
    """Calculate and print the Fibonacci numbers in a range."""
    fibonaccis = get_fibonacci_range(number_range)
    if verbose:
        for number, result in enumerate(fibonaccis):
            print(number + " -> " + result)
    return fibonaccis

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate and print the first n Fibonacci numbers.")
    parser.add_argument("n", type=int, nargs="?", default=20, help="the ending number of the range")
    parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose mode")
    args = parser.parse_args()

    start_time = time.time()
    fibs = print_fibonacci_range(range(args.n + 1), verbose=args.verbose)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Last (" + str(args.n) + "-th) Fibonacci number: " + str(fibs[-1]))
    print("Total execution time: " + str(execution_time) + " seconds")
