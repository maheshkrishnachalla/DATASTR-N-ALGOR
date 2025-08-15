"""
find the repeated sub_string in string

"""

def find_repeated_substring(s):
    n = len(s)
    p1 = 0
    p2 = 1
    lon_str = ''
    sub_str = ''
    i = 1
    if n==1 or n == 0:
        return 'not repeated string'
    while n>i:
        if s[p1] == s[p2]:
            sub_str = s[p1:p2+1]
        else:
            p1 = p2
        p2 = p2+1
        if len(sub_str) > len(lon_str) :
            lon_str = sub_str
        i +=1
    return  lon_str


def find_all_repeated_substrings(s):
    max_len = 1
    runs = []
    i = 0
    while i < len(s):
        char = s[i]
        j = i
        while j < len(s) and s[j] == char:
            j += 1
        length = j-i
        if length > max_len:
            max_len = length
            #runs = [s[i:j]]
            runs.append(s[i:j])
        elif length == max_len:
            runs.append(s[i:j])
        i = j
    return  runs




# Example usage
s = "pppwwkewwwsboss"

#s = 'ppwwekkkewww'
print(find_repeated_substring(s=s))
print(find_all_repeated_substrings(s=s))
