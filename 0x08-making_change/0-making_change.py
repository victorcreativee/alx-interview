#!/usr/bin/python3
"""
Function to determine the fewest number of coins needed
to meet a given amount using dynamic programming.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize a list for storing minimum coins needed for each value up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins to make 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
