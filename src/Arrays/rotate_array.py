"""
Given a list of integers, rotate the list to the right by k steps.
Input: [1, 2, 3, 4, 5], k=2
 Output: [4, 5, 1, 2, 3]
"""
from collections import deque


def rotate_array_to_right(arr:list[int], k:int):
    n = len(arr)
    k = k%n
    print(arr[-k:])
    print(arr[:-k])
    arr =  arr[:-k] + arr[-k:]
    return arr


def rotate_array_to_left(arr:list[int], k:int):
    n = len(arr)
    k = k%n
    print(arr[:k])
    print(arr[k:])
    arr =   arr[k:] + arr[:k]
    return arr

arr = [1,2,3,4,5]
k = int(input("Enter k = "))

right_rotated_array = rotate_array_to_right(arr=arr, k=k)
print(right_rotated_array)

left_rotated_array = rotate_array_to_left(arr=arr, k=k)
print(left_rotated_array)

dequed_arr_right = deque(arr)
dequed_arr_right.rotate(k)
print([i for i in dequed_arr_right])

dequed_arr_left = deque(arr)
dequed_arr_left.rotate(-k)
print([i for i in dequed_arr_left])
