#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1

    desc = "argument" if argc == 1 else "arguments"
    punctuation = "." if argc == 0 else ":"

    print("{} {}{}".format(argc, desc, punctuation))

    if argc:
        for i, arg in enumerate(sys.argv[1:]):
            print("{}: {}".format(i + 1, arg))
