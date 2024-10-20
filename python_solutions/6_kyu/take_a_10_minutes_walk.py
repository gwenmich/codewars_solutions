def is_valid_walk(walk):
    if len(walk) == 10 and walk.count("w") == walk.count("e") and walk.count("s") == walk.count("n"):
        return True
    else:
        return False


# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python