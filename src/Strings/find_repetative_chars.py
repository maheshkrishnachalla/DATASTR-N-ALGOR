"""
Given
st = 'this is new string given find the 2nd and 3rd largest repetative character'
"""


def find_repetative_chars(st):
    lookup = {}
    filtered_str = ''.join([ch for ch in st if ch.isalpha()])
    print(filtered_str)
    for i in filtered_str:
        if i in lookup:
            lookup[i] += 1
        else:
            lookup[i] = 1
    sorted_lookup = sorted(lookup.items(), key= lambda x: x[1], reverse=True)
    print(sorted_lookup)
    second_max = sorted_lookup[1][0] if sorted_lookup[1][1] > 1 else None
    third_max = sorted_lookup[2][0] if sorted_lookup[2][1] > 2 else None
    return  second_max, third_max

st = 'this is new string given find the 2nd and 3rd largest repetative character'

result = find_repetative_chars(st=st)
print(result)