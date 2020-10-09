def anagrams_for(word, list_of_words):
    base = sorted(word)
    answer = []
    for item in list_of_words:
        if base == sorted(item):
            answer.append(item)
    return answer

