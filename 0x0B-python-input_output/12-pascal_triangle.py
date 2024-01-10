#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(n):
    """Representation"""
    if n <= 0:
        return []

    tri = [[1]]
    while len(tri) != n:
        prev = tri[-1]
        curr = [1]
        for inc in range(len(prev) - 1):
            curr.append(prev[inc] + prev[inc + 1])
        curr.append(1)
        tri.append(curr)
    return (tri)
