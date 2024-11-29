"""
val input= List("tea","acb","apt","bac","eat","ate","tap","pen") 

anagram : character same but order can be different

val output=List(List("acb","bac"),List("tea","eat","ate"),List("apt","tap"),List("pen"))

"""
from collections import defaultdict
def get_anagram(arr):
    dt = defaultdict(list)
    #print(dt)
    for word in arr:
        key = "".join(sorted(word))
        dt[key].append(word)

    anagrams_in_list = ', '.join([",".join(v) for k, v in dt.items() if len(v) > 1])
    not_an_anagrams_in_list = ', '.join([",".join(v) for k, v in dt.items() if len(v) == 1])
    print("anagrams in list :", anagrams_in_list)
    print("not anagrams in list :",not_an_anagrams_in_list)
    
    return [v for v in dt.values()]

arr = ["tea","acb","apt","bac","eat","ate","tap","pen"]
print("Both anagrams and Not anagrams in list :",get_anagram(arr=arr))