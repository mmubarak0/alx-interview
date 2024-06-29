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
    for idx in range(n):
        for idy in range(1, idx + 1):
            if idx > 0:
                p = pascal[idx - 1][idy - 1]
            else:
                p = 0
            if idx > 0 and idy < len(pascal[idx - 1]):
                n = pascal[idx - 1][idy]
            else:
                n = 0
            pascal[idx].append(p + n)
    return pascal
