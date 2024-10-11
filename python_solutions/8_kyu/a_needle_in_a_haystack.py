# https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python

def find_needle(haystack):
    for word in haystack:
        if word == "needle":
            return f"found the needle at position {haystack.index(word)}"