
def two_sum(arr , target):
    seen = set()
    for i in arr:
        if target - i in seen:
            return True
        seen.add(i)
    return False


def pair_sum_with_sorting(arr, target):
    left = 0
    right = len(arr) -1
    arr.sort()
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return True
        elif sum < target:
            left += 1
        else:
            right -= 1
    return False


def sort_array(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    #recursively sort both
    left_sort = sort_array(left)
    right_sort = sort_array(right)

    return  merge(left_sort, right_sort)

def merge(left, right):
    merged_list = []
    i , j = 0, 0

    #compare the elements in both the list and add the smallest one to the list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    # any remaining elements from both sub arrays merged
    merged_list.extend(left[i:])
    merged_list.extend(right[j:])

    return merged_list


#arr = [1, 5, 6, 10, 11, 13, 16, 18, 19, 20]
arr = [1, 5, 6, 10, 2, 3, 4, 11,7, 13, 8, 16, 18, 17, 19, 15, 20]
target = 28

print("original arr :", arr)
print(two_sum(arr=arr, target=target))
print(sort_array(arr=arr))
print(pair_sum_with_sorting(arr=arr, target=target))