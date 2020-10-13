def binary_search(target,values):
    middle = len(values) // 2
    if len(values) == 0:
        return -1
    elif values[middle] == target:
        return middle 
    elif values[middle] > target:
        return binary_search(target,values[:middle]) 
    else:
        return middle + binary_search(target, values[middle:]) if binary_search(target, values[middle+1:]) != -1 else -1

    
