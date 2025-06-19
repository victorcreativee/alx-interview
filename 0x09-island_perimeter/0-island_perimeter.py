#!/usr/bin/python3
"""
Island Perimeter Calculator Module
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in a grid.

    Args:
        grid (list of list of int): 2D grid representing water (0) and land (1)

    Returns:
        int: The perimeter of the island
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Start with 4 edges
                perimeter += 4
                # Subtract edges that are shared with adjacent land cells
                if i > 0 and grid[i - 1][j] == 1:  # Top neighbor
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Left neighbor
                    perimeter -= 2
    return perimeter
