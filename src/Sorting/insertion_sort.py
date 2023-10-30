import random as rn
import time

def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        last = i-1
        while last >= 0 and key < arr[last]:
            arr[last + 1] = arr[last]
            last = last - 1
        arr[last + 1] = key
    
    return arr
    
#arr = [5,4,3,2,1]
arr  = rn.sample(range(1,1000),10)
print("input array =",arr)
start = time.time()
insertion_sort(arr=arr)
end = time.time()
print("sorted array =",arr)
print("time =",end-start,"secs")