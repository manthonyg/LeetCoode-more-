def calculate_mode(list):
    import collections
    count = collections.Counter(list)
    return count.most_common(1)