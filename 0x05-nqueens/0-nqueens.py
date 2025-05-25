#!/usr/bin/python3
"""Solves the N Queens problem"""

import sys


def is_safe(queens, row, col):
    """Check if placing a queen at (row, col) is safe"""
    for r, c in enumerate(queens):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(N):
    """Solve the N Queens problem and print all solutions"""
    def backtrack(row, queens):
        if row == N:
            print([[r, c] for r, c in enumerate(queens)])
            return
        for col in range(N):
            if is_safe(queens, row, col):
                backtrack(row + 1, queens + [col])

    backtrack(0, [])


def main():
    """Main function to parse arguments and initiate solving"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)


if __name__ == "__main__":
    main()
