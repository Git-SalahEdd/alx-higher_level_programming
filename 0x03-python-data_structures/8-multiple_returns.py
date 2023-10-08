#!/usr/bin/python3
def multiple_returns(sentence):
    """function that returns a tuple
    with the length of a string and its first character."""
    sentence_length = len(sentence)
    if not sentence:
        return sentence_length, None
    else:
        fst_char = sentence[0]
    return sentence_length, fst_char
