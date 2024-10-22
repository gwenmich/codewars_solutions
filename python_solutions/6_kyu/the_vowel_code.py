# https://www.codewars.com/kata/53697be005f803751e0015aa/train/python

def encode(st):
    replacements = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}
    for key, value in replacements.items():
        st = st.replace(key, value)
    return st

def decode(st):
    replacements = {"1": "a", "2": "e", "3": "i", "4": "o", "5": "u"}
    for key, value in replacements.items():
        st = st.replace(key, value)
    return st



