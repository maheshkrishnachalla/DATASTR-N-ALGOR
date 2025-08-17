"""
You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates.
You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order.
Example

Perform the following steps:
i   arr                         swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]
It took  swaps to sort the array.
Function Description
Complete the function minimumSwaps in the editor below.
minimumSwaps has the following parameter(s):
int arr[n]: an unordered array of integers
Returns
int: the minimum number of swaps to sort the array
Input Format
The first line contains an integer, , the size of .
The second line contains  space-separated integers .
Constraints


Sample Input 0
4
4 3 1 2
Sample Output 0
3
Sample Input 1
5
2 3 4 1 5
Sample Output 1
3
Sample Input 2
7
1 3 5 2 4 6 7
Sample Output 2
3
"""
import os


def minimum_swaps(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] != i+1:
            for j in range(i+1, n):
                if arr[j] == i+1:
                    count += 1
                    arr[i], arr[j] = arr[j], arr[i]
        print(arr)
    return count

def minimum_swaps2(arr):
    n = len(arr)
    count = 0
    i = 0
    while i < n:
        right_value = i+1
        if arr[i] != right_value:
            swap_index = arr[i] - 1
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
            count += 1
        else:
            i +=1
        print(arr)
    return count


if __name__ == '__main__':
    #fptr = open('*/output.txt', 'w')
    n = int(input("Enter n :"))
    arr = list(map(int, input().rstrip().split()))
    res = minimum_swaps2(arr=arr)
    print(res)
    #fptr.write(str(res) + '\n')
    #fptr.close()