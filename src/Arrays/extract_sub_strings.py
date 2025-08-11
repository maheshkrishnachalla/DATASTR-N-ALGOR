st = "aaaattaaayyayattaa000aaaattaayyaaaa"

def get_sub_strings(s):
    subs = "".join([i if i=='a' else ' ' for i in s])
    subs = [i for i in subs.split(" ") if len(i)>0]
    return subs

result = get_sub_strings(s=st)
print(result)
