#!/usr/bin/python3
def multiple_returns(sentence):
    lngth = len(sentence)
    if lngth == 0:
        first = None
    else:
        first = sentence[0]
    return (lngth, first)
