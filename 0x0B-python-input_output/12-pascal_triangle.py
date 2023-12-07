#!/usr/bin/python3
"""12-pascal_triangle Module."""


def pascal_triangle(n):
    """Create a Pascal triangle of n rows."""
    if n <= 0:
        return []
    lOuter = []
    for i in range(n):
        lOuter.append([])
        lOuter[i].append(1)
        if i > 0:
            for j in range(1, i):
                lOuter[i].append(lOuter[i - 1][j] + lOuter[i - 1][j - 1])
            lOuter[i].append(1)
    return lOuter
