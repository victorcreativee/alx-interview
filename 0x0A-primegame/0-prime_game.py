#!/usr/bin/python3

def sieve(n):
    """Sieve of Eratosthenes to count primes up to n."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    # Count cumulative primes up to n
    prime_count = [0] * (n + 1)
    count = 0
    for i in range(n + 1):
        if primes[i]:
            count += 1
        prime_count[i] = count
    return prime_count


def isWinner(x, nums):
    """Determine who is the winner of each game round."""
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    prime_count = sieve(max_n)

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
    return None
