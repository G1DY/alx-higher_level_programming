#!/usr/bin/python3
"""defines a matrix division module"""


def matrix_divided(matrix, div):
    """divides integer/float of a matrix

    Args:
        matrix: list of ints and floats
        div: the divisor (int/float)

    Raises:
        TypeError: if the matrix contains non-numbers
        TypeError: if the matrix contains rows of different sizes
        TypeError: if divisor is not an int or float
        ZeroDivisorError: if the denominator in the division is 0
    Returns:
        A new matrix with the result of division
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
