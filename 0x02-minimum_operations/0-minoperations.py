#!/usr/bin/python3
"""Minimum Operations - returns minimum operations to reach n 'H' characters"""


def minOperations(n):
    """Calculate the fewest number of operations to reach n H characters"""
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        # If n is divisible by the current divisor
        while n % divisor == 0:
            operations += divisor
            n = n // divisor
        divisor += 1

    return operations
