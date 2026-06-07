"""
Group Anagrams Together
Input: arr[] = ["act", "god", "cat", "dog", "tac"]
Output: [["act", "cat", "tac"], ["god", "dog"]]
Explanation: There are 2 groups of anagrams "god", "dog" make group 1. "act", "cat", "tac" make group 2.

Input: arr[] = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
Output: [["abc", "cab", "bac"], ["listen", "silent", "enlist"],["rat", "tar", "art"]]
Explanation:
Group 1: "abc", "bac" and "cab" are anagrams.
Group 2: "listen", "silent" and "enlist" are anagrams.
Group 3: "rat", "tar" and "art" are anagrams.
"""


def group_anagrams_list(arr):
    anagram_groups  = {}
    for word in arr :
        sorted_word = ''.join(sorted(word))

        if  sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]

    return list(anagram_groups.values())

arr = ["act", "god", "cat", "dog", "tac"]
result = group_anagrams_list(arr=arr)
print(result)