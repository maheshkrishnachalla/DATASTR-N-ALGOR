"""
Given an array of size N.
The task is to find the maximum and the minimum element of the array
using the minimum number of comparisons.

Examples:

Input: arr[] = {3, 5, 4, 1, 9}
Output: Minimum element is: 1
              Maximum element is: 9


Input: arr[] = {22, 14, 8, 17, 35, 3}
Output:  Minimum element is: 3
              Maximum element is: 35

"""
def find_min_and_max_element_in_array(arr:list[int]):
    min = arr[0]
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]

    return min, max

arr = [3, 5, 4, 1, 9]#[22, 14, 8, 17, 35, 3]
result = find_min_and_max_element_in_array(arr=arr)
print("minimum value :", result[0])
print("maximum value :", result[1])



