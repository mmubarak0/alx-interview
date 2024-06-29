#!/usr/bin/env python3
"""Pascal's Triangle."""


def pascal_triangle(n):
    """
    Create a list of lists of integers.

    representing the Pascal’s triangle of n.
       1
      1 1
     1 2 1
    1 3 3 1
    [
        [], 0 => [1] length = 1
        [], 1 => [1, 1] length = 2
        [], 2 => [1, 2, 1] length = 3
        [], 3 => [1, 3, 3, 1] length = 4
        [], 4 => [1, 4, 6, 4, 1] length = 5
        [], 5 => [1, 5, 10, 10, 5, 1] length = 6
    ]
    """
    pascal = [[1] for _ in range(n)]
    for idx in range(1, n):
        for idy in range(1, idx + 1):
            prev = pascal[idx - 1][idy - 1]
            next = pascal[idx - 1][idy] if idx != idy else 0
            pascal[idx].append(prev + next)
    return pascal
