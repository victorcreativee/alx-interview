#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
- Input: <IP> - [<date>] "GET /projects/260 HTTP/1.1" <status_code> <file_size>
- After every 10 lines or on KeyboardInterrupt (CTRL + C), prints:
    - Total file size
    - Number of lines per status code (sorted)
"""

import sys

status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_counts = {}
total_size = 0
line_counter = 0


def print_stats():
    """Print the collected metrics"""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")


try:
    for line in sys.stdin:
        line_counter += 1
        try:
            parts = line.strip().split()
            status_code = parts[-2]
            file_size = int(parts[-1])
            total_size += file_size

            if status_code in status_codes:
                if status_code not in status_counts:
                    status_counts[status_code] = 0
                status_counts[status_code] += 1
        except (IndexError, ValueError):
            # Skip lines that are not properly formatted
            continue

        if line_counter % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
