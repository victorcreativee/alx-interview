#!/usr/bin/python3
"""
Rotate 2D Matrix by 90 degrees clockwise in-place
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a square matrix (n x n) 90 degrees clockwise in-place.
    
    Args:
        matrix (list of list of int): The matrix to rotate
    
    Returns:
        None: The matrix is modified in-place
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            # Swap elements across the diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()
