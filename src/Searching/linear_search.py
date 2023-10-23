def linear_search(arr, target):
    for i in range(len(arr)):
        n = arr[i]
        if n == target:
            return i
    return -1

arr  = [4,6, 5,9,1, 3,7]
indx = linear_search(arr=arr,target=7)
print(indx)
