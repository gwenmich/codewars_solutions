# https://www.codewars.com/kata/5679aa472b8f57fb8c000047

def find_even_index(arr):
    for n in range(len(arr)):
        if sum(arr[0:n]) == sum(arr[n + 1:]):
            return n
    return -1