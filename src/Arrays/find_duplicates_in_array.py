
def find_duplicates_in_array(arr):
    seen = set()
    dups = set()
    for i in arr:
        if i in seen:
            dups.add(i)
        else:
            seen.add(i)
    return dups


def find_dups_in_brute(arr):
    dups = []
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j] and arr[j] not in dups:
                dups.append(arr[i])
    return dups

arr = [1,4,2,5,7,3,6,4,2,1,3,6,5,4,3,8,9,4,5,8]
result = find_duplicates_in_array(arr=arr)
print(result)
result2 = find_dups_in_brute(arr=arr)
print((result2))
