def high_and_low(numbers):
    num_list = numbers.split()
    num_list = [int(num) for num in num_list]
    lo_to_hi = sorted(num_list)
    return str(lo_to_hi[-1]) + " " + str(lo_to_hi[0])


# example call
# high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")