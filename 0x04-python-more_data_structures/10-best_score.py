#!/usr/bin/python3
def best_score(a_dictionary):
    score = []
    if a_dictionary:
        for x, y in a_dictionary.items():
            score.append(y)
        score.sort()
        higher = score[-1]
        for x, y in a_dictionary.items():
            if a_dictionary[x] is higher:
                return x
    return None
