#!/usr/bin/python3
"""Calculate minimum operations."""

def minOperations(n):
    """Calculates the fewest number of operations to get exactly n H.

    In a text file, there is a single character H. Your text
    editor can execute only two operations in this file:
    Copy All and Paste. Given a number n

    Example:
        n = 9
        H => Copy All => Paste => HH => Paste =>HHH =>
            Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
        Number of operations: 6
    """
    if n <= 1:
        return 0

    i = 2
    operations = 0
    while i <= n:
        if n % i == 0:
            operations += i
            n /= i
        else:
            i += 1
    return operations
