#!/usr/bin/python3

def sieve(n):
    primes = [True for _ in range(n + 1)]
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    count = 0
    result = [0] * (n + 1)
    for i in range(n + 1):
        if primes[i]:
            count += 1
        result[i] = count
    return result


def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    prime_count = sieve(max_n)

    maria = 0
    ben = 0

    for i in range(x):
        if prime_count[nums[i]] % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
