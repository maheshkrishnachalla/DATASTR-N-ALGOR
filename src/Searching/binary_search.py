import random as rn
def binary_search(arr, start, end, target):
    mid = (end+start)//2
    if start<=end:
        m = arr[mid] 
        s = arr[start]
        e = arr[end]
        if s == target:
            return start
        elif e == target:
            return end
        elif m == target:
            return mid
        elif m > target:
            end = mid-1
        elif m < target:
            start = mid+1
        return binary_search(arr=arr, start=start,end=end, target=target)
    else:
        return -1

arr  = [i for i in range(0,100,rn.randint(1,4))]
print(arr)
#arr  = [2,4,5,7,8,9,15,20,25,30,32,35]
target = int(input("Enter number :"))
start = 0
end = len(arr) - 1
res = binary_search(arr=arr, start=start, end=end,target=target)
print("index of target {target} =".format(target=target), res)