#!/usr/bin/python3

def best_score(a_dictionary):
    """Return key with the highest int value."""

    if not a_dictionary:
        return (None)
    rev_list = sorted(a_dictionary.items(), key=lambda i: i[1], reverse=True)
    return (rev_list[0][0])
