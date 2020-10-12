def char_count(str):
    import collections
    count = collections.Counter(str.replace(' ',''))
    return count    


print(char_count("an apple a day will keep the doctor away"))
