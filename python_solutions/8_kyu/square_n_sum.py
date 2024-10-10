def square_sum(numbers):
    square_num = []
    for num in numbers:
        square_num.append(num ** 2)
    total = sum(square_num)
    return total