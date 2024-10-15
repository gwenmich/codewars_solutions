def count_by(x, n):
    array = []
    for i in range(x, (x * n) + 1):
        if i % x == 0:
            array.append(i)
    return array


# https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python