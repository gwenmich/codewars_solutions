def remove_smallest(numbers):
    if numbers == []:
        return []
    else:
        new_list = sorted(numbers)
        new_list.pop(0)
        return new_list


print(remove_smallest([2, 6, 5, 8, 1]))