#!/usr/bin/python3
def best_score(a_dictionary):
    score = []
    if a_dictionary:
        for i, j in a_dictionary.items():
            score.append(j)
        score.sort()
        higher = score[-1]
        for i, j in a_dictionary.items():
            if a_dictionary[i] is higher:
                return i
    return None
