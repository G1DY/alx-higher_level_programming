#!/usr/bin/python3
"""defines a pascal's triangle"""


def pascal_triangle(n):
    """Representation of a pascal triangle of size n"""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        triangle = triangles[-1]
        temporary = [1]
        for i in range(len(triangle) - 1):
            temporary.append(triangle[i] + triangle[i + 1])
        temporary.append(1)
        triangles.append(temporary)
    return triangles
