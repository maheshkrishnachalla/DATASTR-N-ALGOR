"""
Given array = [2, 7, 9, 11, 14, 3, 5, 8, 10]
target = 9

output : [0, 1]
"""
from operator import indexOf

array = [2, 7, 9, 11, 14, 3, 5, 8, 10]
target = 14

def find_indices_of_sum(arr, target):
    indices = {}
    dt = enumerate(arr)
    print(dt.__doc__)
    for i, v in enumerate(arr):
        if target - v in indices:
            return [indices[target-v], i]
        indices[v] = i
    return []


def find_indices_of_sum_list(arr, target):
    lt = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)-1):
            if arr[i]+arr[j]== target:
                lt.append((i,j))

    return lt

result = find_indices_of_sum(arr=array, target=target)
print(result)

result2 = find_indices_of_sum_list(arr=array, target=target)
print(result2)

