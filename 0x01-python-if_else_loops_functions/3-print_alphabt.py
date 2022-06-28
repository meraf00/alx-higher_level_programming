#!/usr/bin/python3
for c in range(26):
    if not chr(c + 97) in "eq":
        print("{0}".format(chr(c + 97)), end="")
