import datetime
import re
import timeit


def isPalindrome(text):
    text = "".join([i for i in text.lower() if i.isalnum()])
    return text==text[::-1]

def isPalindrome_with_re(text):
    text = re.sub("[^a-z0-9]","",text.lower())
    return text==text[::-1]


#text = "1A man, a plan a canal: Panama1"
text = "SIS"
start_time = datetime.datetime.now()
result = isPalindrome(text=text)
print(result)
end_time = datetime.datetime.now()
print(end_time - start_time)
start_time = datetime.datetime.now()
print(isPalindrome_with_re(text=text))
end_time = datetime.datetime.now()
print(end_time - start_time)