def calculate_mode(list):
    import collections
    maxOccuredList = []
    cache = collections.defaultdict(int)
    max = float('-inf')

    for element in list:
        cache[element] += 1
        if cache[element] > max:
            max = cache[element]
            maxOccuredList = [element]
        elif cache[element] == max:
            maxOccuredList.append(element)
    return maxOccuredList
        