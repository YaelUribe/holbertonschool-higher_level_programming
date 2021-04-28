#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    positions = dir(hidden_4)
    for x in positions:
        if x[0] == '_':
            continue
        print("{}".format(x))
