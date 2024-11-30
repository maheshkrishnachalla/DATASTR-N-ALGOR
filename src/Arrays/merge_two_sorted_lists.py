"""

numA = [2,4,6,7,10,11,13]
numB = [1,3,5,8,9,12,14,16,18,20]
"""
def merge_two_sort_list(num1, num2):
    merged_list = []
    i, j = 0,0
    while i < len(num1) and j < len(num2):
        if num1[i] <= num2[j]:
            merged_list.append(num1[i])
            i += 1
        else:
            merged_list.append(num2[j])
            j += 1
    #print(num1[i:])
    #print(num2[j:])
    merged_list.extend(num1[i:])
    merged_list.extend(num2[j:])
    return merged_list

num1 = [2,4,6,7,10,11,13,15]
num2 = [1,3,5,8,9,12,14,16,18,20,21,23,26]

result =merge_two_sort_list(num1=num1, num2=num2)
print(result)