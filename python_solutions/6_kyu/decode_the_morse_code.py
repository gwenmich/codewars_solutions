# https://www.codewars.com/kata/54b724efac3d5402db00065e/train/python

from preloaded import MORSE_CODE


def decode_morse(morse_code):
    newlist = morse_code.split()
    string = []
    for i in newlist:
        if i == " ":
            string.append(" ")
        string.append(MORSE_CODE[i])
    return "".join(string)
    # return "".join(MORSE_CODE[i] for i in morse_code.split())