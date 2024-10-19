# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

def filter_list(l):
    new_list = [i for i in l if type(i) == int]
    return new_list