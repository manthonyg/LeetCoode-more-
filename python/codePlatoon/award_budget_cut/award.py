def find_grants_cap(grantsArray, newBudget):
    grantsArray.sort()
    print(grantsArray)
    num_grants = len(grantsArray)
    cum = 0
    for i,grant in enumerate(grantsArray):
        cap = (newBudget - cum) / (num_grants - i)
        if cap <= grant:
            return cap
        cum += grant
    

print(find_grants_cap([2, 100, 50, 120, 1000], 190))
print(find_grants_cap([2,4],3))
print(find_grants_cap([210, 200, 150, 193, 130, 110, 209, 342, 117], 1530))
print(find_grants_cap(
    [2, 100, 50, 120, 167], 400))

