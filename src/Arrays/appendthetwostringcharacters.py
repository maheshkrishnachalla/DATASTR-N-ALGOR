"""
word1= 'abcd'
word2 = 'pq'
output = 'apbqcd'
"""


def appendcharactersofword(word1, word2):
    N = len(word1)
    M = len(word2)
    i = 0
    j = 0
    lt = []
    while i < N and j < M:
        lt.append(word1[i])
        lt.append(word2[j])
        i += 1
        j += 1
    lt.append(word1[i:])
    lt.append(word2[j:])

    return ''.join(lt)


word1 = 'abcd'
word2 = 'pq'

result = appendcharactersofword(word1, word2)
print(result)