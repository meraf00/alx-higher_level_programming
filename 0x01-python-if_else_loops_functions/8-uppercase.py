#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 97 <= ord(c) < 97 + 26:
            c = chr(ord(c) - 32)
        print(c, end="")
    print("")
