#!/usr/bin/python3
""" Log parsing script """
import sys
import signal

# Track total file size and counts of each status code
total_size = 0
status_counts = {}
valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

# For every 10 lines
line_count = 0


def print_stats():
    """Prints current accumulated statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")


try:
    for line in sys.stdin:
        line_count += 1

        try:
            parts = line.strip().split()
            status_code = parts[-2]
            file_size = int(parts[-1])

            total_size += file_size

            if status_code in valid_status_codes:
                if status_code not in status_counts:
                    status_counts[status_code] = 0
                status_counts[status_code] += 1
        except (IndexError, ValueError):
            # Skip malformed lines
            continue

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

# Print stats after all input is read (EOF)
print_stats()
