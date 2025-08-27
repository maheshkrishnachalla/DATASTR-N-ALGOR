"""
Given array = [2, 7, 9, 11, 14, 3, 5, 8, 10]
target = 9

output : [0, 1]
"""

array = [2, 7, 9, 11, 14, 3, 5, 8, 10]
target = 20

def find_indices_of_sum(arr, target):
    indices = {}
    dt = enumerate(arr)
    print(dt.__doc__)
    for i, v in enumerate(arr):
        if target - v in indices:
            return [indices[target-v], i]
        indices[v] = i
    return []


result = find_indices_of_sum(arr=array, target=target)
print(result)

