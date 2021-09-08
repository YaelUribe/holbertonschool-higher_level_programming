#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    position = dir(hidden_4)
    for y in position:
        if y[0] == '_':
            continue
        print("{}".format(y))
