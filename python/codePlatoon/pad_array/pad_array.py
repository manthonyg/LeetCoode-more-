def pad(list,size,padding = None):
    while len(list) < size:
        for i in range(size-len(list)):
            list.append(padding)
    return list
