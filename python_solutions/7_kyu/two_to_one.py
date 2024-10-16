def longest(a1, a2):
    long_set = set()
    for char1 in a1:
        long_set.add(char1)
    for char2 in a2:
        long_set.add(char2)
    list_char = list(sorted(long_set))
    word = "".join(list_char)
    return word

# Example function call
# longest("hello", "goodbye")

# https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python
