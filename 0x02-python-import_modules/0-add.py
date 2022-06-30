#!/usr/bin/python3
import add_0.add as add
if __name__ == "__main__":
    a = 1
    b = 2    
    print("{0:d} + {1:d} = {2:d}".format(a, b, add(a, b)))
