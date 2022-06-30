#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4

    for globalvar in vars(hidden_4).keys():
        if not globalvar.startswith("__"):
            print(globalvar)
