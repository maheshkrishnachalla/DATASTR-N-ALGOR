import time
import random as rn 
import math as m
def binary_search(arr, target):
    end = len(arr)-1
    start = 0
    while start<=end:
        mid = (end+start)//2
        if arr[mid] > target:
            end = mid-1
        elif arr[mid] < target:
            start = mid + 1
        else:
            return mid
    return -1 
    


if __name__ == "__main__":
    N = int(input("Enter list range = "))
    target = int(input("Enter number = "))
    #arr = [1,2,4,7,8,9,10,12,14,18,19,20,24,26,30,32,38,40]
    start_time = time.time()
    arr = [i for i in range(1,N, rn.randint(1,4))]
    print("log =", m.log2(N))
    #print(arr)
    result = binary_search(arr=arr, target=target)
    print("index of {target} =".format(target=target), result)
    end_time = time.time()
    print((end_time - start_time),"seconds")
