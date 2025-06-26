#!/usr/bin/python3
"""
Prime Game
"""


def sieve(n):
    """Returns a list of booleans where index is True if it's a prime."""
    primes = [True for _ in range(n + 1)]
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes


def isWinner(x, nums):
    """
    Determines the winner of each round of the prime game.
    x: number of rounds
    nums: list of 'n' values for each round
    Return: name of the player who won the most rounds, or None
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    prime_flags = sieve(max_n)

    # Compute prefix sum of prime counts up to max_n
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if prime_flags[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
