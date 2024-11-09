"""
given array , find the product of values except the index value 
in array
A=List(1,2,3,4,5)

out = List(120,60,40,30,24)
120 = 2x3x4x5
60 = 1x3x4x5
40 = 1x2x4x5
30 = 1x2x3x5
24 = 1x2x3x4

"""

def find_product_of_element(arr:list) -> list:
    p = 1
    for i in arr:    # O(n)
        p = p*i
    return [p//j for j in arr] #O(n)

arr = list(map(float,input("enter list :").split())) #[1,2,3,4,5]
result = find_product_of_element(arr=arr)
print(result)