def palindrome(word):
    import re
    converted = re.sub('[\W_]+', '', str(word).lower())
    return converted == converted[::-1]


