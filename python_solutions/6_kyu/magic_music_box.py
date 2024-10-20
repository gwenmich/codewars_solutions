# https://www.codewars.com/kata/6710e54f8ef071fe99eebd07/train/python

def magic_music_box(words):
    new_words_set = set()
    notes = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]
    for word in words:
        for note in notes:
            if note in word:
                new_words_set.add(word)
    return new_words_set
