# https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python

def number(bus_stops):
    on_board = sum([x[0] for x in bus_stops]) - sum([y[1] for y in bus_stops])
    return on_board





print(number([[1,1], [3, 2], [2, 1]]))