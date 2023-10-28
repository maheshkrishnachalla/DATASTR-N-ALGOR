import random as rn
import time


def selection_sort(arr):
    
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min],arr[i]

#arr = [20,15,12,10,14,2]
arr  = rn.sample(range(1,1000),10)
print(arr)
start = time.time()
selection_sort(arr=arr)
end = time.time()
print(arr)
print(end - start, "secs")