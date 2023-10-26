def binary_search_recursion(array, target):
    start = 0
    end = len(array)-1
    return helper(array, target, start, end)

def helper(array, target, start, end):
    mid = (start+end)//2
    mid_elem = array[mid]
    if start>end:
        return -1
    elif target == mid_elem:
        return mid
    elif target < mid_elem:
        end = mid - 1
    else:
        start = mid + 1
    return helper(array=array, target=target, start=start, end=end)

arr = [2,4,5,6,7,8,9,15,20,25,30,32,35]
target = int(input("Enter number: "))
result = binary_search_recursion(array=arr, target=target)
print("Index of",target,"is",result )