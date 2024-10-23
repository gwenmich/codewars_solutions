# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

def move_zeros(lst):
    for x in lst:
        if x == 0:
            lst.pop(lst.index(x))
            lst.append(0)
    return lst