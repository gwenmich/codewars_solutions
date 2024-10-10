def add_binary(a,b):
    add = a + b
    binary = format(add, 'b')
    return binary

#  OR

def add_binary2(a,b):
    add = a + b
    return bin(add)[2:]