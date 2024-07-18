#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics."""

import sys

if __name__ == "__main__":
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for i, line in enumerate(sys.stdin, 1):
            split_line = line.split()
            if len(split_line) > 2:
                total_size += int(split_line[-1])
                status_code = split_line[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
            if i % 10 == 0:
                print("File size: {}".format(total_size))
                for k, v in sorted(status_codes.items()):
                    if v != 0:
                        print("{}: {}".format(k, v))
    except KeyboardInterrupt:
        pass
    finally:
        print("File size: {}".format(total_size))
        for k, v in sorted(status_codes.items()):
            if v != 0:
                print("{}: {}".format(k, v))
