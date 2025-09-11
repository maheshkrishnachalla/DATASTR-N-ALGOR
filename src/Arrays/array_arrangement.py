"""
Modify a given array of integers so that the first element is the smallest,
the second is the largest, the third is the second-smallest,
the fourth is the second-largest,and so on.
Constraints

The input variable arr is a list of integers.
The length of arr can be any non-negative integer.
The elements in arr can be positive, negative, or zero.
There are no specific constraints on the range of values for the elements in arr.

Input: [13, 7, 8, 3, 2, 10, 15, -1]
Output: [-1, 15, 2, 13, 3, 10, 7, 8]

Input: [-5, -12, -1, 7, 14, -7, 3, 6]
Output: [-12, 14, -7, 7, -5, 6, -1, 3]

Input: [3, 6, 9, -10, -5, -2, 0, 8]
Output: [-10, 9, -5, 8, -2, 6, 0, 3]

"""

def modify_array(arr):
    for i in range(len(arr)):
        if i%2 == 0:
            cur_min = min(arr[i:])
            arr[arr.index(cur_min)] = arr[i]
            arr[i] = cur_min
        if i%2 == 1:
            cur_max = max(arr[i:])
            arr[arr.index(cur_max)] = arr[i]
            arr[i] = cur_max


    return arr


arr = [13, 7, 8, 3, 2, 10, 15, -1]
print(arr)
result = modify_array(arr=arr)
print(result)