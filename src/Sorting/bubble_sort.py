import random as rn
import time

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
        print(arr)
    return arr

#arr = [29,10,14,37,12,19,24]
arr  = rn.sample(range(1,100),10)
print("input :", arr)
start = time.time()
result = bubble_sort(arr=arr)
end = time.time()
print("output :", result)
print(end - start, "secs")