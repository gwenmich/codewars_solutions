# https://www.codewars.com/kata/596fba44963025c878000039/train/python

def contamination(text, char):
    new_text = ""
    for letter in text:
        if letter == " ":
            return" "
        else:
            new_text += char
    return new_text


