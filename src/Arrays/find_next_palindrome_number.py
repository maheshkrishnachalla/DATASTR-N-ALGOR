"""
find the next palindrome number
ex:
n = 123
result = 131

n = 99999
result = 100001
"""
def next_palindrome(n):
    """
    n type: int
    :return:int
    """
    m = n+1
    sum = 0
    while m>0:
        n = m
        sum = 0
        while n > 0:
            r = n%10
            sum = sum*10 + r
            n = n//10
        #print(m)
        #print(sum)
        if m == sum:
            break
        else:
            m = m+1
    return  sum


result = next_palindrome(n=99999)
print(result)