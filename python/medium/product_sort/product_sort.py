import collections
def product_sort(nums):
    # cache = collections.defaultdict(int)
    # for num in nums:
    #     cache[num] += 1
    
    # cache = {k: v for k, v in sorted(cache.items(), key=lambda item: (item[1],item[0]))}
    # result = []
    # for k,v in cache.items():
    #     result += [k] * v
    # return result

    count = collections.Counter(nums)
    sorted_list = sorted(nums, key=lambda item: (count[item], item))
    return sorted_list
