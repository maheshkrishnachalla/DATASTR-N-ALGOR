"""
Longest Substring Without Repeating Characters

Input: s = "geeksforgeeks"
Output: 7
Explanation: The longest substrings without repeating characters are "eksforg” and "ksforge", with lengths of 7.

Input: s = "aaa"
Output: 1
Explanation: The longest substring without repeating characters is "a"

Input: s = "abcdefabcbb"
Output: 6
Explanation: The longest substring without repeating characters is "abcdef".

"""

def longest_substring_without_repeating_characters(st):
    n = len(st)
    if n <=1 :
        return n
    p1 = 0
    p2 = 0
    lastIndex = [-1]*26
    result = 0
    max_len = 0
    while p2 < n:

        p1 = max(p1, lastIndex[ord(st[p2]) - ord('a')] +1)

        result = max(result, p2-p1 + 1)

        if max_len < len(st[p1:p2+1]):
            max_len = len(st[p1:p2+1])
        print(st[p1:p2+1])
        lastIndex[ord(st[p2]) - ord('a')] = p2
        p2 = p2+1

    return result

s = "geeksforgeeks"
result = longest_substring_without_repeating_characters(st=s)
print(result)


