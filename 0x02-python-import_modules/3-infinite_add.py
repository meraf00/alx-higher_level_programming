#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1

    if argc == 0:
        print(0)

    else:
        print(sum(map(int, sys.argv[1:])))
