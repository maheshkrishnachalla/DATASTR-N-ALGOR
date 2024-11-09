import random as rn
import time


def selection_sort(arr):
    
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min],arr[i]
        print(arr)

#arr = [20,15,12,10,14,2]
arr  = rn.sample(range(1,100),10)
print("input :", arr)
start = time.time()
selection_sort(arr=arr)
end = time.time()
print("output :", arr)
print(end - start, "secs")