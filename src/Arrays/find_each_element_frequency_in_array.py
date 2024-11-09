"""
Given a sorted array arr[] of positive integers,
the task is to find the frequency for each element in the array.
Assume all elements in the array are less than some constant M

Note: Do this without traversing the complete array.
i.e. expected time complexity is less than O(n)

Examples:
Input: arr[] = [1, 1, 1, 2, 3, 3, 5, 5, 8, 8, 8, 9, 9, 10]
Output:
Element 1 occurs 3 times
Element 2 occurs 1 times
Element 3 occurs 2 times
Element 5 occurs 2 times
Element 8 occurs 3 times
Element 9 occurs 2 times
Element 10 occurs 1 times

Input: arr[] = [2, 2, 6, 6, 7, 7, 7, 11]
Output:
Element 2 occurs 2 times
Element 6 occurs 2 times
Element 7 occurs 3 times
Element 11 occurs 1 times

"""


def find_frequency_of_element_in_array(arr: list[int], n: int):
    first_ele = arr[0]
    count = 1
    index = 1
    while index < n:
        if arr[index-1] == arr[index]:
            count +=1
            index +=1
        else:
            print(arr[index],"occurs",count,"times")
            first_ele = arr[index]
            count = 1
            index +=1

if __name__ == '__main__':
    arr = [2, 2, 6, 6, 7, 7, 7, 11,11]
    find_frequency_of_element_in_array(arr=arr, n=len(arr))
