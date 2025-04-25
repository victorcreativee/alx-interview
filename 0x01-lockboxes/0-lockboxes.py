#!/usr/bin/python3
"""
This module contains the canUnlockAll function.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of lists): A list of boxes with keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    visited = set()
    stack = [0]  # Start with box 0

    while stack:
        box = stack.pop()
        if box not in visited:
            visited.add(box)
            for key in boxes[box]:
                if 0 <= key < n and key not in visited:
                    stack.append(key)

    return len(visited) == n
