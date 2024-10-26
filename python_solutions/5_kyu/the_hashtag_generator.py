# https://www.codewars.com/kata/52449b062fb80683ec000024/train/python

def generate_hashtag(s):
    """function to create hashtags up to 140 characters with capitalised words and no spaces"""
    if s == "":
        return False
    hashtag = "#" + s.title().replace(" ", "")

    if len(hashtag) > 140:
        return False
    else:
        return hashtag


print(generate_hashtag(" hello world "))
