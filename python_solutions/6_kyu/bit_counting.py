# https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python

def count_bits(n):
    binary_num = bin(n)[2:]
    return sum(int(x) for x in str(binary_num))



