
def find_numerics(arr):
    lt = []
    for i in arr:
        if str(i).isdigit():
            lt.append(i)

    return lt


def find_numerics_with_instance(arr):
    return [x for x in arr if isinstance(x, int)]
arr = [1,'a',2,3,'b','c',4,'d',5,'e']
result = find_numerics(arr)
print(result)
result2 = find_numerics_with_instance(arr=arr)
print(result2)