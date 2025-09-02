"""
Given a string val str = "abbabcdexeabc".
Find the substring with max length with non-repeating characters.
Output : "abcdex
"""
from collections import defaultdict


def find_max_non_repeat_sub_string(st:str):
    lookup = {'-1':1}
    start = 0
    max_start = 0
    max_length = 0
    for end in range(0, len(st)):
        c = st[end]
        if c in lookup and lookup[c] >= start:
            start = lookup[c] + 1
        lookup[c] = end
        if end - start + 1  > max_length:
            max_length = end - start + 1
            max_start = start
        print(max_start, max_length)
    return st[max_start:max_start+max_length]

st = input("Enter String :")
result = find_max_non_repeat_sub_string(st=st)
print(result)
